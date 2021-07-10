from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text

console: Console = Console()


<< << << < HEAD
def make_style_prompt(choices: list, default: str = None, main_style="none", frame_style="none", frame_border_style="none"):


== == == =
def make_style_prompt(choices: list, default: str = None, prompt_msg: str = "What would you like to do:", main_stlye="none", frame_style="none", frame_border_style="none"):


>>>>>> > aa90e8818fe14e5d8a283e244645f0beb968518f
 """
    Prompts user in a cool way and retrieves what the user picked.

    :choices: A list of choices.
    :default: The value that gets returned if user doesn't type anything in.
<<<<<<< HEAD
=======
    :prompt_msg: The message being sent before the options. Example: What is your favourite food:
>>>>>>> aa90e8818fe14e5d8a283e244645f0beb968518f

    Styling:
    :main_style: The main theme/color of the prompt.
    :frame_style: The theme/color for the text in the panels.
    :frame_border_style: The theme/color for the frame in the panels.
    Styling formats should be rich-styles.

    returns the value that the user picked.
    """

  choices = [str(i) for i in choices]
   if default is not None:
        default_index = str(choices.index(default)+1)  # Get index of default so it can be set to the default choice.
    else:
        default_index = None

    choices_styled = []
    c = 0
    for i in choices:
        c += 1
        choices_styled.append(Panel(str(c)+". "+i, style=frame_style, border_style=frame_border_style))

    console.print(Panel(Markdown("**Would you like to:**"), style=main_style, border_style=main_style))
    for i in choices_styled:
        console.print(i)

    choice_index = Prompt.ask(Text.assemble(("╰>", main_style)), choices=[
                              str(x) for x in range(1, c+1)], default=default_index)
    choice_index = int(choice_index)
    return choices[choice_index-1]
