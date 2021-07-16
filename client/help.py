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
    paragraph = "[bright_white]ThaBox is a social media platform in which the conversations " \
                "\nbetween users are for the users only. Not a single message is " \
                "\nsaved, giving you the utmost privacy. Chat with " \
                "\nstrangers in public boxes, or have a blast with your friends " \
                "\nin private boxes. " \
                "\n\n[/][bold grey58]This program was created for the 'Python Discord 2021 CodeJam'.\n[/]"

    paragraph = """
    [bright_white]ThaBox is a social media platform in which the conversations 
    between users are for the users only. Not a single message is
    saved, giving you the utmost privacy. Chat with
    strangers in public boxes, or have a blast with your friends
    in private boxes.
    
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
    paragraph = "[bright_white]There are two types of boxes available - a private and a public" \
                "\nbox. When creating a public box, you get a session ID, which" \
                "\nothers can find in a list of public boxes and join. However, when" \
                "\ncreating a private box, you get a session ID and have to set a" \
                "\npassword for the box. Any user with the session ID and password" \
                "\ncan join your box.\n[/]"
    paragraph = """
    [bright_white]There are two types of boxes available - a private and a public
    box. When creating a public box, you get a session ID, which
    others can find in a list of public boxes and join. However, when
    creating a private box, you get a session ID and have to set a
    password for the box. Any user with the session ID and password
    can join your box.
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
    paragraph = "[bright_white]Messages can be sent to another person in the same box, by simply"\
                "\ntyping it out when you receive the prompt. Only 1 person in the"\
                "\nbox can type at once, so you may need to wait until someone else"\
                "\nhas finished."\
                "\n\nMessages that you receive are available for some seconds."\
                "\nmessage has been sent. Past message are not stored and can't be "\
                "\nretrieved.\n[/]"
    paragraph = """
    [bright_white]Messages can be sent to another person in the same box, by simply
    typing it out when you receive the prompt. Only 1 person in the
    box can type at once, so you may need to wait until someone else
    has finished.
    
    Messages that you receive are available for some seconds.
    message has been sent. Past message are not stored and can't be
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
    paragraph = "[bright_white]The colour scheme of your box can be changed in the"\
                "\nPreferences page once logged in. A valid colour name or a hex-value (#xxxxxx)"\
                "\ncan be used to personalise different parts of your box. [/]\n"
    paragraph = """
    [bright_white]The colour scheme of your box can be changed in the
    Preferences page once logged in. A valid colour name or a hex-value (#xxxxxx)
    can be used to personalise different parts of your box. [/]
    
    """

    console.print((Align(f"""[{main_style}]
    █▀█ █▀█ █▀▀ █▀▀ █▀▀ █▀█ █▀▀ █▄ █ █▀▀ █▀▀ █▀
    █▀▀ █▀▄ ██▄ █▀  ██▄ █▀▄ ██▄ █ ▀█ █▄▄ ██▄ ▄█[/]\n""", align="center", )))
    console.print((Align(paragraph, align="center")))
    help_navigation("Pref", user)
