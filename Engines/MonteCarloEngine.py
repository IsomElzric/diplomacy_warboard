import random


class MonteCarloEngine:
    """
    Win-probability forecast based on the full strategic state of each country.
    It incorporates center count, unit posture, momentum, EMA growth, CGI, and
    operational exposure so the predicted winner reflects the broader game state.
    """

    def _score_country_state(self, state):
        return (
            (state.sc * 2.0) +
            (state.units * 0.9) +
            (state.cgi * 7.0) +
            (state.momentum * 2.2) +
            (state.ema_momentum * 1.8) +
            (getattr(state, "growth_rate", 0) * 5.0) +
            (getattr(state, "unit_growth", 0) * 1.5) +
            (state.active_fronts * 0.9) +
            (getattr(state, "holds", 0) * 0.8) +
            (getattr(state, "supports", 0) * 0.9) +
            (getattr(state, "build_effeciency", 0) * 2.5)
            - (state.isolation * 3.0)
            - (state.encirclement * 3.5)
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
