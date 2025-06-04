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

def select_nature():
    nature_options = [
        "Hardy", "Lonely", "Brave", "Adamant", "Naughty",
        "Bold", "Docile", "Relaxed", "Impish", "Lax",
        "Timid", "Hasty", "Serious", "Jolly", "Naive",
        "Modest", "Mild", "Quiet", "Bashful", "Rash",
        "Calm", "Gentle", "Sassy", "Careful", "Quirky"
    ]

    while True:
        print(f"Available Natures:")
        for i in range(0, len(nature_options), 5):
            print(' | '.join(nature_options[i:i+5]))
        chosen_nature = input("Select a nature: ").capitalize()

        if chosen_nature in nature_options:
            return chosen_nature  # Return valid nature selection
        else:
            print("Invalid nature. Please choose from the list.")

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
    moves_per_page = 60  # 10 rows of 3 moves per page
    print("Available Moves:")

    # Display moves in 3-column format with pagination
    for page_start in range(0, len(available_moves), moves_per_page):
        page_moves = available_moves[page_start:page_start + moves_per_page]
        
        # Print 3 moves per row with proper numbering
        for row_start in range(0, len(page_moves), 3):
            row_moves = page_moves[row_start:row_start + 3]
            row_text = "  ".join(
                f"{page_start + row_start + i + 1:>3}. {move.capitalize():<20}"
                for i, move in enumerate(row_moves))
            print(row_text)
        
        # Pagination control
        if page_start + moves_per_page < len(available_moves):
            user_input = input("\nPress Enter to see more or 'done' to finish: ").lower()
            if user_input == "done":
                break
            print()  # Add spacing before next page

    # Prompt user to select four moves
    while len(chosen_moves) < 4:
        try:
            choice = int(input(f"\nSelect move {len(chosen_moves) + 1}/4 by number (1-{len(available_moves)}): "))
            if 1 <= choice <= len(available_moves):
                selected_move = available_moves[choice - 1]
                if selected_move not in chosen_moves:
                    chosen_moves.append(selected_move)
                    print(f"Added {selected_move.capitalize()}!")
                else:
                    print("You already selected that move. Try again.")
            else:
                print(f"Please enter a number between 1 and {len(available_moves)}.")
        except ValueError:
            print("Please enter a valid number.")
    
    print("\nFinal moveset:")
    for i, move in enumerate(chosen_moves, 1):
        print(f"{i}. {move.capitalize()}")
    
    return chosen_moves


if __name__ == "__main__":
    pokemon_name = input("Enter a pokemon name: ").lower()
    pokemon_info = get_pokemon_info(pokemon_name)

    if pokemon_info:
        #collecting types, abilities, and moves
        types = [t["type"]["name"] for t in pokemon_info["types"]]
        abilities = [a["ability"]["name"] for a in pokemon_info["abilities"]]
        moves = [m["move"]["name"] for m in pokemon_info["moves"]]
        chosen_nature = select_nature()
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