class GameState:
    """
    Represents teh entire board for a single season.
    Holds CountryState objects for each power.
    """

    def __init__(self, year, season):
        self.year = year
        self.season = season
        self.countries = {}

    def add_country_state(self, country_state):
        self.countries[country_state.country] = country_state

    def get_country(self, name):
        return self.countries.get(name, None)

    def __repr__(self):
        return f"GameState {self.year} {self.season}: {list(self.countries.keys())}"