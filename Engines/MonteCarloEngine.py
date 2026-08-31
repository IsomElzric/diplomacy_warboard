import random


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


class MonteCarloEngine:
    """
    Win-probability forecast based on the full strategic state of each country.
    It incorporates center count, unit posture, momentum, EMA growth, CGI, and
    operational exposure so the predicted winner reflects the broader game state.
    """

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

    def simulate(self, game_state, iterations=100):
        countries = [country for country in game_state.countries if country]
        if not countries:
            return {}

        base_scores = {
            country: self._score_country_state(game_state.countries[country])
            for country in countries
        }

        win_counts = {country: 0 for country in countries}
        for _ in range(iterations):
            simulated_scores = {
                country: base_scores[country] + random.gauss(0.0, 1.8)
                for country in countries
            }
            winner = max(simulated_scores, key=simulated_scores.get)
            win_counts[winner] += 1

        total_wins = sum(win_counts.values())
        if total_wins <= 0:
            return {country: 0.0 for country in countries}

        return {
            country: win_counts[country] / total_wins
            for country in countries
        }
