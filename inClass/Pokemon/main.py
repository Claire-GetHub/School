from PokemonClasses import Pokemon, ElectricPokemon, FirePokemon, WaterPokemon
from PokemonTrainer import Trainer
from PokemonBattle import Battle


def main():
    e1 = ElectricPokemon("Jolteon", 1, 100, 10)
    f1 = FirePokemon("Flareon", 1, 100, 10)
    e2 = ElectricPokemon("Jolteon", 1, 100, 10)
    f2 = FirePokemon("Flareon", 1, 100, 10)

    trainer1 = Trainer("skittles")
    trainer1.add_pokemon(e1)
    trainer1.add_pokemon(f1)
    trainer2 = Trainer("jolly")
    trainer2.add_pokemon(e2)
    trainer2.add_pokemon(f2)

    pb = Battle(trainer1, trainer2)
    pb.start_battle()

def test_Trainer():
    e = ElectricPokemon("Jolteon", 1, 100, 10)
    f = FirePokemon("Flareon", 1, 100, 10)
    trainer = Trainer("skittles")
    trainer.add_pokemon(e)
    trainer.add_pokemon(f)
    #trainer.choose_pokemon()
    trainer._change_chosen(f)
    print(trainer.attack_with_pokemon())

def test_pokemon():
    e = ElectricPokemon("Jolteon", 1, 100, 10)
    f = FirePokemon("Flareon", 1, 100, 10)
    w = WaterPokemon("Vaporeon", 1, 100, 10)
    pokemons = [e,f,w]
    for pokemon in pokemons:
        print()
        print(pokemon.status())
        print(pokemon.attack_move())
        pokemon.level_up()
        print(pokemon.status())
        

if __name__ == "__main__":
    main()