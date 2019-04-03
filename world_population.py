import json

filname = 'population_data.json'

with open(filname) as f:
    pop_data = json.load(f)

    for pop_dict in pop_data:
        if pop_dict['Year'] == '1960':
            country_name = pop_dict['Country Name']
            population = pop_dict['Value']
            print(country_name + ":" + population)
