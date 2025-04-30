
class Pokemon:


    def __init__(self, name: str, type: str, level: int, hp: int, attack: int ) -> None:
        """
        Creates a pokemon

        parameters
            :param name: pokemons name
            :param type: pokemons type
            :param level: pokemons level
            :param hp: pokemons health
            :param attack: pokemons attack damage
        """
        self.__name = name
        self.__type = type
        self.__level = level
        self.__hp = hp
        self.__max_hp = hp
        self.__attack = attack

    def attack_move(self, move: str = "slash") -> str:
        """
        returns the pokemons attack

        parameter
            :param move: The name of the move (defaults to basic "slash" move)

        returns
            A string with the pokemons name and what move they used
        """

        return f"{self.__name} used {move}"
    
    def damaged(self, damage) -> None:
        """
        removes given amount of health from pokemon

        parameter
            :param damage: the amount of damage done to a pokemon

        :returns: a string with the pokemons name and the aount they were damaged.
        """
        self.__hp = self.__hp - damage if self.__hp - damage >= 0 else 0
        return f"{self.__name} got {damage} damage. Current hp: {self.__hp}"
    
    def heal(self) -> str:
        """
        heals pokemon by 10
        """
        self.__hp = self.__hp + 10 if self.__hp + 10 <= self.__max_hp else self.__max_hp
        return f"{self.__name} got healed by 10"
    
    def level_up(self) -> str:
        """
        Adds to attributes: level, hp, and attack
            :level: Adds 1
            :hp: Adds 10
            :attack: Adds 5
        """
        self.__level += 1
        self.__hp += 10
        self.__attack += 5
        return f"{self.__name} is now level {self.__level}"

    def status(self) -> str:
        """
        Prints the current value of all attributes

        returns
            A string with all atributes and thier names
        """
        return f"name: {self.__name}\ntype: {self.__type}\nlevel: {self.__level}\nhp: {self.__hp}\nattack: {self.__attack}"
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def attack(self) -> int:
        return self.__attack
    
    @property
    def hp(self) -> int:
        return self.__hp
    



class ElectricPokemon(Pokemon):
    def __init__(self, name: str, level: int, hp: int, attack: int) -> None:
        """
        Creates a electric pokemon

        parameters
            :param name: pokemons name
            :param level: pokemons level
            :param hp: pokemons health
            :param attack: pokemons attack damage
        """
        super().__init__(name, "electric", level, hp, attack)
        self.__electric_move = "zap"

    def attack_move(self) -> str:
        """
        returns the pokemons attack

        returns
            A string with the pokemons name and what move they used
        """      
        return super().attack_move(self.__electric_move)
    


class FirePokemon(Pokemon):
    def __init__(self, name: str, level: int, hp: int, attack: int) -> None:
        """
        Creates a fire pokemon

        parameters
            :param name: pokemons name
            :param level: pokemons level
            :param hp: pokemons health
            :param attack: pokemons attack damage
        """
        super().__init__(name, "fire", level, hp, attack)
        self.__fire_move = "blast"

    def attack_move(self) -> str:
        """
        returns the pokemons attack

        returns
            A string with the pokemons name and what move they used
        """      
        return super().attack_move(self.__fire_move)



class WaterPokemon(Pokemon):
    def __init__(self, name: str, level: int, hp: int, attack: int) -> None:
        """
        Creates a water pokemon

        parameters
            :param name: pokemons name
            :param level: pokemons level
            :param hp: pokemons health
            :param attack: pokemons attack damage
        """
        super().__init__(name, "water", level, hp, attack)
        self.__water_move = "splash"

    def attack_move(self) -> str:
        """
        returns the pokemons attack

        returns
            A string with the pokemons name and what move they used
        """      
        return super().attack_move(self.__water_move)
    