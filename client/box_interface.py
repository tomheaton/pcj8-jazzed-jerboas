import keyboard
import time
import sys
import random
from utils import clear
from utils import GoBack
from utils import User
from rich import print
from rich.console import Console
from rich.align import Align
from rich.prompt import Prompt
from rich.panel import Panel
from rich.layout import Layout
from rich.text import Text

"""
'id, password, size, stype = create_box_tui(User, available_session_data)'
To run the create_box_tui - the variables can be changed (i.e. to a list), by 
returning a different value at lines 322 and 352. To be called on main.py, hover_on = 1

'join_box_tui(User, available_session_data)'
To run the join_box_tui - no variables returned, as the session id's, from available_session_data
is used to print and select a valid session. May need to be edited to return session_id if needed.
To be called on main.py, hover_on = 2
"""

console = Console()

"""
This will be passed into the join_box_tui() function when called. List(?) to be filled
from the database. After database is created, it needs to be implemented into this code.
currently a temp variable
"""

available_session_data = [[1234]]

global layout, colours, private_box_art, public_box_art

colour = {
    "box_default": "bold white",
    "box_hover": "bold yellow"
}

public_box_art = ("""
          +--+
          |  |
          |  |
          |  |
          |  |
          |  |
        +-+  +-+
   +-----\    /-------+
  /|      \  /       /|
 / |       \/       / |  
+--+---------------+  |
|                  |  |
|    PUBLIC BOX    |  +
|                  | /
+------------------+/
""")

private_box_art = ("""
         .------.
        / .----. \  
       _| |____| |_
     .'    ____    '.
     |    /    \    |  
     |    \____/    |
     '.____________.' 
   +------------------+
  /                  /|
 /                  / |  
+--+---------------+  |
|                  |  |
|    PRIVATE BOX   |  +
|                  | /
+------------------+/
""")

# Splitting the console to place the boxes side by side
layout = Layout()
layout.visible = True
layout.split_column(
    Layout(name="title"),
    Layout(name="boxes"),
    Layout(name="screen")
)

layout["title"].size = 5
layout["boxes"].size = 16
layout["screen"].size = 5

layout["boxes"].split_row(
    Layout(name="left"),
    Layout(name="right")
)


# ---TEMP FUNCTIONS - TO BE REPLACED
def is_already_an_id(session_id):
    import random
    return random.choice([True, False])


def is_correct_password(password, session_id):
    import random
    return random.choice([True, False])
# ---------------------------------- #


def layout_setup(select: str, text: str):  # DONE
    """
    Creates menu layout, with ASCII box art and navigation help text.
    """
    global layout, private_box_art, public_box_art, colour

    clear()
    layout["title"].update(Align(text, align="center"))
    layout["screen"].update(
        "\n\n[bold white]!   Use [bold magenta] right arrow[/] or [bold magenta]left arrow[/] to select a box.[/]"
        + "\n[bold white]!   [bold magenta]ENTER[/] to confirm your choice.[/]"
        + "\n[bold white]!   Press [bold magenta]BACKSPACE[/] to return to Menu.[/]")

    if select == "left":
        layout["right"].update(Align(Text(f"{private_box_art}", style=colour["box_default"]), align="center"))
        layout["left"].update(Align(Text(f"{public_box_art}", style=colour["box_hover"]), align="center"))
    else:
        layout["right"].update(Align(Text(f"{private_box_art}", style=colour["box_hover"]), align="center"))
        layout["left"].update(Align(Text(f"{public_box_art}", style=colour["box_default"]), align="center"))

    console.print(layout)


def tui_navigation(select: str, available_session_data):  # DONE
    """
    Returns which box is selected.
    """

    # Adds delay between key presses
    time.sleep(0.2)
    while True:
        if keyboard.is_pressed("backspace"):
            raise GoBack

        if keyboard.is_pressed("left_arrow"):
            if select != "left":
                select = "left"
                return select
            continue

        if keyboard.is_pressed("right_arrow"):
            if select != "right":
                select = "right"
                return select
            continue

        if keyboard.is_pressed("enter"):
            if select == "left":
                select = "public"
                return select

            elif select == "right":
                select = "private"
                return select


