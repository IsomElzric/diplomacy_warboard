from Data.location_data import compute_country_geography_metrics


class FrontMetricsEngine:
    """
    Derive geography-aware country metrics from current province and unit state.
    """

    def compute(self, country, owned_provinces, hostile_countries=None):
        return compute_country_geography_metrics(country, owned_provinces, hostile_countries or [])
