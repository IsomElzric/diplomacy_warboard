SUPPLY_CENTERS = {
    # England
    "Lon": "England",
    "Edi": "England",
    "Lvp": "England",

    # France
    "Par": "France",
    "Mar": "France",
    "Bre": "France",

    # Germany
    "Ber": "Germany",
    "Mun": "Germany",
    "Kie": "Germany",

    # Italy
    "Rom": "Italy",
    "Ven": "Italy",
    "Nap": "Italy",

    # Austria
    "Vie": "Austria",
    "Bud": "Austria",
    "Tri": "Austria",

    # Turkey
    "Smy": "Turkey",
    "Ank": "Turkey",
    "Con": "Turkey",

    # Russia
    "War": "Russia",
    "Mos": "Russia",
    "Stp": "Russia",
    "Sev": "Russia",

    # Neutral SCs
    "Bel": "",
    "Hol": "",
    "Den": "",
    "Nwy": "",
    "Swe": "",
    "Spa": "",
    "Por": "",
    "Ser": "",
    "Gre": "",
    "Bul": "",
    "Rum": "",
    "Tun": ""
}

STARTING_SUPPLY_CENTERS = SUPPLY_CENTERS.copy()


def reset_supply_centers():
    global SUPPLY_CENTERS
    SUPPLY_CENTERS = STARTING_SUPPLY_CENTERS.copy()
