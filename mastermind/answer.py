"""
answer.py
Contains Answer class
"""

from colorama import Fore

from mastermind.combo import Combo
from mastermind.constants import DOT, WELL_POSITIONNED, WRONGLY_POSITIONNED, NO_COLOR_FOUND_MESSAGE


class Answer:
    """The answer given, after a player has proposed a combination"""
    def __init__(self, player_attempt: Combo, secret_combo: Combo) -> None:
        self.player_colors: list = list(player_attempt.combo)
        self.secret_colors: list = list(secret_combo.combo)
        self.content = self.get_answer_colors()

    def __str__(self) -> str:
        return f"Indications: {self.content}" if self.content else NO_COLOR_FOUND_MESSAGE

    def get_answer_colors(self) -> str:
        """Returns the answer string to display"""
        answer = []

        # Looking for well-placed colors
        for i, char in enumerate(self.player_colors):
            if char == self.secret_colors[i]:
                answer.append(f"{WELL_POSITIONNED}{DOT}{Fore.RESET}")
                self.player_colors[i] = "x"
                self.secret_colors[i] = "x"

        # Looking for wrongly-placed colors
        for i, char in enumerate(self.player_colors):
            if char != "x" and char in self.secret_colors:
                answer.append(f"{WRONGLY_POSITIONNED}{DOT}{Fore.RESET}")
                self.player_colors[i] = "x"
                self.secret_colors[self.secret_colors.index(char)] = "x"

        return " ".join(answer)
