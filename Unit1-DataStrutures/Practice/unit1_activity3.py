country_codes = {
    "Afghanistan":"AFG",
    "Canada":"CAN",
    "Chad":"TCD",
    "Chile":"CHL",
    "China":"CHN",
    "Christmas Island":"CXR",
    "Germany":"DEU",
    "Greece":"GRC",
    "Greenland":"GRL",
    "Iceland":"IRL"
    }

print()
print(country_codes)

country_codes['Hungary'] = "HUN"
keys = list(country_codes.keys())
print(f"\nYou added the country {keys[-1]}")

del country_codes["Afghanistan"]

print()
print(country_codes)

country_codes.pop("Canada")

print()
print(country_codes)