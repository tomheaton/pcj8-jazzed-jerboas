from utils import clear
from utils import GoBack
from utils import User
import keyboard
import time
import sys
import random

from rich import print
from rich.console import Console 
from rich.align import Align
from rich.prompt import Prompt
from rich.panel import Panel
from rich.layout import Layout
from rich.text import Text

console = Console()

#This will be passed into the join_box_tui() function when called. List(?) to be filled
#from the database. After database is created, it needs to be implemented into this code.
#currently a temp variable
available_session_data = [[1234]]


global layout, colours, private_box_art, public_box_art

colour = {
    "box_default": "bold white",
    "box_hover": "bold yellow"
}

private_box_art = ("""
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

public_box_art = ("""
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

#Splitting the cosole to place the boxes side by side
layout = Layout()
layout.visible = True
layout.split_column(
    Layout(name = "title"),
    Layout(name = "boxes"),
    Layout(name = "screen")
)

layout["title"].size = 5
layout["boxes"].size = 16
layout["screen"].size = 5

layout["boxes"].split_row(
    Layout(name="left"),
    Layout(name="right")
)

#---TEMP FUNCTIONS - TO BE REPLACED
def is_already_an_id(x):
    import random
    y = random.choice([True, False])
    return y

def is_correct_password(x):
    import random
    y = random.choice([True, False])
    return y
#----------------------------------

def layout_setup(select, text):
    """
    Creates menu layout, with ASCII box art and navigation help text.
    """

    global layout, private_box_art, public_box_art, colour 
    clear()
    layout["title"].update(Align(text, align = "center"))
    if select == "left":
        layout["right"].update(Align(Text(f"{private_box_art}", style = colour["box_default"]), align = "center"))
        layout["left"].update(Align(Text(f"{public_box_art}", style = colour["box_hover"]), align = "center"))
    else:
        layout["right"].update(Align(Text(f"{private_box_art}", style = colour["box_hover"]), align = "center"))
        layout["left"].update(Align(Text(f"{public_box_art}", style = colour["box_default"]), align = "center"))
    
    layout["screen"].update("\n\n[bold white][bold red]![/]   Use [bold magenta] right arrow[/] or [bold magenta]left arrow[/] to select a box,\n!   [bold magenta]ENTER[/] to confirm your choice\n!   Press [bold magenta]BACKSPACE[/] to return to Menu.[/]")
    console.print(layout)


def tui_navigation(select, available_session_data):
    """
    Returns which box is selected.
    """

    time.sleep(0.2)
    while True:
        if keyboard.is_pressed("backspace"):
            raise GoBack

        if keyboard.is_pressed("left_arrow"):
            select = "left"
            return select

        if keyboard.is_pressed("right_arrow"):
            select = "right"
            return select

        if keyboard.is_pressed("enter"):
            if select == "left":
                select = "private"
                return select

            elif select == "right":
                select = "public"
                return select

    
def join_box_tui(user: User, available_session_data, select="left"):
    if select == "public":
        """
        PLAN - print only 4 session at once. Users can navigate this using arrow keys.
        They type the session id of the room they wan to join, and then they join the room.
        DATA NEEDED - public session id, max user count for the room, current amount of users
        in the room. 
        """
        clear()

        console.print(Align("\n█▀█ █ █ █▄▄ █   █ █▀▀   █▄▄ █▀█ ▀▄▀ █▀▀ █▀\n" + 
                              "█▀▀ █▄█ █▄█ █▄▄ █ █▄▄   █▄█ █▄█ █ █ ██▄ ▄█\n", align = "center"), style = "bold cyan")

        console.print(Align(Panel("Room Name = \nSesion ID = \nUsers = ", expand = False), align = "center"), style = "bold white")
        console.print("\n\n[bold white][bold red]![/]   Use [bold magenta] right arrow[/] or [bold magenta]left arrow[/] to find more rooms\n!   [bold magenta]SPACE[/] to type in a session ID\n!   Press [bold magenta]BACKSPACE[/] to go back.[/]")
        
        #Functionality of other keys needs to be implemented.
        while True:
            if keyboard.is_pressed("backspace"):
                select = "left"
                join_box_tui(User, available_session_data,  select)

            if keyboard.is_pressed("space"):
                given_id = console.input("\n>   [bold red]Enter the session ID:[/]   ")

                if (len(given_id) == 4) and (given_id.isdigit() == True):

                    if is_already_an_id(int(given_id)):
                        """
                        Needs to be redirected to a chat room
                        """
                        console.print(Align("\n✔️   Joining ThaBox...", align = "center"))
                        time.sleep(0.5)
                        clear()
                        sys.exit()
                    
                    else:
                        console.print("❌   The room you are trying to join doesn't exist")
                        time.sleep(2)
                        join_box_tui(User, available_session_data,  select)

                else:
                    console.print("❌   Session ID's can only be 4 digit numbers!")
                    time.sleep(2)
                    join_box_tui(User, available_session_data,  select)
      

    elif select == "private":
        clear()
        console.print(Align("\n█▀█ █▀█ █ █ █ ▄▀█ ▀█▀ █▀▀   █▄▄ █▀█ ▀▄▀\n"+
                              "█▀▀ █▀▄ █ ▀▄▀ █▀█  █  ██▄   █▄█ █▄█ █ █\n", align = "center"), style = "bold cyan")
        console.print(Align("\nType [bold magenta]BACK[/] in the Session ID field to go back.\n", align = "center"))                

        while True:
            time.sleep(0.2)
            given_id = console.input(" " * ((console.width // 2) - 14) + "[bold red]Enter the session ID:[/]   ")
            if given_id.lower() == "back":
                select = "left"
                join_box_tui(User, available_session_data,  select)

            elif (len(given_id) == 4) and (given_id.isdigit() == True):
                    if is_already_an_id(int(given_id)):
                        while True:
                            time.sleep(0.2)
                            given_password = console.input("\n" + " " * ((console.width // 2) - 17) + "[bold red]Enter the room password:[/]   ")
                            
                            if is_correct_password(given_password):
                                """
                                Needs to be redirected to a chat room
                                """
                                console.print(Align("\n✔️   Joining ThaBox...", align = "center"))
                                time.sleep(0.5)
                                clear()
                                sys.exit()
                            
                            else:
                                console.print(Align("❌   Incorrect Password!\n", align = "center"))
                    
                    else:
                        console.print(Align("❌   The room you are trying to join doesn't exist!", align = "center"))                   

            else:
                console.print(Align("❌   Session ID's can only be 4 digit numbers!\n", align = "center"))
        
    else:
        """
        JOIN BOX MENU
        """
        layout_setup(select, "[bold cyan]\n\n  █ █▀█ █ █▄ █   █▄▄ █▀█ ▀▄▀\n█▄█ █▄█ █ █ ▀█   █▄█ █▄█ █ █[/]") #select, "JOIN BOX"
        select = tui_navigation(select, available_session_data)
        join_box_tui(User, available_session_data,  select)


def create_box_tui(user: User, available_session_data, select="left"):
    """
    Allows user to create thier own box - can set the room_size
    and add a password, which are both returned along with a random,
    unique session id.
    """

    if select == "public":
        clear()
        #Creates random session ids, until a unique one is created
        while True:
            public_session_id: int = random.randint(1000,9999)
            if not is_already_an_id(public_session_id):
                break

        console.print(Align("\n█▄▄ █▀█ ▀▄▀   █▀ █▀▀ ▀█▀ ▀█▀ █ █▄ █ █▀▀ █▀\n"+
                              "█▄█ █▄█ █ █   ▄█ ██▄  █   █  █ █ ▀█ █▄█ ▄█\n", align = "center"), style = "bold cyan")
        console.print(Align("Type [bold magenta]BACK[/] in any of the fields to go back.\n", align = "center"))
        console.print(Align(f"[bold red]Session ID:[/]   {public_session_id}", align = "center"))

        #
        while True:
            room_size = console.input(" " * ((console.width // 2) - 14) + "[bold red]Enter room size (2 - 4):   [/]")
            if room_size.lower() == "back":
                create_box_tui(User, available_session_data)
            elif room_size == "2" or room_size == "3" or room_size == "4":
                break
            else:
                console.print(Align("❌   Enter a valid number!\n", align = "center"))

        console.print(Align("\n✔️   Creating ThaBox...", align = "center"))
        time.sleep(0.5)
        clear()
        return public_session_id, room_size, None

    elif select == "private":
        clear()
        while True:
            public_session_id: int = random.randint(1000,9999)
            if not is_already_an_id(public_session_id):
                break
        
        console.print(Align("\n█▄▄ █▀█ ▀▄▀   █▀ █▀▀ ▀█▀ ▀█▀ █ █▄ █ █▀▀ █▀\n"+
                              "█▄█ █▄█ █ █   ▄█ ██▄  █   █  █ █ ▀█ █▄█ ▄█\n", align = "center"), style = "bold cyan")
        console.print(Align("Type [bold magenta]BACK[/] in any of the fields to go back.\n", align = "center"))
        console.print(Align(f"[bold red]Session ID:[/]   {public_session_id}", align = "center"))
        
        while True:
            password = console.input(" " * ((console.width // 2) - 12) + "[bold red]Create a Password:   [/]")
            if password.lower() == "back":
                create_box_tui(User, available_session_data)
            elif password == "":
                console.print(Align("❌   Password can't be blank!\n", align = "center"))
            elif " " in password:
                console.print(Align("❌   Password can't have spaces!\n", align = "center"))

            else:
                while True:
                    room_size = console.input(" " * ((console.width // 2) - 12) + "[bold red]Enter room size (2 - 4):   [/]")
                    if room_size.lower() == "back":
                        create_box_tui(User, available_session_data)
                    elif room_size == "2" or room_size == "3" or room_size == "4":
                        break
                    else:
                        console.print(Align("❌   Enter a valid number!\n", align = "center"))
                break

        console.print(Align("\n✔️   Creating ThaBox...", align = "center"))
        time.sleep(0.5)
        clear()
        return public_session_id, room_size, password        

    else:
        """
        CREATE BOX MENU
        """
        layout_setup(select, "[bold cyan]\n\n█▀▀ █▀█ █▀▀ ▄▀█ ▀█▀ █▀▀   █▄▄ █▀█ ▀▄▀\n█▄▄ █▀▄ ██▄ █▀█  █  ██▄   █▄█ █▄█ █ █[/]") #select, "CREATE BOX"
        select = tui_navigation(select, available_session_data)
        create_box_tui(User, available_session_data,  select)