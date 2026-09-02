import random
from dataclasses import dataclass

from Data.location_data import SEA_PROVINCES, PROVINCE_DATA, get_legal_neighbors_for_unit
from Data.supply_centers import STARTING_SUPPLY_CENTERS


PREDICTIVE_WEIGHTS = {
    "sc": 2.0,
    "units": 0.9,
    "strategic_position": 18.0,
    "operational_efficiency": 2.0,
    "center_conversion_rate": 2.5,
    "threat_coverage_rate": 1.5,
    "front_concentration": 1.0,
    "allied_support_rate": 0.5,
    "cgi": 4.0,
    "ema_momentum": 1.6,
    "momentum": 1.2,
    "unit_growth": 0.8,
    "isolation": -2.0,
    "encirclement": -3.0,
}


@dataclass(frozen=True)
class SimulatedUnit:
    country: str
    unit_type: str
    province: str


@dataclass
class SimulationState:
    year: int
    season: str
    units_by_province: dict
    sc_owners: dict

    @classmethod
    def from_game_state(cls, game_state):
        board = game_state.board
        return cls(
            year=game_state.year,
            season=game_state.season,
            units_by_province={
                province: SimulatedUnit(unit.country, unit.unit_type, province)
                for province, unit in board.units_by_province.items()
            },
            sc_owners=board.sc_owners.copy(),
        )

    def copy(self):
        return SimulationState(
            year=self.year,
            season=self.season,
            units_by_province=self.units_by_province.copy(),
            sc_owners=self.sc_owners.copy(),
        )


@dataclass
class MovementResolution:
    state: SimulationState
    successful_moves: set
    bounced_moves: set
    dislodged_units: dict
    dislodged_by: dict
    cut_supports: set


@dataclass
class WinterResolution:
    state: SimulationState
    builds: list
    removals: list
    unfilled_builds: dict
    unfilled_removals: dict


@dataclass
class RetreatResolution:
    state: SimulationState
    successful_retreats: dict
    disbanded_units: dict
    contested_destinations: set


@dataclass
class SimulationResult:
    state: SimulationState
    winner: str | None
    terminal_reason: str
    movement_seasons: int
    stagnant_seasons: int


