from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.console import Console

from utils import clear

import colorama
# Colorame module for creating panel manually because rich wont let u see the string that is actually being printed.




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

RED = '\033[91m'
ENDC = '\033[0m'
PURPLE = '\033[95m'
CYAN = '\033[96m'

box_logo_lines = [
    RED+"╭────────────────────────────────╮  ",
    RED+"│                                │  ",
    RED+"│"+ENDC+PURPLE+" $$$$$$$$\\ $$\\                  "+ENDC+RED+"│"+ENDC+"  ",
    RED+"│"+ENDC+PURPLE+" \\__$$  __|$$ |                 "+ENDC+RED+"│"+ENDC+"  ",
    RED+"│"+ENDC+PURPLE+"    $$ |   $$$$$$$\\   $$$$$$\\   "+ENDC+RED+"│"+ENDC+"  ",
    RED+"│"+ENDC+PURPLE+"    $$ |   $$  __$$\\  \\____$$\\  "+ENDC+RED+"│"+ENDC+"  ",
    RED+"│"+ENDC+PURPLE+"    $$ |   $$ |  $$ | $$$$$$$ | "+ENDC+RED+"│"+ENDC+"  ",
    RED+"│"+ENDC+PURPLE+"    $$ |   $$ |  $$ |$$  __$$ | "+ENDC+RED+"│"+ENDC+"  ",
    RED+"│"+ENDC+PURPLE+"    $$ |   $$ |  $$ |\\$$$$$$$ | "+ENDC+RED+"│"+ENDC+"  ",
    RED+"│"+ENDC+PURPLE+"    \\__|   \\__|  \\__| \\_______| "+ENDC+RED+"│"+ENDC+"  ",
    RED+"│                                │"+ENDC+"  ",
    RED+"│"+ENDC+CYAN+" $$$$$$$\\                       "+ENDC+RED+"│"+ENDC+"  ",
    RED+"│"+ENDC+CYAN+" $$  __$$\\                      "+ENDC+RED+"│"+ENDC+"  ",
    RED+"│"+ENDC+CYAN+" $$ |  $$ | $$$$$$\\  $$\\   $$\\  "+ENDC+RED+"│"+ENDC+"  ",
    RED+"│"+ENDC+CYAN+" $$$$$$$\\ |$$  __$$\\ \\$$\\ $$  | "+ENDC+RED+"│"+ENDC+"  ",
    RED+"│"+ENDC+CYAN+" $$  __$$\\ $$ /  $$ | \\$$$$  /  "+ENDC+RED+"│"+ENDC+"  ",
    RED+"│"+ENDC+CYAN+" $$ |  $$ |$$ |  $$ | $$  $$<   "+ENDC+RED+"│"+ENDC+"  ",
    RED+"│"+ENDC+CYAN+" $$$$$$$  |\\$$$$$$  |$$  /\\$$\\  "+ENDC+RED+"│"+ENDC+"  ",
    RED+"│"+ENDC+CYAN+" \\_______/  \\______/ \\__/  \\__| "+ENDC+RED+"│"+ENDC+"  ",
    RED+"│                                │  "+ENDC,
    RED+"╰────────────────────────────────╯  "+ENDC
]

menu_logo = "".join([x+"\n" if x != box_logo_lines[-1] else x for x in box_logo_lines])


def render_box(rows: list, console) -> Text:
    """
    This function gets the Text-object that is shown to the user once in a session.

    :param rows: A list of strings that together make a box. (There must be at least 16 rows/items)
    :return: Text-object which can be printed with console.print().
    """
    logo_rows = menu_logo.split("\n")

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



def render_menu_screen(rows: list, console) -> Text:
    
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



