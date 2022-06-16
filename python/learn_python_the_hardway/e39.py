states = {
    'Oregon': 'OR',
    'Flordia:': 'FL',
    'Texas': 'TX',
    'New York':'NY'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'TX': 'Austin'
}

cities['NY'] = 'New York'

print('-' * 10)

print("Oregon's abbreviation is ", states['Oregon'])
print('-' * 10)

print("Texas has: ", cities[states['Texas']])

print('-' * 10)

for abbrev,city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

state = states.get('California')

if not state:
    print("Sorry no California")

city = cities.get('TX','Does not exist')
print(f"The capitol of Texas is {city}.")
