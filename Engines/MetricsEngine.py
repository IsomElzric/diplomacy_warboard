CGI_GROWTH_RATE_WEIGHT = 0.6
CGI_MOMENTUM_WEIGHT = 0.25  
CGI_EMA_MOMENTUM_WEIGHT = 0.15
TOTAL_SUPPLY_CENTERS = 34

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

            # Raw board-state inputs normalized to comparable country features.
            current.order_success_rate = (
                current.successful_orders / current.order_count
                if current.order_count > 0 else 0.0
            )
            current.hold_rate = current.holds / current.order_count if current.order_count > 0 else 0.0
            current.support_rate = current.supports / current.order_count if current.order_count > 0 else 0.0
            defensive_orders = current.holds + current.support_holds
            offensive_orders = current.moves + current.support_attacks
            committed_orders = defensive_orders + offensive_orders
            current.unit_utilization = min(1.0, committed_orders / current.units) if current.units > 0 else 0.0
            current.defensive_posture = defensive_orders / current.order_count if current.order_count > 0 else 0.0
            current.offensive_posture = offensive_orders / current.order_count if current.order_count > 0 else 0.0
            current.posture_balance = current.offensive_posture - current.defensive_posture
            if current.order_count == 0:
                current.posture = "Inactive"
            elif current.posture_balance >= 0.5:
                current.posture = "Aggressive"
            elif current.posture_balance >= 0.15:
                current.posture = "Mixed-Offense"
            elif current.posture_balance <= -0.5:
                current.posture = "Defensive"
            elif current.posture_balance <= -0.15:
                current.posture = "Mixed-Defense"
            else:
                current.posture = "Balanced"
            if current.detailed_order_outcomes:
                defensive_success_rate = (
                    current.successful_defensive_orders / defensive_orders
                    if defensive_orders > 0 else 0.0
                )
                offensive_success_rate = (
                    current.successful_offensive_orders / offensive_orders
                    if offensive_orders > 0 else 0.0
                )
            else:
                defensive_success_rate = current.order_success_rate if defensive_orders > 0 else 0.0
                offensive_success_rate = current.order_success_rate if offensive_orders > 0 else 0.0
            if committed_orders:
                current.unit_efficiency = current.unit_utilization * (
                    (defensive_success_rate * defensive_orders + offensive_success_rate * offensive_orders)
                    / committed_orders
                )
            else:
                current.unit_efficiency = 0.0
            current.center_conversion_rate = (
                current.successful_center_attacks / current.center_targets
                if current.center_targets > 0 else 0.0
            )
            current.threat_coverage_rate = (
                current.defended_threatened_centers / current.threatened_centers
                if current.threatened_centers > 0 else 0.0
            )
            current.allied_support_rate = (
                current.allied_supports / current.supports
                if current.supports > 0 else 0.0
            )
            current.unit_sc_ratio = current.units / current.sc if current.sc > 0 else 0.0
            current.board_control = current.sc / TOTAL_SUPPLY_CENTERS
            current.operational_efficiency = (
                current.unit_efficiency * (1.0 + current.support_rate * 0.25)
            )
            current.strategic_position = (
                current.board_control * min(1.0, current.unit_sc_ratio)
                * (1.0 - min(1.0, current.isolation))
                * (1.0 - min(1.0, current.encirclement))
            )

            # SC Gain
            current.sc_gain = (current.sc - prev.sc) if prev else 0

            # Unit Growth
            current.unit_growth = (current.units - prev.units) if prev else 0

            # Build Efficiency (simple calculation)
            current.build_efficiency = (current.builds / current.sc if current.sc > 0 else 0)
            current.build_effeciency = current.build_efficiency

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