class MonteCarloEngine:
    """
    Win-probability forecast based on the full strategic state of each country.
    It incorporates center count, unit posture, momentum, EMA growth, CGI, and
    operational exposure so the predicted winner reflects the broader game state.
    """

    def __init__(self, seed=None):
        self.random = random.Random(seed)

    def create_simulation_state(self, game_state):
        return SimulationState.from_game_state(game_state)

    def _policy_weights(self, country_state):
        posture = getattr(country_state, "posture", "Balanced")
        offensive = float(getattr(country_state, "offensive_posture", 0.0))
        defensive = float(getattr(country_state, "defensive_posture", 0.0))
        weights = {
            "capture_center": 2.0 + offensive,
            "attack_enemy": 1.0 + offensive,
            "defend_center": 1.0 + defensive,
            "hold": 0.4 + defensive,
            "risk": 0.5 + offensive,
        }
        if posture == "Aggressive":
            weights["capture_center"] += 1.2
            weights["attack_enemy"] += 0.8
            weights["hold"] -= 0.25
        elif posture == "Defensive":
            weights["defend_center"] += 1.2
            weights["hold"] += 0.8
            weights["risk"] -= 0.25
        return weights

    def generate_unit_candidates(self, simulation_state, country_state, unit):
        """Return weighted hold/move intentions for one unit without resolving them."""
        weights = self._policy_weights(country_state)
        candidates = [{"action": "HOLD", "from": unit.province, "weight": weights["hold"]}]
        for destination in get_legal_neighbors_for_unit(unit.province, unit.unit_type):
            destination_owner = simulation_state.sc_owners.get(destination)
            occupying_unit = simulation_state.units_by_province.get(destination)
            weight = weights["risk"]
            if destination_owner is not None and destination_owner != unit.country:
                weight += weights["capture_center"]
            if occupying_unit and occupying_unit.country != unit.country:
                weight += weights["attack_enemy"]
            if destination_owner == unit.country:
                weight += weights["defend_center"]
            candidates.append({
                "action": "MOVE",
                "from": unit.province,
                "to": destination,
                "weight": max(0.05, weight),
            })
        return candidates

    def choose_unit_intent(self, simulation_state, country_state, unit):
        candidates = self.generate_unit_candidates(simulation_state, country_state, unit)
        total_weight = sum(candidate["weight"] for candidate in candidates)
        roll = self.random.uniform(0, total_weight)
        for candidate in candidates:
            roll -= candidate["weight"]
            if roll <= 0:
                return candidate
        return candidates[-1]

    def _convoy_route(self, units, convoys, origin, destination):
        """Return an unbroken convoy-fleet route for an army move, if one exists."""
        convoy_fleets = {
            province for province, intent in convoys.items()
            if intent.get("convoy_from") == origin
            and intent.get("convoy_to") == destination
            and units[province].unit_type == "F"
            and province in SEA_PROVINCES
        }
        starting_fleets = [
            province for province in convoy_fleets
            if origin in get_legal_neighbors_for_unit(province, "F")
        ]
        pending = [(province, [province]) for province in starting_fleets]
        visited = set(starting_fleets)
        while pending:
            province, route = pending.pop(0)
            if destination in get_legal_neighbors_for_unit(province, "F"):
                return route
            for neighbor in get_legal_neighbors_for_unit(province, "F"):
                if neighbor in convoy_fleets and neighbor not in visited:
                    visited.add(neighbor)
                    pending.append((neighbor, route + [neighbor]))
        return None

    def resolve_movement(self, simulation_state, intents):
        """Resolve a movement phase with supports and non-paradoxical convoy routes."""
        units = simulation_state.units_by_province
        normalized_intents = {
            province: {"action": "HOLD", "from": province}
            for province in units
        }
        for intent in intents:
            origin = intent.get("from")
            unit = units.get(origin)
            action = str(intent.get("action", "HOLD")).upper()
            if not unit or action not in {"HOLD", "MOVE", "SUPPORT", "CONVOY"}:
                continue
            if (
                action == "MOVE"
                and not intent.get("via_convoy")
                and intent.get("to") not in get_legal_neighbors_for_unit(origin, unit.unit_type)
            ):
                continue
            if action == "CONVOY" and (
                unit.unit_type != "F"
                or origin not in SEA_PROVINCES
                or not intent.get("convoy_from")
                or not intent.get("convoy_to")
            ):
                continue
            normalized_intents[origin] = {**intent, "action": action, "from": origin}

        convoys = {
            origin: intent for origin, intent in normalized_intents.items()
            if intent["action"] == "CONVOY"
        }
        convoy_routes = {}
        for origin, intent in normalized_intents.items():
            unit = units[origin]
            if intent["action"] != "MOVE" or not intent.get("via_convoy"):
                continue
            route = self._convoy_route(units, convoys, origin, intent.get("to"))
            if unit.unit_type != "A" or not route:
                normalized_intents[origin] = {"action": "HOLD", "from": origin}
            else:
                convoy_routes[origin] = route

        moves = {
            origin: intent for origin, intent in normalized_intents.items()
            if intent["action"] == "MOVE"
        }
        supports = {
            origin: intent for origin, intent in normalized_intents.items()
            if intent["action"] == "SUPPORT"
        }

        cut_supports = set()
        for supporter, support in supports.items():
            support_target = support.get("support_to") or support.get("to")
            support_origin = support.get("support_from")
            supporter_unit = units[supporter]
            supported_intent = normalized_intents.get(support_origin, {})
            if not support_target or not support_origin:
                cut_supports.add(supporter)
                continue
            if support_target not in get_legal_neighbors_for_unit(supporter, supporter_unit.unit_type):
                cut_supports.add(supporter)
                continue
            if support_target != support_origin and (
                supported_intent.get("action") != "MOVE"
                or supported_intent.get("to") != support_target
            ):
                cut_supports.add(supporter)
                continue
            for attacker_origin, attack in moves.items():
                attacker = units[attacker_origin]
                if attack.get("to") == supporter and attacker.country != supporter_unit.country:
                    if attacker_origin != support_target:
                        cut_supports.add(supporter)
                        break

        move_strengths = {origin: 1 for origin in moves}
        hold_strengths = {origin: 1 for origin in units}
        for supporter, support in supports.items():
            if supporter in cut_supports:
                continue
            support_origin = support.get("support_from")
            support_target = support.get("support_to") or support.get("to")
            supported_unit = units.get(support_origin)
            if not supported_unit:
                continue
            if support_target == support_origin:
                hold_strengths[support_origin] += 1
            elif moves.get(support_origin, {}).get("to") == support_target:
                move_strengths[support_origin] += 1

        bounced_moves = set()
        destinations = {}
        for origin, move in moves.items():
            destinations.setdefault(move["to"], []).append(origin)

        move_winners = {}
        for destination, attackers in destinations.items():
            strongest = max(move_strengths[origin] for origin in attackers)
            strongest_attackers = [origin for origin in attackers if move_strengths[origin] == strongest]
            if len(strongest_attackers) != 1:
                bounced_moves.update(attackers)
                continue
            move_winners[destination] = strongest_attackers[0]

        resolution_cache = {}
        resolving = set()

        def move_succeeds(origin):
            if origin in resolution_cache:
                return resolution_cache[origin]
            if origin in resolving:
                return True

            resolving.add(origin)
            destination = moves[origin]["to"]
            if move_winners.get(destination) != origin:
                succeeds = False
            else:
                defender = units.get(destination)
                defender_move = moves.get(destination)
                if not defender:
                    succeeds = True
                elif defender.country == units[origin].country:
                    succeeds = bool(defender_move) and move_succeeds(destination)
                elif not defender_move:
                    succeeds = move_strengths[origin] > hold_strengths[destination]
                elif defender_move["to"] == origin:
                    succeeds = move_strengths[origin] > move_strengths[destination]
                else:
                    succeeds = move_succeeds(destination)

            resolving.remove(origin)
            resolution_cache[origin] = succeeds
            return succeeds

        successful_moves = {
            origin for origin in moves
            if move_succeeds(origin)
        }
        dislodged_fleet_origins = {
            moves[origin]["to"] for origin in successful_moves
            if moves[origin]["to"] in convoys
            and units[moves[origin]["to"]].country != units[origin].country
        }
        disrupted_convoys = {
            origin for origin, route in convoy_routes.items()
            if any(fleet in dislodged_fleet_origins for fleet in route)
        }
        successful_moves -= disrupted_convoys
        bounced_moves.update(set(moves) - successful_moves)

        final_state = simulation_state.copy()
        dislodged_units = {}
        for origin in successful_moves:
            destination = moves[origin]["to"]
            defender = units.get(destination)
            if defender and defender.country != units[origin].country:
                dislodged_units[destination] = defender
            final_state.units_by_province.pop(origin, None)

        for origin in successful_moves:
            destination = moves[origin]["to"]
            unit = units[origin]
            final_state.units_by_province[destination] = SimulatedUnit(
                unit.country,
                unit.unit_type,
                destination,
            )

        return MovementResolution(
            state=final_state,
            successful_moves=successful_moves,
            bounced_moves=bounced_moves,
            dislodged_units=dislodged_units,
            dislodged_by={
                destination: origin
                for origin in successful_moves
                for destination in [moves[origin]["to"]]
                if destination in dislodged_units
            },
            cut_supports=cut_supports,
        )

    def resolve_retreats(self, movement_resolution, country_states):
        """Retreat dislodged units to unoccupied legal provinces or disband them."""
        state = movement_resolution.state.copy()
        proposed_retreats = {}
        for origin, unit in movement_resolution.dislodged_units.items():
            attacker_origin = movement_resolution.dislodged_by.get(origin)
            country_state = country_states.get(unit.country)
            weights = self._policy_weights(country_state) if country_state else {"defend_center": 1.0, "risk": 0.5}
            candidates = [
                province for province in get_legal_neighbors_for_unit(origin, unit.unit_type)
                if province != attacker_origin and province not in state.units_by_province
            ]
            if not candidates:
                continue

            scored = []
            for province in candidates:
                owner = state.sc_owners.get(province)
                score = self.random.random() * 0.2
                if owner == unit.country:
                    score += weights["defend_center"]
                elif owner not in (None, "", "Neutral"):
                    score += weights["risk"]
                scored.append((score, province))
            proposed_retreats[origin] = max(scored)[1]

        destinations = {}
        for origin, destination in proposed_retreats.items():
            destinations.setdefault(destination, []).append(origin)
        contested_destinations = {
            destination for destination, origins in destinations.items()
            if len(origins) > 1
        }
        successful_retreats = {}
        disbanded_units = {}
        for origin, unit in movement_resolution.dislodged_units.items():
            destination = proposed_retreats.get(origin)
            if not destination or destination in contested_destinations:
                disbanded_units[origin] = unit
                continue
            state.units_by_province[destination] = SimulatedUnit(
                unit.country,
                unit.unit_type,
                destination,
            )
            successful_retreats[origin] = destination

        return RetreatResolution(
            state=state,
            successful_retreats=successful_retreats,
            disbanded_units=disbanded_units,
            contested_destinations=contested_destinations,
        )

    def resolve_winter(self, simulation_state, adjustments=None):
        """Apply legal Winter builds and removals without mutating the source state."""
        adjustments = adjustments or []
        final_state = simulation_state.copy()
        countries = {
            unit.country for unit in final_state.units_by_province.values()
        } | {
            owner for owner in final_state.sc_owners.values()
            if owner not in (None, "", "Neutral")
        }
        builds_by_country = {}
        removals_by_country = {}
        for adjustment in adjustments:
            country = adjustment.get("country")
            action = str(adjustment.get("action", "")).upper()
            if action == "BUILD":
                builds_by_country.setdefault(country, []).append(adjustment)
            elif action in {"REMOVE", "DISBAND"}:
                removals_by_country.setdefault(country, []).append(adjustment)

        builds = []
        removals = []
        unfilled_builds = {}
        unfilled_removals = {}
        for country in sorted(countries):
            owned_centers = {
                province for province, owner in final_state.sc_owners.items()
                if owner == country
            }
            country_units = {
                province: unit for province, unit in final_state.units_by_province.items()
                if unit.country == country
            }
            adjustment = len(owned_centers) - len(country_units)
            if adjustment > 0:
                home_centers = {
                    province for province, owner in STARTING_SUPPLY_CENTERS.items()
                    if owner == country
                }
                legal_sites = sorted(
                    home_centers & owned_centers - set(final_state.units_by_province)
                )
                requested = builds_by_country.get(country, [])
                for order in requested:
                    province = order.get("province")
                    unit_type = str(order.get("unit_type", "A")).upper()
                    if len([build for build in builds if build["country"] == country]) >= adjustment:
                        break
                    if (
                        province not in legal_sites
                        or unit_type not in {"A", "F"}
                        or (unit_type == "F" and not PROVINCE_DATA.get(province, {}).get("coastal"))
                    ):
                        continue
                    final_state.units_by_province[province] = SimulatedUnit(country, unit_type, province)
                    legal_sites.remove(province)
                    builds.append({"country": country, "unit_type": unit_type, "province": province})

                while len([build for build in builds if build["country"] == country]) < adjustment and legal_sites:
                    province = legal_sites.pop(0)
                    final_state.units_by_province[province] = SimulatedUnit(country, "A", province)
                    builds.append({"country": country, "unit_type": "A", "province": province})

                missing = adjustment - len([build for build in builds if build["country"] == country])
                if missing:
                    unfilled_builds[country] = missing
            elif adjustment < 0:
                required_removals = abs(adjustment)
                requested = removals_by_country.get(country, [])
                removed_provinces = set()
                for order in requested:
                    province = order.get("province")
                    unit = final_state.units_by_province.get(province)
                    if len(removed_provinces) >= required_removals:
                        break
                    if unit and unit.country == country:
                        final_state.units_by_province.pop(province)
                        removed_provinces.add(province)
                        removals.append({"country": country, "unit_type": unit.unit_type, "province": province})

                for province in sorted(country_units, reverse=True):
                    if len(removed_provinces) >= required_removals:
                        break
                    if province in removed_provinces:
                        continue
                    unit = final_state.units_by_province.pop(province, None)
                    if unit:
                        removed_provinces.add(province)
                        removals.append({"country": country, "unit_type": unit.unit_type, "province": province})

                missing = required_removals - len(removed_provinces)
                if missing:
                    unfilled_removals[country] = missing

        final_state.season = "Winter"
        return WinterResolution(
            state=final_state,
            builds=builds,
            removals=removals,
            unfilled_builds=unfilled_builds,
            unfilled_removals=unfilled_removals,
        )

    def generate_turn_intents(self, simulation_state, country_states):
        """Select baseline intents, then coordinate holds into supporting orders."""
        intents = [
            self.choose_unit_intent(simulation_state, country_states[unit.country], unit)
            for unit in simulation_state.units_by_province.values()
            if unit.country in country_states
        ]
        intents_by_origin = {intent["from"]: intent for intent in intents}
        for province, unit in simulation_state.units_by_province.items():
            if intents_by_origin.get(province, {}).get("action") != "HOLD":
                continue
            policy = self._policy_weights(country_states[unit.country])
            support_options = []
            for supported_origin, supported_intent in intents_by_origin.items():
                supported_unit = simulation_state.units_by_province[supported_origin]
                if supported_unit.country != unit.country or supported_origin == province:
                    continue
                target = supported_intent.get("to") if supported_intent.get("action") == "MOVE" else supported_origin
                if target not in get_legal_neighbors_for_unit(province, unit.unit_type):
                    continue
                weight = policy["defend_center"] if target == supported_origin else policy["attack_enemy"]
                support_options.append({
                    "action": "SUPPORT",
                    "from": province,
                    "support_from": supported_origin,
                    "support_to": target,
                    "weight": weight,
                })
            if support_options:
                hold_weight = max(0.05, intents_by_origin[province].get("weight", policy["hold"]))
                options = [{**intents_by_origin[province], "weight": hold_weight}] + support_options
                total_weight = sum(option["weight"] for option in options)
                roll = self.random.uniform(0, total_weight)
                for option in options:
                    roll -= option["weight"]
                    if roll <= 0:
                        intents_by_origin[province] = option
                        break
        return list(intents_by_origin.values())

    def capture_fall_supply_centers(self, simulation_state):
        """Apply Fall supply-center ownership changes and return whether any changed."""
        final_state = simulation_state.copy()
        changed = False
        for province in STARTING_SUPPLY_CENTERS:
            unit = final_state.units_by_province.get(province)
            if unit and final_state.sc_owners.get(province) != unit.country:
                final_state.sc_owners[province] = unit.country
                changed = True
        return final_state, changed

    def _leading_country(self, simulation_state):
        counts = {}
        for owner in simulation_state.sc_owners.values():
            if owner not in (None, "", "Neutral"):
                counts[owner] = counts.get(owner, 0) + 1
        if not counts:
            return None
        return max(counts, key=lambda country: (counts[country], country))

    def simulate_trial(self, game_state, horizon_years=3, stalemate_seasons=4):
        """Run a bounded strategic board simulation through movement and Winter phases."""
        state = self.create_simulation_state(game_state)
        country_states = game_state.countries
        movement_limit = max(1, horizon_years * 2)
        movement_seasons = 0
        stagnant_seasons = 0

        if state.season == "Winter":
            state = self.resolve_winter(state).state
            state.season = "Spring"
            state.year += 1

        while movement_seasons < movement_limit:
            intents = self.generate_turn_intents(state, country_states)
            intents_by_origin = {intent["from"]: intent for intent in intents}
            movement_before = state
            resolution = self.resolve_movement(state, intents)
            retreat_resolution = self.resolve_retreats(resolution, country_states)
            state = retreat_resolution.state
            movement_seasons += 1

            aggressive_success = any(
                movement_before.units_by_province[origin].country
                != movement_before.units_by_province.get(
                    intents_by_origin[origin].get("to"),
                    SimulatedUnit("", "", ""),
                ).country
                or movement_before.sc_owners.get(intents_by_origin[origin].get("to"))
                not in (None, movement_before.units_by_province[origin].country)
                for origin in resolution.successful_moves
            )

            ownership_changed = False
            if state.season == "Fall":
                state, ownership_changed = self.capture_fall_supply_centers(state)
                winner = self._leading_country(state)
                if winner and sum(owner == winner for owner in state.sc_owners.values()) >= 18:
                    return SimulationResult(state, winner, "solo", movement_seasons, stagnant_seasons)
                state = self.resolve_winter(state).state
                state.season = "Spring"
                state.year += 1
            else:
                state.season = "Fall"

            if aggressive_success or ownership_changed:
                stagnant_seasons = 0
            else:
                stagnant_seasons += 1
                if stagnant_seasons >= stalemate_seasons:
                    return SimulationResult(state, None, "stalemate", movement_seasons, stagnant_seasons)

        return SimulationResult(
            state,
            self._leading_country(state),
            "horizon",
            movement_seasons,
            stagnant_seasons,
        )

    def _score_country_state(self, state):
        return (
            state.sc * PREDICTIVE_WEIGHTS["sc"]
            + state.units * PREDICTIVE_WEIGHTS["units"]
            + getattr(state, "strategic_position", 0) * PREDICTIVE_WEIGHTS["strategic_position"]
            + getattr(state, "operational_efficiency", 0) * PREDICTIVE_WEIGHTS["operational_efficiency"]
            + getattr(state, "center_conversion_rate", 0) * PREDICTIVE_WEIGHTS["center_conversion_rate"]
            + getattr(state, "threat_coverage_rate", 0) * PREDICTIVE_WEIGHTS["threat_coverage_rate"]
            + getattr(state, "front_concentration", 0) * PREDICTIVE_WEIGHTS["front_concentration"]
            + getattr(state, "allied_support_rate", 0) * PREDICTIVE_WEIGHTS["allied_support_rate"]
            + state.cgi * PREDICTIVE_WEIGHTS["cgi"]
            + state.ema_momentum * PREDICTIVE_WEIGHTS["ema_momentum"]
            + state.momentum * PREDICTIVE_WEIGHTS["momentum"]
            + getattr(state, "unit_growth", 0) * PREDICTIVE_WEIGHTS["unit_growth"]
            + state.isolation * PREDICTIVE_WEIGHTS["isolation"]
            + state.encirclement * PREDICTIVE_WEIGHTS["encirclement"]
        )

    def simulate_trials(self, game_state, iterations=100, horizon_years=3, stalemate_seasons=4):
        """Aggregate strategic board trials into explainable forecast statistics."""
        countries = [country for country in game_state.countries if country]
        if not countries or iterations <= 0:
            return {"countries": {}, "draw_probability": 0.0, "terminal_reasons": {}}

        solo_wins = {country: 0 for country in countries}
        horizon_leads = {country: 0 for country in countries}
        expected_scs = {country: 0 for country in countries}
        expected_units = {country: 0 for country in countries}
        rank_totals = {country: 0 for country in countries}
        elimination_counts = {country: 0 for country in countries}
        home_center_loss_counts = {country: 0 for country in countries}
        terminal_reasons = {"solo": 0, "stalemate": 0, "horizon": 0}

        for _ in range(iterations):
            result = self.simulate_trial(game_state, horizon_years, stalemate_seasons)
            terminal_reasons[result.terminal_reason] = terminal_reasons.get(result.terminal_reason, 0) + 1
            if result.terminal_reason == "solo" and result.winner in solo_wins:
                solo_wins[result.winner] += 1
            elif result.terminal_reason == "horizon" and result.winner in horizon_leads:
                horizon_leads[result.winner] += 1

            for country in countries:
                expected_scs[country] += sum(
                    owner == country for owner in result.state.sc_owners.values()
                )
                expected_units[country] += sum(
                    unit.country == country
                    for unit in result.state.units_by_province.values()
                )
                home_centers = {
                    province for province, owner in STARTING_SUPPLY_CENTERS.items()
                    if owner == country
                }
                if home_centers and any(
                    result.state.sc_owners.get(province) != country
                    for province in home_centers
                ):
                    home_center_loss_counts[country] += 1

            ranked_countries = sorted(
                countries,
                key=lambda country: (
                    -sum(owner == country for owner in result.state.sc_owners.values()),
                    -sum(unit.country == country for unit in result.state.units_by_province.values()),
                    country,
                ),
            )
            for rank, country in enumerate(ranked_countries, start=1):
                rank_totals[country] += rank
                if (
                    not any(owner == country for owner in result.state.sc_owners.values())
                    or not any(unit.country == country for unit in result.state.units_by_province.values())
                ):
                    elimination_counts[country] += 1

        return {
            "countries": {
                country: {
                    "win_probability": (solo_wins[country] + horizon_leads[country]) / iterations,
                    "solo_probability": solo_wins[country] / iterations,
                    "horizon_lead_probability": horizon_leads[country] / iterations,
                    "expected_scs": expected_scs[country] / iterations,
                    "expected_units": expected_units[country] / iterations,
                    "expected_rank": rank_totals[country] / iterations,
                    "elimination_probability": elimination_counts[country] / iterations,
                    "home_center_loss_probability": home_center_loss_counts[country] / iterations,
                }
                for country in countries
            },
            "draw_probability": terminal_reasons["stalemate"] / iterations,
            "terminal_reasons": terminal_reasons,
        }

    def simulate(self, game_state, iterations=100):
        countries = [country for country in game_state.countries if country]
        if not countries:
            return {}

        if game_state.board.units_by_province:
            details = self.simulate_trials(game_state, iterations=iterations)
            return {
                country: details["countries"][country]["win_probability"]
                for country in countries
            }

        base_scores = {
            country: self._score_country_state(game_state.countries[country])
            for country in countries
        }

        win_counts = {country: 0 for country in countries}
        for _ in range(iterations):
            simulated_scores = {
                country: base_scores[country] + self.random.gauss(0.0, 1.8)
                for country in countries
            }
            winner = max(simulated_scores, key=lambda country: float(simulated_scores[country]))
            win_counts[winner] += 1

        total_wins = sum(win_counts.values())
        if total_wins <= 0:
            return {country: 0.0 for country in countries}

        return {
            country: win_counts[country] / total_wins
            for country in countries
        }
