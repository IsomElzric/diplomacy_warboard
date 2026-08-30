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

        # Derived Metrics
        self.sc_gains = 0
        self.unit_growth = 0
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

    def __repr__(self):
        return f"CountryState {self.country} {self.year} {self.season}: Supply Centers={self.sc}, Units={self.units}"