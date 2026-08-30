# States/BoardState.py
class BoardState:
    def __init__(self, year, season):
        self.year = year
        self.season = season
        self.units_by_province = {}   # province -> UnitState
        self.sc_owners = {}           # province -> owner

    def add_unit(self, unit_state):
        self.units_by_province[unit_state.province] = unit_state

    def get_units_for_country(self, country):
        return [u for u in self.units_by_province.values() if u.country == country]

    def get_owned_scs_for_country(self, country):
        return [p for p, owner in self.sc_owners.items() if owner == country]
    