# Province-level metadata for geography-aware metrics.
# Each province stores its relationship to fronts, borders, and ownership context.

PROVINCE_DATA = {
    # England
    "Lon": {"front_id": "NorthSea", "neighbors": ["NTH", "ENG", "Wal"], "coastal": True},
    "Edi": {"front_id": "NorthSea", "neighbors": ["NTH", "Cly", "Stp"], "coastal": True},
    "Lvp": {"front_id": "EnglishChannel", "neighbors": ["ENG", "Wal", "Yor", "IRI"], "coastal": True},
    "Yor": {"front_id": "EnglishChannel", "neighbors": ["Lvp", "Wal", "NTH"], "coastal": False},
    "Wal": {"front_id": "EnglishChannel", "neighbors": ["Lvp", "Yor", "ENG", "Lon"], "coastal": False},
    "Cly": {"front_id": "NorthSea", "neighbors": ["Edi", "NTH"], "coastal": True},

    # France
    "Par": {"front_id": "WesternFront", "neighbors": ["Bur", "Pic", "Gas"], "coastal": False},
    "Mar": {"front_id": "WesternFront", "neighbors": ["Spa", "Pie", "Bur", "Gas"], "coastal": True},
    "Bre": {"front_id": "WesternFront", "neighbors": ["Gas", "MAO", "Pic"], "coastal": True},
    "Spa": {"front_id": "WesternFront", "neighbors": ["Mar", "Por", "Gas", "Mid"], "coastal": True},
    "Por": {"front_id": "WesternFront", "neighbors": ["Spa", "Mid"], "coastal": True},
    "Bur": {"front_id": "WesternFront", "neighbors": ["Par", "Mun", "Mar", "Gas"], "coastal": False},

    # Germany
    "Ber": {"front_id": "CentralFront", "neighbors": ["Kie", "PrU", "War", "Sil"], "coastal": False},
    "Mun": {"front_id": "CentralFront", "neighbors": ["Bur", "Ber", "Ruh", "Vie"], "coastal": False},
    "Kie": {"front_id": "CentralFront", "neighbors": ["Ber", "Hol", "Den", "Hel"], "coastal": True},
    "Ruh": {"front_id": "CentralFront", "neighbors": ["Mun", "Kie", "Bur"], "coastal": False},

    # Italy
    "Rom": {"front_id": "SouthernFront", "neighbors": ["Nap", "Ven", "Tus"], "coastal": True},
    "Ven": {"front_id": "SouthernFront", "neighbors": ["Rom", "Tri", "Apu", "Pie"], "coastal": False},
    "Nap": {"front_id": "SouthernFront", "neighbors": ["Rom", "Apu", "Ion"], "coastal": True},
    "Tus": {"front_id": "SouthernFront", "neighbors": ["Rom", "Pie", "Lyo"], "coastal": True},

    # Austria
    "Vie": {"front_id": "CentralFront", "neighbors": ["Bud", "Tri", "Mun", "Gal"], "coastal": False},
    "Bud": {"front_id": "CentralFront", "neighbors": ["Vie", "Tri", "Gal", "Ser"], "coastal": False},
    "Tri": {"front_id": "CentralFront", "neighbors": ["Vie", "Bud", "Ven", "Adr"], "coastal": True},
    "Gal": {"front_id": "CentralFront", "neighbors": ["War", "Vie", "Bud", "Rum"], "coastal": False},

    # Turkey
    "Smy": {"front_id": "EasternFront", "neighbors": ["Con", "Ank", "Arm"], "coastal": True},
    "Ank": {"front_id": "EasternFront", "neighbors": ["Con", "Smy", "Arm", "Bla"], "coastal": True},
    "Con": {"front_id": "EasternFront", "neighbors": ["Smy", "Ank", "Bul", "Bla"], "coastal": True},
    "Bul": {"front_id": "EasternFront", "neighbors": ["Con", "Ser", "Rum", "Gre"], "coastal": True},

    # Russia
    "War": {"front_id": "EasternFront", "neighbors": ["Mos", "Ukr", "Gal", "PrU"], "coastal": False},
    "Mos": {"front_id": "EasternFront", "neighbors": ["War", "Stp", "Sev", "Ukr"], "coastal": False},
    "Stp": {"front_id": "NorthernFront", "neighbors": ["Mos", "Fin", "Nwy", "Bot"], "coastal": True},
    "Sev": {"front_id": "EasternFront", "neighbors": ["Mos", "Ukr", "Rum", "Bla"], "coastal": True},
    "Ukr": {"front_id": "EasternFront", "neighbors": ["War", "Mos", "Sev", "Rum"], "coastal": False},

    # Neutral / contested
    "Bel": {"front_id": "WesternFront", "neighbors": ["Hol", "Pic", "Bur", "Eng"], "coastal": True},
    "Hol": {"front_id": "CentralFront", "neighbors": ["Bel", "Kie", "Hel"], "coastal": True},
    "Den": {"front_id": "NorthernFront", "neighbors": ["Kie", "Ska", "Nwy", "Hel"], "coastal": True},
    "Nwy": {"front_id": "NorthernFront", "neighbors": ["Stp", "Swe", "NTH", "Fin"], "coastal": True},
    "Swe": {"front_id": "NorthernFront", "neighbors": ["Nwy", "Fin", "BOT", "Bal"], "coastal": True},
    "Ser": {"front_id": "CentralFront", "neighbors": ["Bul", "Tri", "Bud", "Gre"], "coastal": False},
    "Gre": {"front_id": "SouthernFront", "neighbors": ["Bul", "Ser", "Aeg", "Ion"], "coastal": True},
    "Rum": {"front_id": "EasternFront", "neighbors": ["Bul", "Ukr", "Bud", "Sev"], "coastal": True},
    "Tun": {"front_id": "SouthernFront", "neighbors": ["TYS", "Ion", "Mid"], "coastal": True},
    "Bul/EC": {"front_id": "EasternFront", "neighbors": ["Con", "Rum", "Gre", "Bul/SC"], "coastal": True},
    "Bul/SC": {"front_id": "EasternFront", "neighbors": ["Bul/EC", "Rum", "Gre"], "coastal": True},
    "Spa/NC": {"front_id": "WesternFront", "neighbors": ["Por", "Gas", "Spa/SC"], "coastal": True},
    "Spa/SC": {"front_id": "WesternFront", "neighbors": ["Spa/NC", "Mar", "Por", "Mid"], "coastal": True},
}

