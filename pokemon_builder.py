import requests

base_url = "https://pokeapi.co/api/v2/"

class Pokemon:
    def __init__(self, name, types, abilities):
        self.name = name
        self.types = types
        self.abilities = abilities
        self._ability = None
    
    @property
    def ability(self):
        return self._ability
    
    @ability.setter
    def ability(self, new_ability):
        if new_ability in self.abilities:
            self._ability = new_ability
        else:
            raise ValueError(f"Invalid Ability.")


def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        # print("Pokemon found.")
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data. Reponse code: {response.status_code}")

if __name__ == "__main__":
    pokemon_name = input("Enter a pokemon name: ").lower()
    pokemon_info = get_pokemon_info(pokemon_name)

    if pokemon_info:
        #since types can be one or more, we need to loop through the types and store them as a 
        types = [t["type"]["name"] for t in pokemon_info["types"]]
        abilities = [a["ability"]["name"] for a in pokemon_info["abilities"]]

        pokemon = Pokemon(pokemon_info["name"], types, abilities)
        #, pokemon_info["type"], pokemon_info["ability"]
        print(f"Name: {pokemon.name.capitalize()}")
        #need to loop AGAIN to capitalize all values :(
        print(f"Type(s): {', '.join([t.capitalize() for t in pokemon.types])}")
        print(f"Possible Ability(s): {', '.join([a.capitalize() for a in pokemon.abilities])}")
        try:
            chosen_ability = input(f"Select an ability from: {', '.join(pokemon.abilities)}\n")
            pokemon.ability = chosen_ability
            print(f"{pokemon.name.capitalize()} now has the ability: {pokemon.ability.capitalize()}")
        except ValueError as e:
            print(e)
        
        print("*****************************************")
        print(f"Your {pokemon.name.capitalize()}: \nType: {', '.join([t.capitalize() for t in pokemon.types])} \nAbility: {pokemon.ability.capitalize()}")
        print("*****************************************")

        # pick_ability()


        #only capitalized the first value
        # print(f"Type(s): {', '.join(pokemon.types).capitalize()}")

# if pokemon_info:
#     print(f"Name: {pokemon_info["name"].capitalize()}")
#     print(f"Id: {pokemon_info["id"]}")
#     print(f"Height: {pokemon_info["height"] * .1:.01f} m")
#     print(f"Weight: {pokemon_info["weight"] * .1:.01f} kg")