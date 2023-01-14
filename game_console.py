#!/usr/bin/env python

import pokemon_api as pokemon_api
import japanese


#zesvgreqgh
def gess_name_translation(language1, language2, pokemon_id,names=None):
    if names == None:
        names = pokemon_api.get_pokemon_names(pokemon_id, [language1, language2])
    if(names.__len__() < 2):
        print("Error: pokemon not found")
        return

    print("What is the name of this pokemon in " + language2 + "?")
    
    print(names[0])

    answer = input()
    if answer.lower() == names[1].lower():
        print("Correct!")
    else:
        print("Wrong! The correct answer is " + names[1])

#zesvgreqgh
def gess_name_in_romanji(pokemon_id, name=None):
    if name == None:
        name = pokemon_api.get_pokemon_names(pokemon_id, ['ja'])
    print("What is this pokemon's name in romaji?")
    print(name)
    answer = input()
    if answer.lower() == japanese.japanese_to_romanji(name).lower():
        print("Correct!")
    else:
        print("Wrong! The correct answer is " + japanese.japanese_to_romanji(name))



def main():
    while True:
        pokemon_id = pokemon_api.get_random_pokemon_id()
        names = pokemon_api.get_pokemon_names(pokemon_id, ['ja', 'fr'])
        gess_name_in_romanji(pokemon_id, names[0])
        gess_name_translation('ja', 'fr', 0, names)
        
main()