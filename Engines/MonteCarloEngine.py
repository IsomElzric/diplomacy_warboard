import random


class MonteCarloEngine:
    """
    Lightweight forecast engine for country win probability estimation based on current state.
    It is intentionally simple and designed to be expanded with richer geography and unit data.
    """

    def simulate(self, game_state, iterations=100):
        results = {}

        for country, state in game_state.countries.items():
            if not country:
                continue

            score = (
                state.cgi +
                (state.momentum * 0.4) +
                (state.ema_momentum * 0.2) +
                (state.active_fronts * 0.15) -
                (state.isolation * 0.2) -
                (state.encirclement * 0.2)
            )

            wins = 0
            for _ in range(iterations):
                roll = random.random()
                drift = random.uniform(-0.6, 0.6)
                projected = score + drift
                if projected > 0:
                    wins += 1

            results[country] = wins / iterations if iterations else 0

        total = sum(results.values())
        if total > 0:
            normalized = {country: value / total for country, value in results.items()}
            return normalized

        return {country: 0.0 for country in results}
