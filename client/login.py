import utils
import re
import string
import random
import pickle
import time
from utils import User, Preferences, clear
from hashlib import sha256
from rich.prompt import Prompt
from rich.panel import Panel
from rich.console import Console
from rich.text import Text


with open("server\\secrets.pkl", "rb") as fp:
    secrets = pickle.load(fp)


printable_chars = list(string.printable.replace("\n", "").replace(" ", "").replace("    ", ""))

console = Console()


def create_account(username: str, password: str):
    global secrets
    password = hash_pass(password)
    secrets.append(User(username=username, paswrd=password, preferences=Preferences()))
    with open("server\\secrets.pkl", "wb") as fp:
        pickle.dump(secrets, fp)


def sign_up():
    global secrets
    progress_visual = []

    username_status = "working"
    while username_status != "ready":
        clear()
        console.print(Panel(Text.assemble(("Enter a username", "bold purple")),
                      style="bold purple", border_style="bold purple"))

        usernames_taken = [x.username for x in secrets]
        username = Prompt.ask(Text.assemble(("╰→", "bold red")))

        if username in usernames_taken:
            clear()
            console.print(Panel(Text.assemble(("Username already taken", "bold purple")),
                          style="bold red", border_style="bold red"))
            time.sleep(2.1)
            clear()
            continue
        if " " in username:
            clear()
            console.print(Panel(Text.assemble(("Can not have space in username", "bold purple")),
                          style="bold red", border_style="bold red"))
            time.sleep(2.1)
            clear()
            continue
        if len(username) < 4:
            clear()
            console.print(Panel(Text.assemble(("Username must be at least 4 characters long",
                          "bold purple")), style="bold red", border_style="bold red"))
            time.sleep(2.1)
            clear()
            continue

        secrets.append(User(username, "test", Preferences()))

        progress_visual.append(Panel(Text.assemble(("Username ✓", "bold green")),
                               style="bold green", border_style="bold green"))
        progress_visual.append(Text.assemble(("╰→", "bold red"), (username, "none")))
        username_status = "ready"

    password_status = "working"
    while password_status != "ready":
        clear()
        for i in progress_visual:
            console.print(i)

        console.print(Panel(Text.assemble(("Enter a password (1)", "bold cyan")),
                      style="bold cyan", border_style="bold cyan"))
        password = Prompt.ask(Text.assemble(("╰→", "bold red")), password=True)

        # Checks
        if " " in password:
            clear()
            console.print(Panel(Text.assemble(("Can not have space in password", "bold cyan")),
                          style="bold red", border_style="bold red"))
            time.sleep(2.1)
            clear()
            continue
        if len(password) < 8:
            clear()
            console.print(Panel(Text.assemble(("Password must be at least 8 characters long",
                          "bold cyan")), style="bold red", border_style="bold red"))
            time.sleep(2.1)
            clear()
            continue
        if len(password) > 32:
            clear()
            console.print(Panel(Text.assemble(("Password can not be any longer than 32 characters",
                          "bold cyan")), style="bold red", border_style="bold red"))
            time.sleep(2.1)
            clear()
            continue
        if not re.search("[a-z]", password):
            clear()
            console.print(Panel(Text.assemble(("Password must contain at least one lowercase character",
                          "bold cyan")), style="bold red", border_style="bold red"))
            time.sleep(2.1)
            clear()
            continue
        if not re.search("[A-Z]", password):
            clear()
            console.print(Panel(Text.assemble(("Password must contain at least one uppercase character",
                          "bold cyan")), style="bold red", border_style="bold red"))
            time.sleep(2.1)
            clear()
            continue
        if not re.search("[A-Z]", password):
            clear()
            console.print(Panel(Text.assemble(("Password must contain at least one uppercase character",
                          "bold cyan")), style="bold red", border_style="bold red"))
            time.sleep(2.1)
            clear()
            continue
        if not re.search("[0-9]", password):
            clear()
            console.print(Panel(Text.assemble(("Password must contain at least one digit", "bold cyan")),
                          style="bold red", border_style="bold red"))
            time.sleep(2.1)
            clear()
            continue
        for i in password:
            if i not in printable_chars:
                clear()
                console.print(Panel(Text.assemble(("Password can only contain letters from the ASCII table",
                              "bold cyan")), style="bold red", border_style="bold red"))
                time.sleep(2.1)
                clear()
                continue

        console.print(Panel(Text.assemble(("Repeat password (2)", "bold cyan")),
                      style="bold cyan", border_style="bold cyan"))
        password2 = Prompt.ask(Text.assemble(("╰→", "bold red")), password=True)

        if password != password2:
            clear()
            console.print(Panel(Text.assemble(("Passwords did not match", "bold cyan")),
                          style="bold red", border_style="bold red"))
            time.sleep(2.1)
            clear()
            continue

        progress_visual.append(Panel(Text.assemble(("Password ✓", "bold green")),
                               style="bold green", border_style="bold green"))
        progress_visual.append(Text.assemble(("╰→", "bold red"), ("HIDDEN", "bold yellow")))
        password_status = "ready"
    clear()
    for i in progress_visual:
        console.print(i)


def add_salt(hash_no_salt):
    for i in range(9):
        hash_no_salt += random.choice(printable_chars)
    return hash_no_salt


def remove_salt(hash_and_salt):
    back_hash_removed = hash_and_salt[:-9]
    return back_hash_removed


def hash_pass(passwrd: str):
    hashed = sha256(bytes(passwrd, "utf8")).hexdigest()
    return add_salt(hashed)


def login():
    choice = utils.make_style_prompt(choices=["Log in", "Sign up"], prompt_msg="Please log-in/sign up:",
                                     main_style="bold purple", frame_border_style="bold cyan", frame_style="bold red")
    if choice == "Log in":
        pass
    if choice == "Sign up":
        sign_up()


login()