"""
constants.py
Constants needed
"""

from colorama import Fore

# Colors
COLORS = {1: Fore.YELLOW,
          2: Fore.BLUE,
          3: Fore.RED,
          4: Fore.GREEN,
          5: Fore.WHITE,
          6: Fore.MAGENTA, }
COLORS_CODES = "".join(str(nb) for nb in COLORS)
FRENCH_COLORS_NAMES = ("Jaune", "Bleu", "Rouge", "Vert", "Blanc", "Magenta")
WELL_POSITIONNED = Fore.RED
WRONGLY_POSITIONNED = Fore.WHITE

# Game constants
NB_OF_COLORS_BY_COMBO = 4
MAX_NB_OF_ATTEMPTS = 12

# Symbols
SQUARE = "\u25A0"  # corresponding to ■
DOT = "\u25CF"  # corresponding to ●

# Game messages
SEPARATOR = " " * 5
COLORS_STRING = SEPARATOR.join(f"[{nb}]: {color}{FRENCH_COLORS_NAMES[nb - 1]}{Fore.RESET}"
                               for nb, color in COLORS.items())
GAME_RULES = f"""JEU DU MASTERMIND
Trouvez en maximum {MAX_NB_OF_ATTEMPTS} coups la combinaison secrète de {NB_OF_COLORS_BY_COMBO} couleurs 
générée par l'ordinateur.
Une même couleur peut être utilisée plusieurs fois.
À chaque tentative, vous obtiendrez des indications:
- chaque pastille rouge signifiera "l'une des couleurs est bien placée"
- chaque pastille blanche signifiera "l'une des couleurs est mal placée"
Voici les chiffres à utiliser pour indiquer les couleurs de votre choix:
{COLORS_STRING}
"""
INPUT_MESSAGE = "[{}] Saisissez les {} chiffres de votre combinaison: "
INVALID_COMBO_MESSAGE = (f"{Fore.RED}{'SAISIE INVALIDE:'}{Fore.RESET} la combinaison doit "
                         f"contenir {NB_OF_COLORS_BY_COMBO} chiffres compris entre 1 et {len(COLORS)}.\n")
NO_COLOR_FOUND_MESSAGE = "🥹 Aucune couleur n'est présente dans la combinaison secrète..."
LOSE_MESAGE = """😓🥹😰 Vous avez épuisé vos {} tentatives.
La combinaison secrète était: {} ({})."""
WIN_MESSAGE = "🎉🎉🎉 Bravo ! Vous avez trouvé la combinaison secrète en {} coups. 🎉🎉🎉"
