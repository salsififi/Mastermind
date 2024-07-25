"""
game.py
Contains Game class
"""

from random import randint

from mastermind.combo import Combo
from mastermind.constants import NB_OF_COLORS_BY_COMBO, COLORS


class Game:
    """A Mastermind Game"""

    def __init__(self) -> None:
        self.attempt_number: int = 1
        self.end: bool = False
        self.secret_combo = self.generate_secret_combo()

    @staticmethod
    def generate_secret_combo():
        """Generates the secret combination of colors"""
        return Combo("".join(str(randint(1, len(COLORS)))
                             for _ in range(NB_OF_COLORS_BY_COMBO)))


if __name__ == '__main__':
    for _ in range(10):
        g = Game()
        print(g.secret_combo)
