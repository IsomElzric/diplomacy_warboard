# States/BoardState.py
from States.UnitState import UnitState


class BoardState:
    def __init__(self, year, season):
        self.year = year
        self.season = season
        self.units_by_province = {}   # province -> UnitState
        self.sc_owners = {}           # province -> owner

    def add_unit(self, unit_state):
        self.units_by_province[unit_state.province] = unit_state

    def remove_unit(self, province):
        self.units_by_province.pop(province, None)

    def copy(self, year=None, season=None):
        cloned = BoardState(year if year is not None else self.year, season if season is not None else self.season)
        cloned.sc_owners = self.sc_owners.copy()
        for province, unit in self.units_by_province.items():
            cloned.add_unit(UnitState(
                country=unit.country,
                unit_type=unit.unit_type,
                province=province,
                order=dict(unit.order or {}),
            ))
        return cloned

    def get_units_for_country(self, country):
        return [u for u in self.units_by_province.values() if u.country == country]

    def get_owned_scs_for_country(self, country):
        return [p for p, owner in self.sc_owners.items() if owner == country]
    