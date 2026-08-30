# Engines/SCOwnershipEngine.py
from Data.supply_centers import SUPPLY_CENTERS

class SCOwnershipEngine:
    def compute(self, final_positions, season):
        ownership = {"Neutral": set()}

        # Start from canonical ownership
        for province, owner in SUPPLY_CENTERS.items():
            if owner is None or owner == "":
                ownership["Neutral"].add(province)
            else:
                ownership.setdefault(owner, set()).add(province)

        # Only Fall changes ownership
        if season != "Fall":
            return ownership

        # Apply ownership changes
        for province, country in final_positions.items():
            if province in SUPPLY_CENTERS:
                prev_owner = SUPPLY_CENTERS[province]

                if prev_owner in (None, "", "Neutral"):
                    ownership.setdefault("Neutral", set()).discard(province)
                elif prev_owner in ownership:
                    ownership[prev_owner].discard(province)

                if country in (None, "", "Neutral"):
                    ownership.setdefault("Neutral", set()).add(province)
                else:
                    ownership.setdefault(country, set()).add(province)

                SUPPLY_CENTERS[province] = country or "Neutral"

        return ownership
