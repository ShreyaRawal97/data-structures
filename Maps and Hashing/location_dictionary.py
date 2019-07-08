# Code

locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Egypt': ['Cairo']}
# TODO: Print a list of all cities in the USA in alphabetic order.
usa_sorted = sorted(locations['North America']['USA'])
print (1)
for city in usa_sorted:
    print (city)

# TODO: Print all cities in Asia, in alphabetic order, next to the name of the country
asia_cities = []
print (2)
for countries, cities in locations['Asia'].items():
    city_country = cities[0] + " - " + countries
    asia_cities.append(city_country)
asia_sorted = sorted(asia_cities)
for city in asia_sorted:
    print (city)
