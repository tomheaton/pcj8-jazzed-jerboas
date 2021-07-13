import textwrap
import re

from rich import console
import rich
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.console import Console
from rich.screen import Screen 
from rich.live import Live
from rich.markup import escape

from utils import clear, User, Preferences
import time
import random


def get_index_duplicates(lst, item):
    return [i for i, x in enumerate(lst) if x == item]

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
    RED+"╭────────────────────────────────╮  "+ENDC,
    RED+"│                                │  "+ENDC,
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

box_rows = [
        "[{}]┌───────────────────────────────────────────────────────────────────────────────────┐",
        "[{}]│[/]{}[{}]│[/]",
        "[{}]│[/]{}[{}]│[/]",
        "[{}]│[/]{}[{}]│[/]",
        "[{}]│[/]{}[{}]│[/]",
        "[{}]│[/]{}[{}]│[/]",
        "[{}]│[/]{}[{}]│[/]",
        "[{}]│[/]{}[{}]│[/]",
        "[{}]│[/]{}[{}]│[/]",
        "[{}]│[/]{}[{}]│[/]",
        "[{}]│[/]{}[{}]│[/]",
        "[{}]│[/]{}[{}]│[/]",
        "[{}]│[/]{}[{}]│[/]",
        "[{}]│[/]{}[{}]│[/]",
        "[{}]│[/]{}[{}]│[/]",
        "[{}]│[/]{}[{}]│[/]",
        "[{}]│[/]{}[{}]│[/]",
        "[{}]│[/]{}[{}]│[/]",
        "[{}]│[/]{}[{}]│[/]",
        "[{}]│[/]{}[{}]│[/]",
        "[{}]│[/]{}[{}]│[/]",
        "[{}]│[/]{}[{}]│[/]",
        "[{}]│[/]{}[{}]│[/]",
        "[{}]│[/]{}[{}]│[/]",
        "[{}]│[/]{}[{}]│[/]",
        "[{}]└───────────────────────────────────────────────────────────────────────────────────┘[/]"
        
        #"┘",
        #"└",
        #"┘",
        #"┐",
        #"├",
        #"┤",
        #"─"
    ]

menu_logo = "".join([x+"\n" if x != box_logo_lines[-1] else x for x in box_logo_lines])


def render_box(rows: list) -> Text:
    """
    Discontinued project........
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


def get_box(rows, preferences):
    if len(rows) != 26:
        raise ValueError("Box must contain 26 rows.")

    border_color = "green"


    new_rows = []

    count = -1
    for i in rows:
        count +=1
        new_rows.append(Text.from_markup(box_rows[count].format(border_color, i, border_color)))
    return new_rows



def get_message_box(msg_sender: User, message: str, stage: int):
    """Returns a list of strings which together assemble the message box that is being displayed in ThaBox."""
    size = len(message)

    name_color = "bold cyan"
    message_color = "bold white"
    border_color = "bold magenta"


    message_lines = textwrap.wrap(message, width=32)

    message_string = ""
    count = 0
    for _ in message_lines:
        count += 1
        if not count == len(message_lines):
            message_string += f"│{_ : <32}│" + "\n"
            continue
        message_string += f"│{_ : <32}│"
        
    if len(message_string.splitlines()) > 9:
       raise ValueError("Message too long!")

    msg_box = \
    f"""┌────────────────────────────────┐
│{"Message from" : ^32}│
│{msg_sender.username : ^32}│
├────────────────────────────────┤
{message_string}
└────────────────────────────────┘"""
    

    
    lines = msg_box.splitlines()
    if stage < 34:
        a = [line[(34-stage):34]for line in lines]
    if stage >= 34:
        a = ["".join([" " for _ in range(stage-34)])+line for line in lines]
    
    new = []

    c = 0
    for i in a:
        c+=1
        if c == 1 or c == 2 or c == 4:
            new.append(Text.from_markup(f"[{border_color}]{i}[/]\n"))
            continue
        if c == 3:
            list_username = list(user.username)
            list_line = list(i)
            if list_line.count("│")-list_username.count("│") == 2: # Ignore │ in usernames.
                indexes = get_index_duplicates(list_line, "│")
                list_line[indexes[0]] = f"[{border_color}]│[/][{name_color}]"
                list_line[indexes[-1]] = f"[/][{border_color}]│[/]\n"
                new.append(Text.from_markup("".join(list_line)))
            if list_line.count("│")-list_username.count("│") == 1:
                indexes = get_index_duplicates(list_line, "│")
                list_line[indexes[-1]] = f"[/][{border_color}]│[/]\n"
                list_line.insert(0, f"[{name_color}]")
                new.append(Text.from_markup("".join(list_line)))
            continue
        if not c-4 > len(message_lines):
            list_line = list(i)
            current_msg_line = list(message_lines[c-5])
            if list_line.count("│")-current_msg_line.count("│") == 2: # Ignore │ in usernames.
                indexes = get_index_duplicates(list_line, "│")

                list_line[indexes[0]] = f"[{border_color}]│[/][{message_color}]"
                list_line[indexes[-1]] = f"[/][{border_color}]│[/]\n"

                new.append(Text.from_markup("".join(list_line)))
            if list_line.count("│")-current_msg_line.count("│") == 1:
                indexes = get_index_duplicates(list_line, "│")

                if stage == 1:
                    list_line[0] = f"[{border_color}]│[/]\n" 
                else:
                    list_line[0] = f"[{message_color}]"
                    list_line[indexes[-1]] = f" [{border_color}]│[/]\n" 
                
                
                new.append(Text.from_markup("".join(list_line)))

        if c-4 > len(message_lines):
            list_line = list(i)
            if "└" in list_line and "┘" in list_line: 
                indexleft = get_index_duplicates(list_line, "└")[0]
                indexright = get_index_duplicates(list_line, "┘")[0]

                list_line[indexleft] = f"[{border_color}]└"
                list_line[indexright] = f"┘[/]"
                new.append(Text.from_markup("".join(list_line)))

            if "┘" in list_line and  not "└" in list_line:
                index = get_index_duplicates(list_line, "┘")[0]
              
                if stage == 1:
                    list_line[index] = f"[{border_color}]┘[/]"
                    
                else:
                    list_line[0] = f"[{border_color}]─"
                    list_line[index] = f"┘[/]"
                new.append(Text.from_markup("".join(list_line)))
                
                




    return new


   


    direction = random.randint(1, 2) # Message will fade in from one of two directions. (left, right)

    
if __name__ == '__main__':
    user = User(username=r"MyDogCummedOnTeenagers", paswrd="thisis100%hashedlol", preferences=Preferences())
    console = Console()
    
    
    
    with Live("", refresh_per_second=5000) as live:
        for _ in range(0, 90):
            a = get_message_box(user, "The message box now works with color and animation at the same time. Now I need to intergrate it in render_box. That will be hell, but its worth it for the end result. aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", _)
            
            new_Text = Text("")
            for i in a:
                new_Text = Text.assemble(new_Text, i)
            live.update(new_Text)
            time.sleep(0.0000004)

        
 