def create_session_id():  # DONE
    """
    Adds leading 0's if necessary and returns a unique session_id,
    by comparing it to taken id's.
    """
    num: int = random.randint(1, 1000)
    session_id: str = ("0" * (4 - len(str(num)))) + str(num)
    if is_already_an_id(session_id):
        return create_session_id()

    return session_id


def enter_session_id(prompt: str, alignment: str, password_prompt):  # IN PROGRESS
    """
    Prompts user to enter a valid session ID
    """
    given_id = console.input(prompt)

    if given_id.lower() == "back":
        return join_box_tui(User, available_session_data)

    elif (len(given_id) == 4) and (given_id.isdigit() is True):
        if is_already_an_id(int(given_id)):
            if password_prompt:
                enter_password(password_prompt, given_id)

            else:
                """
                Needs to be redirected to a chat room
                """
                console.print(Align("\n✔️   Joining ThaBox...", align=alignment))
                time.sleep(0.5)
                clear()
                sys.exit()

        else:
            console.print(Align("❌   The room you are trying to join doesn't exist\n", align=alignment))
            time.sleep(0.5)
            return enter_session_id(prompt, alignment, password_prompt)

    else:
        console.print(Align("❌   Session ID's can only be 4 digit numbers!\n", align=alignment))
        time.sleep(0.5)
        return enter_session_id(prompt, alignment, password_prompt)


def enter_password(prompt, session_id):  # IN PROGRESS
    """
    Checks if entered password is correct.
    """
    time.sleep(0.3)  # Input delay
    given_password = console.input(prompt)
    if is_correct_password(given_password, session_id):
        """
        Needs to be redirected to a chat room
        """
        console.print(Align("\n✔️   Joining ThaBox...", align="center"))
        time.sleep(1)
        clear()
        sys.exit()

    else:
        console.print(Align("❌   Incorrect Password!", align="center"))
        return enter_password(prompt, session_id)