STANDARD_ADJACENCY = {
    "Cly": ["Edi", "Lvp", "NWG"], "Edi": ["Cly", "Yor", "NTH", "NWG"],
    "Lvp": ["Cly", "Yor", "Wal", "IRI"], "Yor": ["Lvp", "Wal", "Lon", "NTH"],
    "Wal": ["Lvp", "Yor", "Lon", "IRI", "ENG"], "Lon": ["Wal", "Yor", "ENG", "NTH"],
    "Nwy": ["NTH", "NWG", "BAR", "SKA", "Swe", "Fin", "Stp"],
    "Swe": ["Nwy", "SKA", "Den", "BAL", "BOT", "Fin"],
    "Fin": ["Nwy", "Swe", "Stp", "BOT"], "Stp": ["Fin", "Nwy", "BAR", "BOT", "Mos", "Lvn"],
    "Lvn": ["Stp", "Mos", "War", "Pru", "BAL", "BOT"], "Den": ["NTH", "SKA", "Swe", "HEL", "Kie", "BAL"],
    "Hol": ["NTH", "HEL", "Kie", "Ruh", "Bel"], "Bel": ["NTH", "ENG", "Pic", "Bur", "Ruh", "Hol"],
    "Kie": ["Den", "HEL", "BAL", "Ber", "Mun", "Ruh", "Hol"], "Ruh": ["Hol", "Kie", "Mun", "Bur", "Bel"],
    "Ber": ["Kie", "Pru", "Sil", "Mun"], "Pru": ["Ber", "Sil", "War", "BAL", "Lvn"],
    "Sil": ["Ber", "Pru", "War", "Gal", "Boh", "Mun"], "Mun": ["Ruh", "Kie", "Ber", "Sil", "Boh", "Tyr", "Vie", "Bur"],
    "Pic": ["Bel", "ENG", "Bre", "Par", "Bur"], "Bre": ["ENG", "MAO", "Pic", "Par", "Gas"],
    "Par": ["Pic", "Bre", "Gas", "Bur"], "Bur": ["Pic", "Par", "Gas", "Mar", "Mun", "Ruh", "Bel"],
    "Gas": ["Bre", "Par", "Bur", "Mar", "Spa", "MAO"], "Mar": ["Gas", "Bur", "Pie", "Spa", "LYO"],
    "Spa": ["Gas", "Mar", "Por", "MAO", "WES", "LYO"], "Por": ["Spa", "MAO"],
    "NAf": ["MAO", "WES", "Tun"], "Tun": ["WES", "TYS", "ION", "NAf"],
    "Pie": ["Mar", "LYO", "Tus", "Ven", "Tyr"], "Ven": ["Pie", "Tyr", "Tri", "Apu", "Rom"],
    "Tus": ["Pie", "LYO", "TYS", "Rom"], "Rom": ["Tus", "Ven", "Apu", "Nap", "TYS"],
    "Nap": ["Rom", "Apu", "ION", "TYS"], "Apu": ["Ven", "Rom", "Nap", "ION", "ADR"],
    "Boh": ["Mun", "Sil", "Gal", "Vie", "Tyr"], "Tyr": ["Mun", "Boh", "Vie", "Tri", "Ven", "Pie"],
    "Vie": ["Mun", "Boh", "Tyr", "Tri", "Bud", "Gal"], "Tri": ["Vie", "Tyr", "Ven", "Apu", "ADR", "Alb", "Ser", "Bud"],
    "Bud": ["Vie", "Tri", "Gal", "Rum", "Ser"], "Gal": ["Vie", "Bud", "Rum", "Ukr", "War", "Sil", "Boh"],
    "Ser": ["Tri", "Bud", "Rum", "Bul", "Gre", "Alb"], "Alb": ["Tri", "Ser", "Gre", "ION", "ADR"],
    "Gre": ["Alb", "Ser", "Bul", "AEG", "ION"], "Bul": ["Ser", "Rum", "Gre", "Con", "AEG", "BLA"],
    "Rum": ["Bud", "Gal", "Ukr", "Sev", "BLA", "Bul", "Ser"], "Con": ["Bul", "BLA", "Ank", "Smy", "AEG"],
    "Smy": ["Con", "Ank", "Arm", "EAS", "AEG"], "Ank": ["Con", "Smy", "Arm", "BLA"],
    "Arm": ["Ank", "Smy", "Sev", "Syr", "BLA"], "Syr": ["Arm", "Smy", "EAS"],
    "Sev": ["Arm", "Ukr", "Rum", "BLA", "Mos"], "Ukr": ["Gal", "War", "Mos", "Sev", "Rum"],
    "Mos": ["Stp", "Lvn", "War", "Ukr", "Sev"], "War": ["Lvn", "Pru", "Sil", "Gal", "Ukr", "Mos"],
    "NAO": ["NWG", "Cly", "IRI", "MAO"], "NWG": ["NAO", "BAR", "Nwy", "NTH", "Edi", "Cly"],
    "BAR": ["NWG", "Nwy", "Stp"], "NTH": ["NWG", "Nwy", "SKA", "Den", "HEL", "Hol", "Bel", "ENG", "Lon", "Yor", "Edi"],
    "SKA": ["NTH", "Nwy", "Swe", "Den"], "HEL": ["NTH", "Den", "Kie", "Hol"],
    "BAL": ["Den", "Swe", "BOT", "Lvn", "Pru", "Ber", "Kie"], "BOT": ["Swe", "Fin", "Stp", "Lvn", "BAL"],
    "ENG": ["NTH", "Bel", "Pic", "Bre", "MAO", "IRI", "Wal", "Lon"], "IRI": ["NAO", "MAO", "ENG", "Wal", "Lvp"],
    "MAO": ["NAO", "IRI", "ENG", "Bre", "Gas", "Spa", "Por", "WES", "NAf"],
    "WES": ["MAO", "Spa", "LYO", "TYS", "Tun", "NAf"], "LYO": ["WES", "TYS", "Pie", "Tus", "Rom", "Mar", "Spa"],
    "TYS": ["WES", "LYO", "ION", "Tun", "Nap", "Rom", "Tus"], "ION": ["TYS", "Tun", "Alb", "Gre", "AEG", "EAS", "Nap", "Apu", "ADR"],
    "ADR": ["ION", "Alb", "Tri", "Ven", "Apu"], "AEG": ["ION", "Gre", "Bul", "Con", "Smy", "EAS"],
    "EAS": ["ION", "AEG", "Smy", "Syr"], "BLA": ["Rum", "Bul", "Con", "Ank", "Arm", "Sev"],
}

