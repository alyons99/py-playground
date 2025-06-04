import requests

base_url = "https://pokeapi.co/api/v2/"

class Pokemon:
    def __init__(self, name, types, nature, abilities, moves):
        self.name = name
        self.types = types
        self.nature = nature
        self.abilities = abilities
        self._ability = None
        self.moves = moves


    
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

def select_ability(available_abilities):
    while True:
        print(f"Available Abilities: {', '.join([a.capitalize() for a in available_abilities])}")
        chosen_ability = input("Select an ability: ").lower()

        if chosen_ability in available_abilities:
            return chosen_ability  # Return valid ability selection
        else:
            print("Invalid ability. Please choose from the list.")

def select_moves(available_moves):
    chosen_moves = []
    print("Available Moves (showing 100 at a time):")

    # Display moves in batches of 100
    for i in range(0, len(available_moves), 100):  
        print("\n".join(f"{idx + 1}. {move.capitalize()}" for idx, move in enumerate(available_moves[i:i+100], i)))
        if input("Press Enter to see more or type 'done' to finish: ").lower() == "done":
            break

    # Prompt user to select four moves
    while len(chosen_moves) < 4:
        try:
            choice = int(input(f"Select a move by number (1-{len(available_moves)}): "))
            if 1 <= choice <= len(available_moves) and available_moves[choice - 1] not in chosen_moves:
                chosen_moves.append(available_moves[choice - 1])
            else:
                print("Invalid choice or duplicate move. Try again.")
        except ValueError:
            print("Please enter a valid number.")
    
    return chosen_moves


if __name__ == "__main__":
    pokemon_name = input("Enter a pokemon name: ").lower()
    pokemon_info = get_pokemon_info(pokemon_name)

    if pokemon_info:
        #collecting types, abilities, and moves
        types = [t["type"]["name"] for t in pokemon_info["types"]]
        abilities = [a["ability"]["name"] for a in pokemon_info["abilities"]]
        moves = [m["move"]["name"] for m in pokemon_info["moves"]]
        chosen_nature = input("Enter a nature: ")
        chosen_ability = select_ability(abilities)
        selected_moves = select_moves(moves)

        pokemon = Pokemon(pokemon_info["name"], types, chosen_nature, abilities, selected_moves)
        pokemon.ability = chosen_ability

        # #, pokemon_info["type"], pokemon_info["ability"]
        # print(f"Name: {pokemon.name.capitalize()}")
        # #need to loop AGAIN to capitalize all values :(
        # print(f"Type(s): {', '.join([t.capitalize() for t in pokemon.types])}")
        # print(f"Possible Ability(s): {', '.join([a.capitalize() for a in pokemon.abilities])}")
        # try:
        #     chosen_ability = input(f"Select an ability from: {', '.join(pokemon.abilities)}\n")
        #     pokemon.ability = chosen_ability
        #     print(f"{pokemon.name.capitalize()} now has the ability: {pokemon.ability.capitalize()}")
        # except ValueError as e:
        #     print(e)
    

        print("*****************************************")
        print(f"Your {pokemon.name.capitalize()}: \nType: {', '.join([t.capitalize() for t in pokemon.types])} \nNature: {chosen_nature}\nAbility: {pokemon.ability.capitalize()}\nMoves: {', '.join([m.capitalize() for m in pokemon.moves])}")
        print("*****************************************")

        # pick_ability()


        #only capitalized the first value
        # print(f"Type(s): {', '.join(pokemon.types).capitalize()}")

# if pokemon_info:
#     print(f"Name: {pokemon_info["name"].capitalize()}")
#     print(f"Id: {pokemon_info["id"]}")
#     print(f"Height: {pokemon_info["height"] * .1:.01f} m")
#     print(f"Weight: {pokemon_info["weight"] * .1:.01f} kg")