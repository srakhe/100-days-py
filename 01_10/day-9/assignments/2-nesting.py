travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# TODO: Write the function that will allow new countries
def add_new_country(country_name, visits, cities):
    travel_log.append({"country": country_name, "visits": visits, "cities": cities})


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
