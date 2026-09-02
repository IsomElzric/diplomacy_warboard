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
        r"(?P<from>[A-Za-z/]+)\s*"
        r"(?P<rest>.*)\s+"
        r"(?P<result>SUCCEEDS|FAILS)"
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

    INLINE_RETREAT_LINE = re.compile(
        r"^(?P<unit>[AF])\s+"
        r"(?P<from>[A-Za-z/]+)\s+Retreat\s+to\s+"
        r"(?P<to>[A-Za-z/]+)\s+"
        r"(?P<result>SUCCEEDS|FAILS)"
        r"(?:\s*\((?P<reason>.+)\))?"
        r"$",
        re.IGNORECASE,
    )

    BARE_RETREAT_LINE = re.compile(
        r"^Retreat\s+to\s+(?P<to>[A-Za-z/]+)\s+"
        r"(?P<result>SUCCEEDS|FAILS)"
        r"(?:\s*\((?P<reason>.+)\))?$",
        re.IGNORECASE,
    )

    BARE_DISBAND_LINE = re.compile(
        r"^Disband\s+(?P<result>SUCCEEDS|FAILS)"
        r"(?:\s*\((?P<reason>.+)\))?$",
        re.IGNORECASE,
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
        previous_order = None

        for line in lines:

            # Switch into retreat mode
            if self.RETREAT_HEADER.match(line):
                retreat_mode = True
                current_country = None
                previous_order = None
                continue

            # Country Retreat header
            if self.COUNTRY_RETREAT_HEADER.match(line):
                retreat_mode = True
                current_country = line.split()[0]
                retreats[current_country] = []
                previous_order = None
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
                previous_order = None
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
                continue

            inline_retreat = self.INLINE_RETREAT_LINE.match(line)
            if inline_retreat and current_country:
                entry = inline_retreat.groupdict()
                entry["action"] = "RETREAT"
                entry["success"] = entry["result"] == "SUCCEEDS"
                entry["dislodged"] = True
                entry["dislodged_by"] = None
                retreats.setdefault(current_country, []).append(entry)
                continue

            bare_retreat = self.BARE_RETREAT_LINE.match(line)
            if bare_retreat and current_country and previous_order:
                entry = bare_retreat.groupdict()
                entry["unit"] = previous_order["unit"]
                entry["from"] = previous_order["from"]
                entry["action"] = "RETREAT"
                entry["success"] = entry["result"] == "SUCCEEDS"
                entry["dislodged"] = True
                entry["dislodged_by"] = None
                retreats.setdefault(current_country, []).append(entry)
                continue

            bare_disband = self.BARE_DISBAND_LINE.match(line)
            if bare_disband and current_country and previous_order:
                entry = bare_disband.groupdict()
                entry["unit"] = previous_order["unit"]
                entry["from"] = previous_order["from"]
                entry["to"] = None
                entry["action"] = "DISBAND"
                entry["success"] = entry["result"] == "SUCCEEDS"
                entry["dislodged"] = True
                entry["dislodged_by"] = None
                retreats.setdefault(current_country, []).append(entry)
                continue

            # Order line
            m = self.ORDER_LINE.match(line)
            if m and current_country:
                rest = (m.group("rest") or "").strip()
                entry = m.groupdict()
                entry["to"] = None

                if rest == "H":
                    entry["action"] = "HOLD"
                elif rest.startswith("S "):
                    entry["action"] = "SUPPORT"
                    entry["to"] = rest[2:].strip()
                elif rest.startswith("C "):
                    entry["action"] = "CONVOY"
                    entry["to"] = rest[2:].strip()
                elif rest.startswith("-"):
                    entry["action"] = "MOVE"
                    entry["to"] = rest[1:].strip()
                elif rest:
                    entry["action"] = "MOVE"
                    entry["to"] = rest.strip()
                else:
                    entry["action"] = "HOLD"

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
                    previous_order = entry
                continue

        return movement, retreats
