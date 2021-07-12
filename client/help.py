import keyboard
import time

from utils import clear
from utils import GoBack
from rich import print
from rich.console import Console
from rich.prompt import Prompt
from rich.align import Align

console = Console()

def help_navigation(currentpage):
    """
    Allows user to cycle through the help pages.
    """

    page_cycle: list = ["About", "Boxes", "Messages", "Pref"]
    currentpage: int = page_cycle.index(currentpage)

    if currentpage == 3:
        next: int = page_cycle[0]
        previous: int = page_cycle[2]

    elif currentpage == 0:
        next: int = page_cycle[1]
        previous: int = page_cycle[3]
    
    else:
        next: int = page_cycle[currentpage + 1]
        previous: int = page_cycle[currentpage - 1]

    console.print("\n[bold white][bold red]![/]   Use [bold magenta] right arrow[/] or [bold magenta]left arrow[/] to navigate the page, or press [bold magenta]BACKSPACE[/] to return to Menu.[/]")
    
    #Adding delays between key presses so that the pages won't cyle through too fast.
    time.sleep(0.2)

    while True:
        if keyboard.is_pressed("left_arrow"):
            if previous == "About":
                help_start_Page()
                break

            elif previous == "Boxes":
                help_boxes()
                break

            elif previous == "Messages":
                help_messages()
                break

            elif previous == "Pref":
                help_preference()
                break

        elif keyboard.is_pressed("right_arrow"):
            if next == "About":
                help_start_Page()
                break

            elif next == "Boxes":
                help_boxes()
                break

            elif next == "Messages":
                help_messages()
                break

            elif next == "Pref":
                help_preference()
                break
        
        elif keyboard.is_pressed("backspace"):
            GoBack()

def help_start_Page():
    clear()
    paragraph = "[bright_white]'ThaBox' is a social media platform in which the conversations \nbetween users are for the users only. Not a single message is \nsaved in the server, giving you the utmost privacy. Chat with \nstrangers in public boxes, or have a blast with your friends \nin private boxes. \n\n[/][bold grey58]This program was created for the 'Python Discord 2021 CodeJam'.\n[/]"

    console.print((Align("[bold cyan]ABOUT[/]\n", align = "center", )))
    console.print((Align(paragraph, align = "center")))
    help_navigation('About')

def help_boxes():
    clear()
    paragraph = "[bright_white]There are two types of boxes available - a private and a public\nbox. When creating a public box, you get a session ID, which\nothers can find in a list of public boxes and join. However, when\ncreating a private box, you get a session ID and have to set a\npassword for the box. Any user with the session ID and password\ncan join your box.\n[/]"

    console.print((Align("[bold cyan]JOINING AND CREATING BOXES[/]\n", align = "center", )))
    console.print((Align(paragraph, align = "center")))
    help_navigation('Boxes')

def help_messages():
    clear()
    paragraph = "[bright_white]Message can be sent to another person in the same box, by simply\ntyping it out when you recieve the prompt. Only 1 person in the\nbox can type at once, so you may need to wait until someone else\nhas finished.\n\nMessages that you received are available only until the next \nmessage has been sent. Past message are deleted and can't be \nretrieved.\n[/]"

    console.print((Align("[bold cyan]SENDING AND RECEIVING MESSAGES[/]\n", align = "center", )))
    console.print((Align(paragraph, align = "center")))
    help_navigation("Messages")

def help_preference():
    clear()
    paragraph = "[bright_white]The colour scheme of your message box can be changed in the\n'Preferences' settings. A valid colour name, a hex ('#xxxxxx')\nor an [bold red]R[/][bold green]G[/][bold blue]B[/] ('rgb(r, g, b)') value\ncan be used to personalise different parts of your box. [/]\n"

    console.print((Align("[bold cyan]PREFERENCES[/]\n", align = "center", )))
    console.print((Align(paragraph, align = "center")))
    help_navigation("Pref")

help_start_Page()