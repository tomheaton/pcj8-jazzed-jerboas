from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
console: Console = Console()

def make_style_prompt(choices: list, default: str = None, prompt_msg: str = "What would you like to do:", main_stlye="none", frame_style="none", frame_border_style="none"):
    """
    Prompts user in a cool way and retrieves what the user picked.

    :choices: A list of choices. 
    :default: The value that gets returned if user doesn't type anything in.
    :prompt_msg: The message being sent before the options. Example: What is your favourite food:

    Styling: 
    :main_style: The main theme/color of the prompt.
    :frame_style: The theme/color for the text in the panels.
    :frame_border_style: The theme/color for the frame in the panels.
    Styling formats should be rich-styles.
    
    returns the value that the user picked.
    """
    
    choices = [str(i) for i in choices]
    if default is not None:
        default_index = str(choices.index(default)+1) # Get index of default so it can be set to the default choice.
    else:
        default_index = None
    
    choices_styled = []
    c = 0
    for i in choices:
        c+=1
        choices_styled.append(Panel(str(c)+". "+i, style=frame_style, border_style=frame_border_style))
    
    console.print(Panel(Markdown("**"+prompt_msg+"**"), style=main_stlye, border_style=main_stlye))
    for i in choices_styled:
        console.print(i)
    
    choice_index = Prompt.ask(Text.assemble(("╰>", main_stlye)), choices=[str(x) for x in range(1, c+1)], default=default_index)
    choice_index = int(choice_index)
    return choices[choice_index-1]

