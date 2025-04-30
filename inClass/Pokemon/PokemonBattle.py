from PokemonClasses import Pokemon
from PokemonTrainer import Trainer


class Battle:
    def __init__(self, trainer1: Trainer, trainer2: Trainer) -> None:
        self.trainer1 = trainer1
        self.trainer2 = trainer2
        self.current_trainer = trainer1
        self.playing = True

    def start_battle(self) -> None:
        #remove choose battle
        self.trainer1.choose_pokemon()
        self.trainer2.choose_pokemon()
        while self.playing:
            if not self.trainer1.check_pokemon():
                self.winner(self.trainer2)
                break
            if not self.trainer2.check_pokemon():
                self.winner(self.trainer1)
                break
        self.turn()

    def turn(self) -> None:
        options = [self.current_trainer.attack_with_pokemon, self.current_trainer.heal_pokemon, self.flee ]
        while True:
            try:
                option = options[int(input(f"{self.current_trainer.name.upper()}\n1: attack\n2: heal\n3: flee"))]
            except (ValueError, IndexError):
                pass
            else:
                option()
                self.current_trainer = self.trainer1 if self.current_trainer == self.trainer2 else self.trainer2

    def flee(self) -> None:
        trainer = self.trainer2 if self.current_trainer == self.trainer2 else self.trainer1
        self.playing = False
        print(f"{trainer.name} fleed!")
        self.winner()

    def winner(self, trainer):
        print(f"{trainer.name} won!")
    