SEA_PROVINCES = {
    "ADR", "AEG", "BAL", "BAR", "BLA", "BOT", "EAS", "ENG", "HEL", "ION",
    "IRI", "LYO", "MAO", "NAO", "NTH", "NWG", "SKA", "TYS", "WES",
}

for province, neighbors in STANDARD_ADJACENCY.items():
    PROVINCE_DATA.setdefault(province, {"front_id": "", "coastal": False})["neighbors"] = neighbors


PROVINCE_GRAPH = {
    province: set(metadata.get("neighbors", []))
    for province, metadata in PROVINCE_DATA.items()
}

FRONT_GRAPH = {}
for province, metadata in PROVINCE_DATA.items():
    front = metadata.get("front_id")
    if front:
        FRONT_GRAPH.setdefault(front, set()).add(province)


def get_fronts_for_country(country, owned_provinces):
    """Return a set of front ids represented by the country's owned provinces."""
    fronts = set()
    for province in owned_provinces:
        meta = PROVINCE_DATA.get(province, {})
        front_id = meta.get("front_id")
        if front_id:
            fronts.add(front_id)
    return fronts


def get_neighbors_for_province(province):
    return list(PROVINCE_GRAPH.get(province, set()))


def get_legal_neighbors_for_unit(province, unit_type):
    """Return strategic forecast destinations legal for an army or fleet."""
    origin = (province or "").split("/")[0]
    neighbors = PROVINCE_GRAPH.get(origin, set())
    if unit_type == "A":
        return sorted(neighbor for neighbor in neighbors if neighbor not in SEA_PROVINCES)

    if unit_type == "F":
        if origin not in SEA_PROVINCES and not PROVINCE_DATA.get(origin, {}).get("coastal"):
            return []
        return sorted(
            neighbor for neighbor in neighbors
            if neighbor in SEA_PROVINCES or PROVINCE_DATA.get(neighbor, {}).get("coastal")
        )

    return []


