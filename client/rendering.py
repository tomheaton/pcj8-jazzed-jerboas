from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.console import Console

from utils import clear

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True) 
# Colorame module for creating panel manually because rich wont let u see the string that is actually being printed.

console = Console()

logo_text = Text.assemble(
    (
"""
$$$$$$$$\\ $$\\
\\__$$  __|$$ |
   $$ |   $$$$$$$\\   $$$$$$\\
   $$ |   $$  __$$\\  \\____$$\\
   $$ |   $$ |  $$ | $$$$$$$ |
   $$ |   $$ |  $$ |$$  __$$ |
   $$ |   $$ |  $$ |\\$$$$$$$ |
   \\__|   \\__|  \\__| \\_______|\n
""",
     "bold magenta"),
    (
"""$$$$$$$\\
$$  __$$\\
$$ |  $$ | $$$$$$\  $$\   $$\\
$$$$$$$\ |$$  __$$\ \$$\ $$  |
$$  __$$\ $$ /  $$ | \$$$$  /
$$ |  $$ |$$ |  $$ | $$  $$<
$$$$$$$  |\$$$$$$  |$$  /\$$\\
\\_______/  \\______/ \\__/  \\__|
""",
     "bold cyan")
)


ENDC = '\033[0m'
box_logo_lines = [
    f"{Fore.RED}╭────────────────────────────────╮  ",
    f"{Fore.RED}│                                │  ",
    f"{Fore.RED}│ {Style.BRIGHT}{Fore.MAGENTA}$$$$$$$$\\ $$\\                  {Style.NORMAL}{Fore.RED}│  ",
    f"{Fore.RED}│ {Style.BRIGHT}{Fore.MAGENTA}\\__$$  __|$$ |                 {Style.NORMAL}{Fore.RED}│  ",
    f"{Fore.RED}│    {Style.BRIGHT}{Fore.MAGENTA}$$ |   $$$$$$$\\   $$$$$$\\   {Style.NORMAL}{Fore.RED}│  ",
    f"{Fore.RED}│    {Style.BRIGHT}{Fore.MAGENTA}$$ |   $$  __$$\\  \\____$$\\  {Style.NORMAL}{Fore.RED}│  ",
    f"{Fore.RED}│    {Style.BRIGHT}{Fore.MAGENTA}$$ |   $$ |  $$ | $$$$$$$ | {Style.NORMAL}{Fore.RED}│  ",
    f"{Fore.RED}│    {Style.BRIGHT}{Fore.MAGENTA}$$ |   $$ |  $$ |$$  __$$ | {Style.NORMAL}{Fore.RED}│  ",
    f"{Fore.RED}│    {Style.BRIGHT}{Fore.MAGENTA}$$ |   $$ |  $$ |\\$$$$$$$ | {Style.NORMAL}{Fore.RED}│  ",
    f"{Fore.RED}│    {Style.BRIGHT}{Fore.MAGENTA}\\__|   \\__|  \\__| \\_______| {Style.NORMAL}{Fore.RED}│  ",
    f"{Fore.RED}│                                │  ",
    f"{Fore.RED}│ {Style.BRIGHT}{Fore.CYAN}$$$$$$$\\                       {Style.NORMAL}{Fore.RED}│  ",
    f"{Fore.RED}│ {Style.BRIGHT}{Fore.CYAN}$$  __$$\\                      {Style.NORMAL}{Fore.RED}│  ",
    f"{Fore.RED}│ {Style.BRIGHT}{Fore.CYAN}$$ |  $$ | $$$$$$\\  $$\\   $$\\  {Style.NORMAL}{Fore.RED}│  ",
    f"{Fore.RED}│ {Style.BRIGHT}{Fore.CYAN}$$$$$$$\\ |$$  __$$\\ \\$$\\ $$  | {Style.NORMAL}{Fore.RED}│  ",
    f"{Fore.RED}│ {Style.BRIGHT}{Fore.CYAN}$$  __$$\\ $$ /  $$ | \\$$$$  /  {Style.NORMAL}{Fore.RED}│  ",
    f"{Fore.RED}│ {Style.BRIGHT}{Fore.CYAN}$$ |  $$ |$$ |  $$ | $$  $$<   {Style.NORMAL}{Fore.RED}│  ",
    f"{Fore.RED}│ {Style.BRIGHT}{Fore.CYAN}$$$$$$$  |\\$$$$$$  |$$  /\\$$\\  {Style.NORMAL}{Fore.RED}│  ",
    f"{Fore.RED}│ {Style.BRIGHT}{Fore.CYAN}\\_______/  \\______/ \\__/  \\__| {Style.NORMAL}{Fore.RED}│  ",
    f"{Fore.RED}│                                │  ",
    f"{Fore.RED}╰────────────────────────────────╯  "
]
menu_logo = "".join([x+ENDC+"\n" if x != box_logo_lines[-1] else x+ENDC for x in box_logo_lines])


def render_box(rows: list) -> Text:
    """
    This function gets the Text-object that is shown to the user once in a session.

    :param rows: A list of strings that together make a box. (There must be at least 16 rows/items)
    :return: Text-object which can be printed with console.print().
    """
    logo_rows = logo_text.split("\n")
    rows = ['  ' + x for x in rows]

    if len(rows) < 16:
        raise ValueError("The argument rows needs to contain at least 16 rows.")
    if len(rows) > 16:
        dummy_rows_to_add = len(rows) - len(logo_rows)
        dummy_rows = [Text.assemble(('-' * 30, "red")) for _ in range(dummy_rows_to_add)]
        for i in range(dummy_rows_to_add):
            logo_rows.append(dummy_rows[i])

    new_rows = []
    for i in range(0, len(rows)):
        new_rows.append(Text.assemble(logo_rows[i], rows[i] + '\n'))
    return Text.assemble(*new_rows)



def render_menu_screen(rows: list) -> Text:
    """
    This function gets the Text-object that is shown to the user once in the main_menu.

    :param rows: A list of strings that together make a box. (There must be at least 21 rows/items)
    :return: Text-object which can be printed with console.print().
    """
    
    logo_rows = menu_logo.split("\n")


    if len(rows) < 21:
        raise ValueError("The argument rows needs to contain at least 21 rows.")
    if len(rows) > 21:
        dummy_rows_to_add = len(rows) - len(logo_rows)
        dummy_rows = [Text.assemble(('-' * 34+"  ", "red")) for _ in range(dummy_rows_to_add)]
        for i in range(dummy_rows_to_add):
            logo_rows.append(dummy_rows[i])

    new_rows = []
    for i in range(0, len(rows)):
        new_rows.append(Text.assemble(logo_rows[i], rows[i] + '\n'))
    return Text.assemble(*new_rows)



