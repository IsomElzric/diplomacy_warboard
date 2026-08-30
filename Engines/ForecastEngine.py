SCORE_MOMENTUM_WEIGHT = 0.4
SCORE_EMA_MOMENTUM_WEIGHT = 0.2

class ForecastEngine:
    """
    Produces simple forecasts based on current metrics.
    """

    def forecast(self, game_state):
        results = {}

        for country, state in game_state.countries.items():
            if not country:
                continue

            projected_scs = state.sc + state.momentum + state.ema_momentum

            # Forecast score (normalized)
            score = (
                state.cgi +
                (state.momentum * SCORE_MOMENTUM_WEIGHT) +
                (state.ema_momentum * SCORE_EMA_MOMENTUM_WEIGHT)
            )

            results[country] = {
                'sc': state.sc,
                'momentum': state.momentum,
                'ema': state.ema_momentum,
                'cgi': state.cgi,
                'projected_scs': projected_scs,
                'forecast_score': score
            }

        # Compute win outlook (relative score)
        total_score = sum([res['forecast_score'] for res in results.values()])
        for country, country_data in results.items():
            country_data['win_outlook'] = (
                country_data['forecast_score'] / total_score if total_score > 0 else 0
            )

        return results