def enter_room_size(user):  # DONE
    """
    Validates the user input, so they enter a correct size, and 
    returns the room_size.
    """
    size = console.input(" " * ((console.width // 2) - 14) + "[bold red]Enter room size (2 - 6):   [/]")

    if size.lower() == "back":
        return create_box_tui(user, available_session_data)

    if size == "2" or size == "3" or size == "4" or size == "5" or size == "6":
        return str(size)

    else:
        console.print(Align("❌   Enter a valid number!\n", align="center"))
        return enter_room_size(user)


def join_box_tui(user: User, available_session_data, select="left"):  # IN PROGRESS
    if select == "public":
        """
        PLAN - print only 4 session at once. Users can navigate this using arrow keys.
        They type the session id of the room they wan to join, and then they join the room.
        DATA NEEDED - public session id, max user count for the room, current amount of users
        in the room. 
        """
        clear()

        console.print(Align("\n█▀█ █ █ █▄▄ █   █ █▀▀   █▄▄ █▀█ ▀▄▀ █▀▀ █▀\n"
                            + "█▀▀ █▄█ █▄█ █▄▄ █ █▄▄   █▄█ █▄█ █ █ ██▄ ▄█\n",
                            align="center"),
                      style=user.preferences.preference_dict["Border Colour"])

        console.print(Align(Panel("Room Name = \nSession ID = \nUsers = ", expand=False), align="center"),
                      style="bold white")
        console.print(
            "\n\n[bold white]!   Use [bold magenta] right arrow[/] or [bold magenta]left arrow[/] to find more rooms.[/]\n"
            + "[bold white]!   [bold magenta]SPACE[/] to type in a session ID.[/]\n"
            + "[bold white]!   Press [bold magenta]BACKSPACE[/] to go back.[/]")

        # Functionality of other keys needs to be implemented.
        time.sleep(0.2)
        while True:
            if keyboard.is_pressed("backspace"):
                select = "left"
                return join_box_tui(user, available_session_data, select)

            if keyboard.is_pressed("space"):
                console.print()
                enter_session_id("[bold red]>   Enter the session ID or type 'BACK' to go back:[/]   ", "left", False)

            if keyboard.is_pressed("left_arrow"):
                pass

            if keyboard.is_pressed("right_arrow"):
                pass

    elif select == "private":
        clear()
        console.print(Align("\n█▀█ █▀█ █ █ █ ▄▀█ ▀█▀ █▀▀   █▄▄ █▀█ ▀▄▀\n"
                            + "█▀▀ █▀▄ █ ▀▄▀ █▀█  █  ██▄   █▄█ █▄█ █ █\n", align="center"),
                      style=user.preferences.preference_dict["Border Colour"])

        console.print(Align("\nType [bold magenta]BACK[/] in the Session ID field to go back.\n", align="center"))

        enter_session_id((" " * ((console.width // 2) - 14) + "[bold red]Enter the session ID:[/]   "), "center",
                         (str("\n" + " " * ((console.width // 2) - 17) + "[bold red]Enter the room password:[/]   ")))
    else:
        """
        JOIN BOX MENU
        """
        layout_setup(select,
                     f"[{user.preferences.preference_dict['Border Colour']}]\n\n  █ █▀█ █ █▄ █   █▄▄ █▀█ ▀▄▀\n█▄█ █▄█ █ █ ▀█   █▄█ █▄█ █ █[/]")  # select, "JOIN BOX"
        select = tui_navigation(select, available_session_data)
        join_box_tui(user, available_session_data, select)


def create_box_tui(user: User, available_session_data, select="left"):
    """
    Allows user to create thier own box - can set the room_size
    and add a password, which are both returned along with a random,
    unique session id.
    """

    if select == "public":
        clear()
        public_session_id = create_session_id()

        console.print(Align("\n█▄▄ █▀█ ▀▄▀   █▀ █▀▀ ▀█▀ ▀█▀ █ █▄ █ █▀▀ █▀\n"
                            + "█▄█ █▄█ █ █   ▄█ ██▄  █   █  █ █ ▀█ █▄█ ▄█\n", align="center"),
                      style=user.preferences.preference_dict['Border Colour'])
        console.print(Align("Type [bold magenta]BACK[/] in any of the fields to go back.\n", align="center"))
        console.print(Align(f"[bold red]Session ID:[/]   {public_session_id}", align="center"))

        room_size = enter_room_size(user)

        console.print(Align("\n✔️   Creating ThaBox...", align="center"))
        time.sleep(0.5)

        server_type = select
        password = False

        return user, public_session_id, password, room_size, server_type

    elif select == "private":
        clear()
        private_session_id = create_session_id()

        console.print(Align("\n█▄▄ █▀█ ▀▄▀   █▀ █▀▀ ▀█▀ ▀█▀ █ █▄ █ █▀▀ █▀\n"
                            + "█▄█ █▄█ █ █   ▄█ ██▄  █   █  █ █ ▀█ █▄█ ▄█\n", align="center"),
                      style=user.preferences.preference_dict['Border Colour'])
        console.print(Align("Type [bold magenta]BACK[/] in any of the fields to go back.\n", align="center"))
        console.print(Align(f"[bold red]Session ID:[/]   {private_session_id}", align="center"))

        while True:
            time.sleep(0.2)
            password = console.input(" " * ((console.width // 2) - 12) + "[bold red]Create a Password:   [/]")
            if password.lower() == "back":
                return create_box_tui(user, available_session_data)
            elif password == "":
                console.print(Align("❌   Password can't be blank!\n", align="center"))
            elif " " in password:
                console.print(Align("❌   Password can't have spaces!\n", align="center"))
            elif len(password) < 8:
                console.print(Align("❌   Password must have at least 8 characters!\n", align="center"))

            else:
                room_size = enter_room_size(user)
                break

        console.print(Align("\n✔️   Creating ThaBox...", align="center"))
        time.sleep(0.5)

        server_type = select
        return user, private_session_id, password, room_size, server_type

    else:
        """
        CREATE BOX MENU
        """
        layout_setup(select,
                     f"[{user.preferences.preference_dict['Border Colour']}]\n\n█▀▀ █▀█ █▀▀ ▄▀█ ▀█▀ █▀▀   █▄▄ █▀█ ▀▄▀\n█▄▄ █▀▄ ██▄ █▀█  █  ██▄   █▄█ █▄█ █ █[/]")  # select, "CREATE BOX"
        select = tui_navigation(select, available_session_data)
        return create_box_tui(user, available_session_data, select)


def chat_rooms_scroll():
    what_to_do = Prompt.ask(Text.assemble(("1: Scroll up\n", "bold cyan"), ("2: Scroll down\n", "bold cyan"),
                                          ("3: Select\n", "bold purple")), choices=["1", "2", "3"], default="3")
