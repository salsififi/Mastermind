"""
DEVINEZ LA COMBINAISON SECRÈTE
A mastermind game in commandline
Challenge n°17 from the Docstring Discord server
(https://discord.com/channels/396825382009044994/1137654909873967225/1263915841359970445)

Date: 2024-07-27
Author: Simon Salvaing
(Thanks to @Rocket for his code review !)
"""

from mastermind.constants import (GAME_RULES)
from mastermind.game import Game


def main() -> None:
    """Game loop"""
    print(GAME_RULES)
    Game().play()


if __name__ == '__main__':
    main()
