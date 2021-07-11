from prompt_toolkit.shortcuts import input_dialog
from prompt_toolkit import Application
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import HSplit, VSplit
from prompt_toolkit.widgets import TextArea, Frame
from prompt_toolkit.history import InMemoryHistory
from rich.text import Text
from rich import print
from rich.layout import Layout
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

console: Console = Console()
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

ip: str = ''
name: str = ''
# text = input_dialog(
#     title='Input dialog example',
#     text='Please type your name:').run()


# def accept(buff):
#     """ Accept the content of the default buffer. This is called when
#     the validation succeeds. """
#     app.exit(result=buff.document.text)
#     return True  # Keep text, we call 'reset' later on.


# inputArea = TextArea(text="", multiline=False, history=InMemoryHistory(), accept_handler=accept)
# outputArea = TextArea(wrap_lines=False, read_only=True)


# content_container = HSplit([
#     VSplit([
#         TextArea(wrap_lines=False, read_only=True),
#         TextArea(text=str(main_title), wrap_lines=False, read_only=True),
#         TextArea(wrap_lines=False, read_only=True),
#     ]
#     ),
#     inputArea,
#     outputArea
# ])

# layout = Layout(content_container)

# kb = KeyBindings()


# @kb.add('tab')
# def _(event):
#     ip = event.app.current_buffer.text


# app = Application(layout=layout,
#                   key_bindings=kb,
#                   full_screen=True,
#                   mouse_support=True
#                   )
# app.run()

layout: Layout = Layout()

layout.split_column(
    Layout(Panel(Align.center(main_title)), name="upper"),
    Layout(name="lower")
)

layout["lower"].split_row(
    Layout(Panel(f'IP: {ip}'), name="left"),
    Layout(Panel(f'name: {name}'), name="right"),
)


ip = input_dialog(
    title='Input dialog example',
    text='Please type the IP:').run()

name = input_dialog(
    title='Input dialog example',
    text='Please type your name:').run()

layout['left'].update(
    Panel(f'IP: {ip}')
)
layout['right'].update(
    Panel(f'name: {name}')
)

print(layout)