def compute_board_tactical_metrics(country, units_by_province, sc_owners):
    """Return tactical exposure metrics from the current occupied board."""
    occupants = {
        province: unit.country
        for province, unit in (units_by_province or {}).items()
    }
    own_units = {province for province, owner in occupants.items() if owner == country}
    owned_centers = {province for province, owner in (sc_owners or {}).items() if owner == country}

    frontline_units = set()
    hostile_adjacencies = 0
    for province in own_units:
        hostile_neighbors = [
            neighbor for neighbor in PROVINCE_GRAPH.get(province, set())
            if occupants.get(neighbor) not in (None, country)
        ]
        if hostile_neighbors:
            frontline_units.add(province)
            hostile_adjacencies += len(hostile_neighbors)

    threatened_centers = set()
    defended_centers = set()
    for center in owned_centers:
        neighbors = PROVINCE_GRAPH.get(center, set())
        if any(occupants.get(neighbor) not in (None, country) for neighbor in neighbors):
            threatened_centers.add(center)
            if center in own_units or any(occupants.get(neighbor) == country for neighbor in neighbors):
                defended_centers.add(center)

    unvisited = set(frontline_units)
    active_fronts = 0
    while unvisited:
        active_fronts += 1
        pending = [unvisited.pop()]
        while pending:
            province = pending.pop()
            connected = PROVINCE_GRAPH.get(province, set()) & unvisited
            unvisited -= connected
            pending.extend(connected)

    return {
        "active_fronts": active_fronts,
        "frontline_units": len(frontline_units),
        "hostile_adjacencies": hostile_adjacencies,
        "threatened_centers": len(threatened_centers),
        "defended_threatened_centers": len(defended_centers),
        "exposed_centers": len(threatened_centers - defended_centers),
        "center_defense_rate": (
            len(defended_centers) / len(threatened_centers)
            if threatened_centers else 1.0
        ),
        "isolation": max(0.0, 1.0 - (len(frontline_units) / max(1, len(own_units)))),
        "encirclement": min(1.0, hostile_adjacencies / max(1, len(own_units) * 2)),
    }


