# IO/OrderParser.py
# IO/OrderParser.py
import re

VALID_COUNTRIES = {
    "Austria","England","France","Germany","Italy","Russia","Turkey"
}

class OrderParser:
    COUNTRY_HEADER = re.compile(r"^[A-Z][a-z]+$")
    RETREAT_HEADER = re.compile(r"^Retreats$", re.IGNORECASE)
    COUNTRY_RETREAT_HEADER = re.compile(r"^[A-Z][a-z]+\s+Retreats$", re.IGNORECASE)

    ORDER_LINE = re.compile(
        r"^(?P<unit>[AF])\s+"
        r"(?P<from>[A-Za-z/]+)"
        r"(?:\s*-\s*(?P<to>[A-Za-z/]+))?"
        r"\s+(?P<result>SUCCEEDS|FAILS)"
        r"(?:\s*\((?P<reason>.+)\))?"
        r"$"
    )

    WINTER_ORDER_LINE = re.compile(
        r"^(?P<unit>[AF])\s+"
        r"(?P<from>[A-Za-z/]+)\s+"
        r"(?P<action>Build|Disband)\s+"
        r"(?P<result>SUCCEEDS|FAILS)"
        r"(?:\s*\((?P<reason>.+)\))?"
        r"$"
    )

    DISLODGED_PATTERN = re.compile(
        r"DISLODGED(?:\s+by\s+(?P<attacker>.+))?",
        re.IGNORECASE
    )

    def parse(self, text):
        lines = [line.strip() for line in text.splitlines() if line.strip()]

        movement = {}
        retreats = {}

        current_country = None
        retreat_mode = False

        for line in lines:

            # Switch into retreat mode
            if self.RETREAT_HEADER.match(line):
                retreat_mode = True
                current_country = None
                continue

            # Country Retreat header
            if self.COUNTRY_RETREAT_HEADER.match(line):
                retreat_mode = True
                current_country = line.split()[0]
                retreats[current_country] = []
                continue

            # Country header
            if self.COUNTRY_HEADER.match(line):
                if line not in VALID_COUNTRIES:
                    continue
                current_country = line
                if retreat_mode:
                    retreats.setdefault(current_country, [])
                else:
                    movement.setdefault(current_country, [])
                continue

            # Order line
            m = self.ORDER_LINE.match(line)
            if m and current_country:
                entry = m.groupdict()
                entry["action"] = "MOVE" if entry["to"] else "HOLD"
                entry["success"] = entry["result"] == "SUCCEEDS"

                # Dislodgement detection
                entry["dislodged"] = False
                entry["dislodged_by"] = None
                if entry["reason"]:
                    dm = self.DISLODGED_PATTERN.search(entry["reason"])
                    if dm:
                        entry["dislodged"] = True
                        entry["dislodged_by"] = dm.group("attacker")

                # Store
                if retreat_mode:
                    retreats[current_country].append(entry)
                else:
                    movement[current_country].append(entry)
                continue

            winter = self.WINTER_ORDER_LINE.match(line)
            if winter and current_country:
                entry = winter.groupdict()
                entry["action"] = entry["action"].upper()
                entry["to"] = None
                entry["success"] = entry["result"] == "SUCCEEDS"
                entry["dislodged"] = False
                entry["dislodged_by"] = None

                if retreat_mode:
                    retreats[current_country].append(entry)
                else:
                    movement[current_country].append(entry)

        return movement, retreats
