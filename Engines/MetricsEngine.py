CGI_GROWTH_RATE_WEIGHT = 0.6
CGI_MOMENTUM_WEIGHT = 0.25  
CGI_EMA_MOMENTUM_WEIGHT = 0.15

class MetricsEngine:
    """
    Computes derived metrics for country histories without mixing countries together.
    """

    def _compute_metrics_for_history(self, history):
        """
        history: list of CountryState objects in chronological order for a single country.
        """

        for i in range(len(history)):
            current = history[i]
            prev = history[i - 1] if i > 0 else None

            # SC Gain
            current.sc_gain = (current.sc - prev.sc) if prev else 0

            # Unit Growth
            current.unit_growth = (current.units - prev.units) if prev else 0

            # Build Efficiency (simple calculation)
            current.build_efficiency = (current.builds / current.sc if current.sc > 0 else 0)

            # Growth Rate (normalized SC change)
            current.growth_rate = (current.sc_gain / current.sc if current.sc > 0 else 0)

            # Momentum updates only in fall. During the rest of the season cycle,
            # the last validated fall value should persist until the next fall refresh.
            if prev and current.season != "Fall":
                current.momentum = prev.momentum
                current.ema_momentum = prev.ema_momentum
                current.cgi = prev.cgi
                continue

            # Momentum (simple version: SC gain + unit growth)
            current.momentum = current.sc_gain + current.unit_growth

            # EMA Momentum (alpha = 0.5 for now)
            if prev:
                alpha = 0.5
                current.ema_momentum = (alpha * current.momentum) + ((1 - alpha) * prev.ema_momentum)
            else:
                current.ema_momentum = current.momentum

            # Composite Growth Index (CGI)
            current.cgi = (
                current.growth_rate * CGI_GROWTH_RATE_WEIGHT +
                current.momentum * CGI_MOMENTUM_WEIGHT +
                current.ema_momentum * CGI_EMA_MOMENTUM_WEIGHT
            )

    def compute_metrics_by_country(self, country_histories):
        """
        country_histories: dict[str, list[CountryState]] or list[CountryState]
        Processes each country's history independently so order data for one country
        never leaks into the metrics of another country.
        """

        if isinstance(country_histories, dict):
            for history in country_histories.values():
                if history:
                    self._compute_metrics_for_history(history)
            return

        grouped = {}
        for state in country_histories:
            grouped.setdefault(state.country, []).append(state)

        for history in grouped.values():
            self._compute_metrics_for_history(history)

    def compute_metrics(self, history):
        """
        Backwards-compatible wrapper for a mixed or country-grouped list of states.
        """
        self.compute_metrics_by_country(history)