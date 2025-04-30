from PokemonClasses import Pokemon

class Trainer:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__team = []
        self.__chosen : Pokemon = None

    def add_pokemon(self, pokemon: Pokemon) -> None:
        """
        Adds a pokemon to the trainers team
        :param pokemon: the pokemon you want added to the team
        """
        self.__team.append(pokemon)

    @property
    def trainer_team(self):
        return self.__team
    @property
    def name(self) -> str:
        return self.__name
    
    def choose_pokemon(self) -> Pokemon:
        for i in range(len(self.__team)):
            print(f"{i + 1}:\n{self.__team[i].status()}\n")

        while True:
            try:
                self._change_chosen(self.__team[int(input("pokemons index: ")) - 1])
                print(self.__name)
            except (IndexError, ValueError):
                pass
            else:
                print(f"{self.__chosen.name} was chosen!")
                return self.__chosen
            
    def _change_chosen(self, pokemon) -> None:
        """
        used for the backend to easily change pokemon
        :param pokemon: the pokemon you want chosen (the pokemon that will be used in attack_with_pokemon and heal_pokemon)
        """
        self.__chosen = pokemon

    @property
    def chosen(self):
        return self.__chosen

    def attack_with_pokemon(self) -> int:
        """
        :prints: the string with the attack move
        :returns: the amount of damage
        """
        if self.__chosen:
            print(self.__chosen.attack_move())
            return self.__chosen.attack
        
    def heal_pokemon(self) -> None:
        """
        Heals the chosen pokemon
        :prints: a string with the pokemons name and their current hp
        """
        if self.__chosen:
            self.__chosen.heal()
            print(f"{self.__chosen.name} got healed. Current hp: {self.chosen.hp}")

    def check_pokemon(self) -> bool:
        for pokemon in self.__team:
            if pokemon.hp > 0:
                return True
        return False