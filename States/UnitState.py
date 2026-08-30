# States/UnitState.py
class UnitState:
    def __init__(self, country, unit_type, province, order=None):
        self.country = country
        self.unit_type = unit_type  # "A" or "F"
        self.province = province
        self.order = order or {}    # parsed order dict
    