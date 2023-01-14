#!/usr/bin/env python

import requests
import numpy.random as random

def get_pokemon(id):
    url = "https://pokeapi.co/api/v2/pokemon-species/" + str(id)
    response = requests.get(url)
    if response.status_code != 200:
        print(response.text)
    else:
        data = response.json()
        return data

def get_pokemon_names(id, languages='all'):
    data = get_pokemon(id)
    names = []
    #if no language is specified, get all names
    if languages == 'all':
        for name in data['names']:
            names.append(name['name'])
    else:
        for language in languages:
            for name in data['names']:
                if name['language']['name'] == language:
                    names.append(name['name'])
    return names

def get_number_of_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon-species/?limit=0/"
    response = requests.get(url)
    if response.status_code != 200:
        print(response.text)
    else:
        data = response.json()
        return data['count']

def get_random_pokemon_id():
    return random.randint(1, get_number_of_pokemon())

