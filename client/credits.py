from utils import clear

from time import sleep

from rich.live import Live
from rich.table import Table
from rich.console import Console, RenderGroup
from rich import print
from rich.align import Align
from rich.text import Text
from rich.panel import Panel

console: Console = Console()

height: list = ['bottom', 'middle', 'top']

team_name: list = [
    Text.assemble((r":                |$$$$$$$$| |$$| |$$| |$$$$$$|               :", 'bold purple'), justify='center'),
    Text.assemble((r":                   |$$|    |$$| |$$| |$|                    :", 'bold purple'), justify='center'),
    Text.assemble((r":                   |$$|    |$$$$$$$| |$$$$|                 :", 'bold purple'), justify='center'),
    Text.assemble((r":                   |$$|    |$$| |$$| |$|                    :", 'bold purple'), justify='center'),
    Text.assemble((":                   |$$|    |$$| |$$| |$$$$$$|               :\n", 'bold purple'), justify='center'),

    Text.assemble((r":          |$| |$$$$$| |$$$$$| |$$$$$| |$$$$$| |$$$$$\       :", 'bold magenta'), justify='center'),
    Text.assemble((r":          |$| |$$ $$|    /$$/    /$$/ |$|     |$$| \$\      :", 'bold magenta'), justify='center'),
    Text.assemble((r":          |$| |$$$$$|   /$$/    /$$/  |$$$|   |$$| |$|      :", 'bold magenta'), justify='center'),
    Text.assemble((r":       ___|$| |$| |$|  /$$/    /$$/   |$|     |$$| /$/      :", 'bold magenta'), justify='center'),
    Text.assemble((":      |$$$$$| |$| |$| |$$$$$| |$$$$$| |$$$$$| |$$$$$/       :\n", 'bold magenta'), justify='center'),

    Text.assemble((r":    |$| |$$$$$| |$$$$$\  |$$$$\   /$$$$$\  |$$$$$|  /$$$$$| :", 'bold purple'), justify='center'),
    Text.assemble((r":    |$| |$|     |$$  $$| |$  $$| |$$   $$| |$$ $$| |$$\     :", 'bold purple'), justify='center'),
    Text.assemble((r":    |$| |$$$|   |$$$$$/  |$$$$/  |$$   $$| |$$$$$|  \$$$$$\ :", 'bold purple'), justify='center'),
    Text.assemble((r": ___|$| |$|     |$| \$\  |$  $$\ |$$   $$| |$| |$|      /$$|:", 'bold purple'), justify='center'),
    Text.assemble((r":|$$$$$| |$$$$$| |$|  \$\ |$$$$$/  \$$$$$/  |$| |$|  |$$$$$/ :", 'bold purple'), justify='center'),
]

jazzed_jerboas: list = ['[green]tomheaton[/]', '[purple]MikeNoCap[/]', '[purple]HiPeople21[/]',
                        '[purple]TahU28[/]', '[purple]ryoflux[/]', '[purple]b-a-b-i-s[/]']

message: list = ['Placeholder']

# team_name: list = [Text.assemble((
#     r"""
# :                |$$$$$$$$| |$$| |$$| |$$$$$$|               :
# :                   |$$|    |$$| |$$| |$|                    :
# :                   |$$|    |$$$$$$$| |$$$$|                 :
# :                   |$$|    |$$| |$$| |$|                    :
# :                   |$$|    |$$| |$$| |$$$$$$|               :
#    """,
#     'bold purple'), justify='center'), Text.assemble((
#         r"""
# :          |$| |$$$$$| |$$$$$| |$$$$$| |$$$$$| |$$$$$\       :
# :          |$| |$$ $$|    /$$/    /$$/ |$|     |$$| \$\      :
# :          |$| |$$$$$|   /$$/    /$$/  |$$$|   |$$| |$|      :
# :       ___|$| |$| |$|  /$$/    /$$/   |$|     |$$| /$/      :
# :      |$$$$$| |$| |$| |$$$$$| |$$$$$| |$$$$$| |$$$$$/       :
# """, 'bold magenta'), justify='center'), Text.assemble((
#             r"""
# :    |$| |$$$$$| |$$$$$\  |$$$$\   /$$$$$\  |$$$$$|  /$$$$$| :
# :    |$| |$|     |$$  $$| |$  $$| |$$   $$| |$$ $$| |$$\     :
# :    |$| |$$$|   |$$$$$/  |$$$$/  |$$   $$| |$$$$$|  \$$$$$\ :
# : ___|$| |$|     |$| \$\  |$  $$\ |$$   $$| |$| |$|      /$$|:
# :|$$$$$| |$$$$$| |$|  \$\ |$$$$$/  \$$$$$/  |$| |$|  |$$$$$/ :
# """, 'bold purple'), justify='center')]

