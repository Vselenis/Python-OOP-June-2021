# from OOP.defining_classes_exercise.3.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught " + pokemon.pokemon_details()
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        for pokemon in self.pokemons:
            if pokemon.name == pokemon_name:
                self.pokemons.remove(pokemon)
                return f"You have released {pokemon_name}"

        return "Pokemon is not caught"




    def trainer_data(self):
        result = [f"Pokemon Trainer {self.name}",
                 f"Pokemon count {len(self.pokemons)}"]

        pokemon_info = [f"- {p.pokemon_details()}" for p in self.pokemons]

        return '\n'.join(result + pokemon_info)
        
# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())
#

