import sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format as fg

# init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected


def word_art(s):
    # cprint(figlet_format(str(s), font='starwars'), 'yellow', 'on_red', attrs=['bold'])
    ascii_banner = fg(str(s))
    print(ascii_banner)

stages = ['''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''']

