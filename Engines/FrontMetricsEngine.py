from Data.location_data import compute_board_tactical_metrics


class FrontMetricsEngine:
    """
    Derive geography-aware country metrics from current province and unit state.
    """

    def compute(self, country, units_by_province, sc_owners):
        return compute_board_tactical_metrics(country, units_by_province, sc_owners)
