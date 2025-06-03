import requests

base_url = "https://pokeapi.co/api/v2/"

class Pokemon:
    def __init__(self, name):
        self.name = name
        # self.type = type
        # self.ability = ability
    
    # @ability.setter
    # def ability(self, new_ability):
    #     pass



def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        print("Pokemon found.")
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data. Reponse code: {response.status_code}")

if __name__ == "__main__":
    pokemon_name = input("Enter a pokemon name: ").lower()
    pokemon_info = get_pokemon_info(pokemon_name)

    if pokemon_info:
        pokemon = Pokemon(pokemon_info["name"])
        #, pokemon_info["type"], pokemon_info["ability"]
        print(f"Pokemon Name: {pokemon.name.capitalize()}")

# if pokemon_info:
#     print(f"Name: {pokemon_info["name"].capitalize()}")
#     print(f"Id: {pokemon_info["id"]}")
#     print(f"Height: {pokemon_info["height"] * .1:.01f} m")
#     print(f"Weight: {pokemon_info["weight"] * .1:.01f} kg")