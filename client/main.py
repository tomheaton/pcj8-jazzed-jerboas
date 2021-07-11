from rich.text import Text
from rich.prompt import Prompt
from rich.panel import Panel
from rich.console import Console

from utils import User, Preferences, GoBack, clear
from rendering import render_menu_screen



# Importing of functions to run on select
import credits
import login














console = Console()

main_title = Text.assemble(
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


def main_menu(logged_in: bool = False, logged_in_as = None):
    selected = False
    if logged_in:
        options = {
            "Logged in as "+logged_in_as.username: 1,
            "Create box": 2,
            "Join box": 3,
            "Preferences": 4,
            "Help/Info": 5,
            "Credits": 6,
            "Exit": 7
        }
    if not logged_in:
        options = {
            "Logg in/Sign up": 1,
            "Help/Info": 2,
            "Credits": 3,
            "Exit": 4
        }
    
    hover_on = 1
    while not selected:
        rows = []
        rows_temp = [x.center(len("--------------------"), "|") for x in list(options)]
        if logged_in:
            logged_in_as_msg = rows_temp.pop(0)
        rows_temp[hover_on-1] = Text.assemble((rows_temp[hover_on-1].center(len("--------------------"), "|"), "bold yellow"))
        

        rows.append(Text.assemble(("--------------------", "bold blue")))
        for i in rows_temp:
            rows.append("")
            rows.append("")
            rows.append(i)
            rows.append("")
            rows.append("")
            rows.append(Text.assemble(("--------------------", "bold blue")))
        
        # Fill up unused space.
        while len(rows) < 21:
            rows.append(Text.assemble(("--------------------", "bold red")))
        
        if logged_in:
            rows.insert(0, Text.assemble((logged_in_as_msg, "bold green")))
        
        console.print(render_menu_screen(rows))
    
        what_to_do = Prompt.ask(Text.assemble(("1: Scroll up\n", "bold cyan"), ("2: Scroll down\n", "bold cyan"), ("3: Select\n", "bold purple")), choices=["1", "2", "3"], default="3")
        if what_to_do == "1":
            if hover_on == 1:
                clear()
                continue
            hover_on -= 1
        if what_to_do == "2":
            if hover_on == len(rows_temp):
                clear()
                continue
            hover_on += 1
        if what_to_do == "3":
            if logged_in:
                if hover_on == 1:
                    try:
                        clear()
                        pass # Create box
                        hover_on = 1
                        clear()
                        continue
                    except GoBack:
                        hover_on = 1
                        clear()
                        continue
                elif hover_on == 2:
                    try:
                        clear()
                        pass # Join box
                        hover_on = 1
                        clear()
                        continue
                    except GoBack:
                        hover_on = 1
                        clear()
                        continue
                elif hover_on == 3:
                    try:
                        clear()
                        pass # Preferences
                        hover_on = 1
                        clear()
                        continue
                    except GoBack:
                        hover_on = 1
                        clear()
                        continue
                elif hover_on == 4:
                    try:
                        clear()
                        pass # Help/Info
                        hover_on = 1
                        clear()
                        continue
                    except GoBack:
                        hover_on = 1
                        clear()
                        continue
                elif hover_on == 5:
                    try:
                        clear()
                        credits.credits() # Credits
                        hover_on = 1
                        clear()
                        continue
                    except GoBack:
                        hover_on = 1
                        clear()
                        continue
                elif hover_on == 6:
                    clear()
                    exit() # Exit, not even implemented yet lol
            
            if hover_on == 1:
                clear()
                return main_menu(logged_in=True, logged_in_as=login.login())
            elif hover_on == 2:
                try:
                    clear()
                    pass # Help/Info
                    hover_on = 1
                    clear()
                    continue
                except GoBack:
                    hover_on = 1
                    clear()
                    continue
            elif hover_on == 3:
                try:
                    clear()
                    credits.credits() # Credits
                    hover_on = 1
                    clear()
                    continue
                except GoBack:
                    hover_on = 1
                    clear()
                    continue
            elif hover_on == 4:
                clear()
                exit() # Exit, not even implemented yet lol


        clear()
        
        


if __name__ == '__main__':
    main_menu()
    