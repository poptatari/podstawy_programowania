# Create an array with 5 dictionaries, each containing 
# a country and its population. Then, print the array contents.

countries = [
    {"name": "Poland", "population": 38000000},
    {"name": "Germany", "population": 83000000},
    {"name": "France", "population": 68000000},
    {"name": "Spain", "population": 47000000},
    {"name": "Italy", "population": 59000000}
]
print('COUNTRY  POPULATION')
for country in countries:
    print(f"{country['name']}   {country['population']}")

