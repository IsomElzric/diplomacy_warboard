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
