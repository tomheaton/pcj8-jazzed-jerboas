import keyboard
import time
from utils import clear
from utils import GoBack
from rich import print
from rich.console import Console
from rich.prompt import Prompt
from rich.align import Align

console = Console()


def help_navigation(currentpage, user):
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

    console.print(
        "\n[bold white][bold red]![/]   Use [bold magenta] right arrow[/] or [bold magenta]left arrow[/] to navigate the page, or press [bold magenta]BACKSPACE[/] to return to Menu.[/]")

    # Adding delays between key presses so that the pages won't cyle through too fast.
    time.sleep(0.2)

    while True:
        if keyboard.is_pressed("left_arrow"):
            if previous == "About":
                help_start_page(user)
                break

            elif previous == "Boxes":
                help_boxes(user)
                break

            elif previous == "Messages":
                help_messages(user)
                break

            elif previous == "Pref":
                help_preference(user)
                break

        elif keyboard.is_pressed("right_arrow"):
            if next == "About":
                help_start_page(user)
                break

            elif next == "Boxes":
                help_boxes(user)
                break

            elif next == "Messages":
                help_messages(user)
                break

            elif next == "Pref":
                help_preference(user)
                break

        elif keyboard.is_pressed("backspace"):
            raise GoBack


def help_start_page(user):
    if user is not None:
        main_style = user.preferences.preference_dict["Border Colour"]
    else:
        main_style = "bold cyan"
    clear()

    paragraph = """
    [bright_white]ThaBox is a social media platform in which the conversations 
    between users are for the users only. Not a single message is
    saved, giving you the utmost privacy. Chat with
    strangers in boxes, or have a blast with your friends
    in boxes.
    
    [/][bold grey58]This program was created for the 'Python Discord 2021 CodeJam'.\n[/]
    """

    console.print((Align(f"""[{main_style}]
    ▄▀█ █▄▄ █▀█ █ █ ▀█▀
    █▀█ █▄█ █▄█ █▄█  █ [/]\n""", align="center", )))
    console.print((Align(paragraph, align="center")))
    help_navigation('About', user)


def help_boxes(user):
    if user is not None:
        main_style = user.preferences.preference_dict["Border Colour"]
    else:
        main_style = "bold cyan"
    clear()

    paragraph = """
    [bright_white]When creating a box, it will check if a box of that 
    name already exists, and if it doesn't one will be created. However,
    if it does exist, you will join the box and be able to start talking.
    [/]
    """

    console.print((Align(f"""[{main_style}]
     █▄▄ █▀█ ▀▄▀ █▀▀ █▀
     █▄█ █▄█ █ █ ██▄ ▄█[/]\n""", align="center", )))
    console.print((Align(paragraph, align="center")))
    help_navigation('Boxes', user)


def help_messages(user):
    if user is not None:
        main_style = user.preferences.preference_dict["Border Colour"]
    else:
        main_style = "bold cyan"
    clear()

    paragraph = """
    [bright_white]Messages can be sent to another person in the same box, by simply
    typing it out when you receive the prompt. However you can only see the other 
    people's messages after you have finished typing.
    
    Messages that you receive are available for some seconds after
    the message has been sent. Message are not stored and can't be
    retrieved.
    [/]
    """

    console.print((Align(f"""[{main_style}]
    █▀▄▀█ █▀▀ █▀ █▀ ▄▀█ █▀▀ █▀▀ █▀
    █ ▀ █ ██▄ ▄█ ▄█ █▀█ █▄█ ██▄ ▄█[/]\n""", align="center", )))
    console.print((Align(paragraph, align="center")))
    help_navigation("Messages", user)


def help_preference(user):
    if user is not None:
        main_style = user.preferences.preference_dict["Border Colour"]
    else:
        main_style = "bold cyan"
    clear()
    paragraph = """
    [bright_white]The colour scheme of your box can be changed in the
    preferences page once logged in. A valid colour name or a hex-value (#xxxxxx)
    can be used to personalise different parts of your box. [/]
    
    """

    console.print((Align(f"""[{main_style}]
    █▀█ █▀█ █▀▀ █▀▀ █▀▀ █▀█ █▀▀ █▄ █ █▀▀ █▀▀ █▀
    █▀▀ █▀▄ ██▄ █▀  ██▄ █▀▄ ██▄ █ ▀█ █▄▄ ██▄ ▄█[/]\n""", align="center", )))
    console.print((Align(paragraph, align="center")))
    help_navigation("Pref", user)

