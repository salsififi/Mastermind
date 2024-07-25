"""
combo.py
Contains Combo class
"""
from colorama import Fore

from mastermind.constants import COLORS, COLORS_CODES, SQUARE


class Combo:
    """A combination of 4 colors in a Mastermind game"""

    def __init__(self, combo: str) -> None:
        if len(combo) != 4 or any(char not in COLORS_CODES for char in combo):
            raise ComboError()
        self.combo = combo

    @property
    def colors(self) -> str:
        """Displays colored squares based on combo"""
        return " ".join(COLORS[int(char)] + SQUARE + Fore.RESET for char in self.combo)

    def __repr__(self):
        return f"Combo {self.combo}: {self.colors}"

    def __str__(self) -> str:
        return f"{self.colors}"

    def __eq__(self, other) -> bool:
        return self.combo == other.combo


class ComboError(Exception):
    pass
