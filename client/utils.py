import os

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text

console: Console = Console()


class Preferences:
    """
    This needs to be passed onto the 'User' class as it sets the default preferences:
    'sampleuser = User("samplename", "password", default_preference)'

    default_preference = {
        "Name Colour" : "bold cyan",
        "Message Colour" : "bold white",
        "Border Colour" : "bold magenta"
    }

    To change the preference, this is used:
    'sampleuser.preferences = Preferences.settings(sampleuser.preferences)'
    *Note: this only allows for one settings to be changed, so a while loop would need
    to be used to allow multiple settings be to changed.
    """

    def __init__(self):
        self.preference_dict = default_preference = {
        "Name Colour" : "bold cyan",
        "Message Colour" : "bold white",
        "Border Colour" : "bold magenta"
        }


    def template_message(self) -> None:
        """
        Function which prints out a preview of how the users box is going to look.
        """
        console.print(Panel("This is a template message.", title=("["+self["Name Colour"]+"]") + "Title" + "[/]",
                      border_style=self["Border Colour"], style=self["Message Colour"], width=25, padding=1, title_align="left"))

    def settings(self):
        """
        Function which allows the user to change thier settings. Allows hex and named
        colour values and returns then updated preference.
        """
        Preferences.template_message(self)
        val_to_be_changed: str = Prompt.ask("\n🖌️    What would you like to change?    ", choices=[
                                            "Border Colour", "Name Colour", "Message Colour", "BACK"])

        if val_to_be_changed == "BACK":
            raise GoBack

        else:
            while True:
                colour: str = Prompt.ask("🎨   Enter the name or hex value of your desired colour   ")
                try:
                    test: str = console.print("", style=colour)
                except:
                    console.print("❌   Please enter a valid colour!\n")
                else:
                    previous_setting: str = self[val_to_be_changed]
                    self[val_to_be_changed] = "bold " + str(colour)
                    console.print("✔️   Updated successfully!\n")
                    return self


class User:
    def __init__(self, username: str, paswrd: str, preferences: Preferences):
        self.username = username
        self.hashed_pass = paswrd
        self.preferences = preferences
        self.friends = []



class GoBack(Exception):
    pass

def make_style_prompt(choices: list, default: str = None, prompt_msg: str = "Would you like to:", main_style: str = "none",
                      frame_style: str = "none",
                      frame_border_style: str = "none") -> str:
    """
    Prompts user in a cool way and retrieves what the user picked.

    :param choices: A list of choices.
    :param default: The value that gets returned if user doesn't type anything in.
    :param prompt_msg: The message being printed before the choices.
    :param main_style: The main theme/color of the prompt.
    :param frame_style: The theme/color for the text in the panels.
    :param frame_border_style: The theme/color for the frame in the panels.
    :return: str value of final style choice the user selected.
    """
    choices = [str(i) for i in choices]
    if default is not None:
        # Get index of default so it can be set to the default choice.
        default_index = str(choices.index(default) + 1)
    else:
        default_index = None

    choices_styled = []
    c = 0
    for i in choices:
        c += 1
        choices_styled.append(Panel(f"{c}. {i}", style=frame_style, border_style=frame_border_style))

    console.print(Panel(Markdown("**" + prompt_msg + "**"), style=main_style, border_style=main_style))
    for i in choices_styled:
        console.print(i)

    choice_index = Prompt.ask(Text.assemble(("╰>", main_style)), choices=[str(x) for x in range(1, c + 1)],
                              default=default_index)
    choice_index = int(choice_index)
    return choices[choice_index - 1]


def clear() -> int:
    """
    Clears terminal
    """
    return os.system('cls' if os.name == 'nt' else 'clear')
