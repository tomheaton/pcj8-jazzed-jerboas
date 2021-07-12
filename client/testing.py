from prompt_toolkit.shortcuts import input_dialog
from prompt_toolkit import Application
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import HSplit, VSplit, Window
from prompt_toolkit.widgets import TextArea, Frame
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from rich.text import Text
# from rich import print
# # from rich.layout import Layout
# from rich.console import Console
# from rich.panel import Panel
# from rich.align import Align

# console: Console = Console()
main_title: Text = Text.assemble(
    ("""$$$$$$$$\\ $$\\
\\__$$  __|$$ |
   $$ |   $$$$$$$\\   $$$$$$\\
   $$ |   $$  __$$\\  \\____$$\\
   $$ |   $$ |  $$ | $$$$$$$ |
   $$ |   $$ |  $$ |$$  __$$ |
   $$ |   $$ |  $$ |\\$$$$$$$ |
   \\__|   \\__|  \\__| \\_______|\n""",
     "bold magenta"),
    ("""$$$$$$$\\
$$  __$$\\
$$ |  $$ | $$$$$$\  $$\   $$\\
$$$$$$$\ |$$  __$$\ \$$\ $$  |
$$  __$$\ $$ /  $$ | \$$$$  /
$$ |  $$ |$$ |  $$ | $$  $$<
$$$$$$$  |\$$$$$$  |$$  /\$$\\
\\_______/  \\______/ \\__/  \\__|""",
     "bold cyan")
)

buffer1 = Buffer()
buffer2 = Buffer()
# text = input_dialog(
#     title='Input dialog example',
#     text='Please type your name:').run()


def accept(buff):
    """ Accept the content of the default buffer. This is called when
    the validation succeeds. """
    app.exit(result=buff.document.text)
    return True  # Keep text, we call 'reset' later on.


inputArea1 = Window(content=BufferControl(buffer=buffer1))
inputArea2 = Window(content=BufferControl(buffer=buffer2))


content_container = VSplit([

    inputArea1,
    inputArea2,
    TextArea(text=str(main_title), wrap_lines=False, read_only=True),
])

layout = Layout(content_container)

kb = KeyBindings()


@kb.add('tab')
def _(event):
    ip = event.app.current_buffer.text


@kb.add('c-q')
def exit_(event):
    """
    Pressing Ctrl-Q will exit the user interface.

    Setting a return value means: quit the event loop that drives the user
    interface and return this value from the `Application.run()` call.
    """
    event.app.exit()


app = Application(layout=layout,
                  key_bindings=kb,
                  full_screen=True,
                  mouse_support=True
                  )
app.run()


# Rich thing
# ip: str = ''
# name: str = ''
# layout: Layout = Layout()

# layout.split_column(
#     Layout(Panel(Align.center(main_title)), name="upper"),
#     Layout(name="lower")
# )

# layout["lower"].split_row(
#     Layout(Panel(f'IP: {ip}'), name="left"),
#     Layout(Panel(f'name: {name}'), name="right"),
# )


# ip = input_dialog(
#     title='Input dialog example',
#     text='Please type the IP:').run()

# name = input_dialog(
#     title='Input dialog example',
#     text='Please type your name:').run()

# layout['left'].update(
#     Panel(f'IP: {ip}')
# )
# layout['right'].update(
#     Panel(f'name: {name}')
# )

# print(layout)