def get_country_front_pressure(owned_provinces, hostile_countries):
    """Count hostile adjacent pressure on the country from neighboring countries."""
    hostile = set(hostile_countries or [])
    pressure = 0
    for province in owned_provinces:
        for neighbor in get_neighbors_for_province(province):
            if neighbor in hostile:
                pressure += 1
    return pressure


def compute_country_geography_metrics(country, owned_provinces, neighboring_countries=None):
    """
    Build a simple geography-focused metric bundle for a country.
    - active_fronts = number of unique front ids touched by owned provinces
    - isolation = higher when provinces are disconnected and not spread across many fronts
    - encirclement = hostile border pressure from adjacent enemy countries
    """
    owned = {province for province in (owned_provinces or []) if province in PROVINCE_DATA}
    if not owned:
        return {
            "active_fronts": 0,
            "isolation": 1.0,
            "encirclement": 0.0,
        }

    fronts = get_fronts_for_country(country, owned)
    active_fronts = len(fronts)

    # Isolation rises as a country owns provinces on fewer fronts and fewer connected routes.
    isolation = max(0.0, 1.0 - (active_fronts / 4.0))

    hostile = set(neighboring_countries or [])
    hostile_pressure = get_country_front_pressure(owned, hostile)
    encirclement = min(1.0, hostile_pressure / max(1, len(owned) * 2))

    return {
        "active_fronts": active_fronts,
        "isolation": isolation,
        "encirclement": encirclement,
    }


def compute_country_geography_from_units(country, unit_positions, ownership_by_province, hostile_countries=None):
    """
    unit_positions: dict[str, str] | set[str]
        Either a mapping of owner -> province or a direct set of province names.
    ownership_by_province: dict[str, str] mapping province -> owner country
    """
    owned_provinces = {
        province for province, owner in ownership_by_province.items()
        if owner == country and province in PROVINCE_DATA
    }

    if isinstance(unit_positions, dict):
        for owner, province in unit_positions.items():
            if owner == country and province in PROVINCE_DATA:
                owned_provinces.add(province)
    elif unit_positions:
        for province in unit_positions:
            if province in PROVINCE_DATA:
                owned_provinces.add(province)

    hostile = set(hostile_countries or [])
    return compute_country_geography_metrics(country, owned_provinces, hostile)
