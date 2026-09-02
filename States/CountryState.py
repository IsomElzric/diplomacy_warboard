class CountryState:
    """
    Represents the state of a single country for a single season.
    """

    def __init__(self, country, year=1901, season="Spring", sc=3, units=3, builds=0):
        self.country = country
        self.year = year
        self.season = season

        # Core Values
        self.sc = sc
        self.units = units
        self.builds = builds

        # Board-derived inputs
        self.order_count = 0
        self.successful_orders = 0
        self.order_success_rate = 0.0
        self.moves = 0
        self.support_holds = 0
        self.support_attacks = 0
        self.successful_defensive_orders = 0
        self.successful_offensive_orders = 0
        self.detailed_order_outcomes = False
        self.unit_utilization = 0.0
        self.defensive_posture = 0.0
        self.offensive_posture = 0.0
        self.posture_balance = 0.0
        self.posture = "Inactive"
        self.unit_efficiency = 0.0
        self.center_targets = 0
        self.successful_center_attacks = 0
        self.center_conversion_rate = 0.0
        self.threatened_centers = 0
        self.defended_threatened_centers = 0
        self.threat_coverage_rate = 0.0
        self.front_concentration = 0.0
        self.allied_supports = 0
        self.allied_support_rate = 0.0
        self.unit_sc_ratio = 0.0
        self.board_control = 0.0
        self.solo_distance = 18
        self.winter_adjustment = 0
        self.home_centers = 0
        self.home_centers_lost = 0
        self.home_centers_enemy_occupied = 0
        self.frontline_units = 0
        self.hostile_adjacencies = 0
        self.exposed_centers = 0
        self.center_defense_rate = 1.0
        self.successful_moves = 0
        self.failed_moves = 0
        self.failed_orders = 0
        self.retreats = 0
        self.disbands = 0

        # Derived Metrics
        self.sc_gains = 0
        self.unit_growth = 0
        self.build_efficiency = 0.0
        self.build_effeciency = 0
        self.momentum = 0
        self.ema_momentum = 0
        self.growth_rate = 0
        self.cgi = 0

        # Advanced Inputs
        self.holds = 0
        self.supports = 0
        self.active_fronts = 0

        # Advanced Derived Metrics
        self.hold_rate = 0
        self.support_rate = 0
        self.isolation = 0
        self.encirclement = 0
        self.operational_efficiency = 0.0
        self.strategic_position = 0.0

    def __repr__(self):
        return f"CountryState {self.country} {self.year} {self.season}: Supply Centers={self.sc}, Units={self.units}"