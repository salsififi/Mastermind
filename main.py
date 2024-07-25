"""
DEVINEZ LA COMBINAISON SECRÈTE
A mastermind game in commandline
Challenge n°17 from the Docstring Discord server
(https://discord.com/channels/396825382009044994/1137654909873967225/1263915841359970445)
Date: 2024-07-23
"""

from colorama import Fore

from mastermind.answer import Answer
from mastermind.combo import Combo, ComboError
from mastermind.constants import (GAME_RULES, MAX_NB_OF_ATTEMPTS, WIN_MESSAGE, LOSE_MESAGE,
                                  INPUT_MESSAGE, INVALID_COMBO_MESSAGE)
from mastermind.game import Game


def main():
    """Game loop"""
    print(GAME_RULES)
    game = Game()
    while not game.end:
        try:
            player_combo = Combo(input(INPUT_MESSAGE.format(f"Essai n°{game.attempt_number}"
                                                            if game.attempt_number < MAX_NB_OF_ATTEMPTS
                                                            else f"{Fore.RED + 'DERNIER ESSAI !' + Fore.RESET}")))
        except ComboError:
            print(INVALID_COMBO_MESSAGE)
            continue

        print(player_combo, end="\t")
        if player_combo == game.secret_combo:
            game.end = True
            print(WIN_MESSAGE.format(game.attempt_number))
        else:
            game.attempt_number += 1
            print(Answer(player_combo, game.secret_combo))
            print()
            if game.attempt_number > MAX_NB_OF_ATTEMPTS:
                game.end = True
                print(LOSE_MESAGE.format(MAX_NB_OF_ATTEMPTS, game.secret_combo, game.secret_combo.combo))


if __name__ == '__main__':
    main()