new_line = '\n'


# def print_credits(to_print: list[str]) -> None:
#     height = console.height
#     rule = "[purple]--------------------[/purple][magenta]This was built by:[/magenta][purple]--------------------[/purple]"
#     with console.screen() as screen:
#         for i in range(height + len(to_print)):
#             for_printing: list[str] = []
#             for j in to_print[:height - i]:
#                 for_printing.append(j)
#             if i == 0:
#                 text: Text = Align.center(
#                     Text.from_markup(
#                         f"{new_line * height}", justify="center"),
#                 )
#             elif i == 1:
#                 text: Text = Align.center(
#                     Text.from_markup(
#                         f"{new_line * height}{rule}", justify="center"),

#                 )
#             else:
#                 text: Text = Align.center(
#                     Text.from_markup(
#                         f"{new_line * height}{rule}\n{for_printing}", justify="center"),
#                 )
#             screen.update(Panel(text))
#             sleep(0.5)


# args: list = []
# for i in team_name:
#     args.append(i)
# for i in jazzed_jerboas:
#     args.append(i)
# for i in message:
#     args.append(i)
# print_credits(args)

def credits() -> None:
    with console.screen() as screen:
        rule: str = '[purple]--------------------[/purple][magenta]This was built by:[/magenta][purple]--------------------[/purple]'
        text: Text = Align.center(
            Text.from_markup(
                f"{rule}", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(0.5)

        text: Text = Align.center(
            Text.from_markup(
                f"{rule}\n{team_name[0]}", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(0.5)

        text: Text = Align.center(
            Text.from_markup(
                f"{rule}\n{new_line.join([str(i) for i in team_name[:2]])}", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(0.5)

        text: Text = Align.center(
            Text.from_markup(
                f"{rule}\n{new_line.join([str(i) for i in team_name[:3]])}", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(0.5)

        text: Text = Align.center(
            Text.from_markup(
                f"{rule}\n{new_line.join([str(i) for i in team_name[:4]])}", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(0.5)

        text: Text = Align.center(
            Text.from_markup(
                f"{rule}\n{new_line.join([str(i) for i in team_name[:5]])}", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(0.5)

        text: Text = Align.center(
            Text.from_markup(
                f"{rule}\n{new_line.join([str(i) for i in team_name[:6]])}", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(0.5)

        text: Text = Align.center(
            Text.from_markup(
                f"{rule}\n{new_line.join([str(i) for i in team_name[:7]])}", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(0.5)

        text: Text = Align.center(
            Text.from_markup(
                f"{rule}\n{new_line.join([str(i) for i in team_name[:8]])}", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(0.5)

        text: Text = Align.center(
            Text.from_markup(
                f"{rule}\n{new_line.join([str(i) for i in team_name[:9]])}", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(0.5)

        text: Text = Align.center(
            Text.from_markup(
                f"{rule}\n{new_line.join([str(i) for i in team_name[:10]])}", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(0.5)

        text: Text = Align.center(
            Text.from_markup(
                f"{rule}\n{new_line.join([str(i) for i in team_name[:11]])}", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(0.5)

        text: Text = Align.center(
            Text.from_markup(
                f"{rule}\n{new_line.join([str(i) for i in team_name[:12]])}", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(0.5)

        text: Text = Align.center(
            Text.from_markup(
                f"{rule}\n{new_line.join([str(i) for i in team_name[:13]])}", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(0.5)

        text: Text = Align.center(
            Text.from_markup(
                f"{rule}\n{new_line.join([str(i) for i in team_name[:14]])}", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(0.5)

        text: Text = Align.center(
            Text.from_markup(
                f"{rule}\n{new_line.join([str(i) for i in team_name])}", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(0.5)

        text: Text = Align.center(
            Text.from_markup(
                f"{rule}\n{new_line.join([str(i) for i in team_name])}\n{jazzed_jerboas[0])", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(0.5)

        text: Text = Align.center(
            Text.from_markup(
                f"{rule}\n{new_line.join([str(i) for i in team_name])}\n{new_line.join([str(i) for i in jazzed_jerboas[:2])", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(0.5)

        text: Text = Align.center(
            Text.from_markup(
                f"{rule}\n{new_line.join([str(i) for i in team_name])}\n{new_line.join([str(i) for i in jazzed_jerboas[:3])", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(0.5)

        text: Text = Align.center(
            Text.from_markup(
                f"{rule}\n{new_line.join([str(i) for i in team_name])}\n{new_line.join([str(i) for i in jazzed_jerboas[:4])", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(0.5)

        text: Text = Align.center(
            Text.from_markup(
                f"{rule}\n{new_line.join([str(i) for i in team_name])}\n{new_line.join([str(i) for i in jazzed_jerboas[:5])", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(0.5)

        text: Text = Align.center(
            Text.from_markup(
                f"{rule}\n{new_line.join([str(i) for i in team_name])}\n{new_line.join([str(i) for i in jazzed_jerboas)", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(0.5)

        text: Text = Align.center(
            Text.from_markup(
                f"{rule}\n{new_line.join([str(i) for i in team_name])}\n{new_line.join([str(i) for i in jazzed_jerboas)", justify="center"),
            vertical=height[1],
        )
        screen.update(Panel(text))
        sleep(0.5)

        text: Text = Align.center(
            Text.from_markup(
                f"{rule}\n{new_line.join([str(i) for i in team_name])}\n{new_line.join([str(i) for i in jazzed_jerboas)", justify="center"),
            vertical=height[2],
        )
        screen.update(Panel(text))
        sleep(0.5)

        text: Text = Align.center(
            Text.from_markup(
                f"{rule}\n{new_line.join([str(i) for i in team_name])}\n{new_line.join([str(i) for i in jazzed_jerboas)", justify="center"),
            vertical=height[2],
        )
        screen.update(Panel(text))
        sleep(0.5)

        text: Text = Align.center(
            Text.from_markup(
                f"{jazzed_jerboas[4]}\n{jazzed_jerboas[5]}", justify="center"),
            vertical=height[2],
        )
        screen.update(Panel(text))
        sleep(0.5)

        text: Text = Align.center(
            Text.from_markup(
                f"{jazzed_jerboas[5]}", justify="center"),
            vertical=height[2],
        )
        screen.update(Panel(text))
        sleep(0.5)

        text: Text = Align.center(
            Text.from_markup(
                f"", justify="center"),
            vertical=height[2],
        )
        screen.update(Panel(text))
        sleep(0.5)

        text: Text = Align.center(
            Text.from_markup(
                f"{message}", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(1)

        text: Text = Align.center(
            Text.from_markup(
                f"{message}", justify="center"),
            vertical=height[1],
        )
        screen.update(Panel(text))
        sleep(1)

        text: Text = Align.center(
            Text.from_markup(
                f"{message}", justify="center"),
            vertical=height[2],
        )
        screen.update(Panel(text))
        sleep(1)

        text: Text = Align.center(
            Text.from_markup(
                f"", justify="center"),
            vertical=height[2],
        )
        screen.update(Panel(text))
        sleep(0.5)


credits()
