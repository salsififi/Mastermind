"""
game.py
Contains Game class
"""

from random import choices

from colorama import Fore

from mastermind.answer import Answer
from mastermind.combo import Combo, ComboError
from mastermind.constants import NB_OF_COLORS_BY_COMBO, COLORS, INPUT_MESSAGE, INVALID_COMBO_MESSAGE, SEPARATOR, \
    WIN_MESSAGE, MAX_NB_OF_ATTEMPTS, LOSE_MESAGE


class Game:
    """A Mastermind Game"""

    def __init__(self) -> None:
        self.attempt_number: int = 1
        self.end: bool = False
        self.secret_combo: Combo = self.generate_secret_combo()

    @staticmethod
    def generate_secret_combo() -> Combo:
        """Generates the secret combination of colors"""
        return Combo("".join(str(num) for num in choices(list(COLORS), k=NB_OF_COLORS_BY_COMBO)))

    def play(self) -> None:
        """Runs a Matermind game"""
        while not self.end:
            try:
                player_combo = Combo(input(INPUT_MESSAGE.format(f"Essai n°{self.attempt_number}"
                                                                if self.attempt_number < MAX_NB_OF_ATTEMPTS
                                                                else f"{Fore.RED}{'DERNIER ESSAI !'}{Fore.RESET}",
                                                                NB_OF_COLORS_BY_COMBO)))
            except ComboError:
                print(INVALID_COMBO_MESSAGE)
                continue

            if player_combo == self.secret_combo:
                self.end = True
                print(f"{player_combo}{SEPARATOR}{WIN_MESSAGE.format(self.attempt_number)}")
            else:
                self.attempt_number += 1
                print(f"{player_combo}{SEPARATOR}{Answer(player_combo, self.secret_combo)}\n")
                if self.attempt_number > MAX_NB_OF_ATTEMPTS:
                    self.end = True
                    print(LOSE_MESAGE.format(MAX_NB_OF_ATTEMPTS, self.secret_combo, self.secret_combo.combo))
