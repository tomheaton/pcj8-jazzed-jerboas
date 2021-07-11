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

message: list = ['Placeholder', 'Placeholder', 'Placeholder']

new_line = '\n'


def credits() -> None:
    with console.screen() as screen:
        rule: str = '[purple]--------------------[/purple][magenta]This was built by:[/magenta][purple]--------------------[/purple]'
        clear()
        text: Text = Align.center(
            Text.from_markup(
                f"{rule}", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(0.5)

        for j in range(len(team_name)):
            console.clear()
            text: Text = Align.center(
                Text.from_markup(
                    f"{rule}\n{new_line.join([str(i) for i in team_name[:j]])}", justify="center"),
                vertical=height[0],
            )
            screen.update(Panel(text))
            sleep(0.5)

        for j in range(len(jazzed_jerboas) + 1):
            clear()
            text: Text = Align.center(
                Text.from_markup(
                    f"{rule}\n{new_line.join([str(i) for i in team_name])}\n{new_line.join([str(i) for i in jazzed_jerboas[:j]])}", justify="center"),
                vertical=height[0],
            )
            screen.update(Panel(text))
            sleep(0.5)

        clear()
        text: Text = Align.center(
            Text.from_markup(
                f"{rule}\n{new_line.join([str(i) for i in team_name])}\n{new_line.join([str(i) for i in jazzed_jerboas])}", justify="center"),
            vertical=height[1],
        )
        screen.update(Panel(text))
        sleep(0.5)

        clear()
        text: Text = Align.center(
            Text.from_markup(
                f"{rule}\n{new_line.join([str(i) for i in team_name])}\n{new_line.join([str(i) for i in jazzed_jerboas])}", justify="center"),
            vertical=height[2],
        )
        screen.update(Panel(text))
        sleep(0.5)

        clear()
        text: Text = Align.center(
            Text.from_markup(
                f"\n{new_line.join([str(i) for i in team_name])}\n{new_line.join([str(i) for i in jazzed_jerboas])}", justify="center"),
            vertical=height[2],
        )
        screen.update(Panel(text))
        sleep(0.5)

        for j in range(len(team_name)):
            clear()
            text: Text = Align.center(
                Text.from_markup(
                    f"{new_line.join([str(i) for i in team_name[j:]])}\n{new_line.join([str(i) for i in jazzed_jerboas])}", justify="center"),
                vertical=height[2],
            )
            screen.update(Panel(text))
            sleep(0.5)

        for j in range(len(jazzed_jerboas) + 1):
            clear()
            text: Text = Align.center(
                Text.from_markup(
                    f"{new_line.join([str(i) for i in jazzed_jerboas[j:]])}", justify="center"),
                vertical=height[2],
            )
            screen.update(Panel(text))
            sleep(0.5)

        clear()
        text: Text = Align.center(
            Text.from_markup(
                "", justify="center"),
            vertical=height[2],
        )
        screen.update(Panel(text))
        sleep(0.5)

        for j in range(len(message) + 1):
            clear()
            text: Text = Align.center(
                Text.from_markup(
                    f"{new_line.join([str(i) for i in message[:j]])}", justify="center"),
                vertical=height[0],
            )
            screen.update(Panel(text))
            sleep(1)

        clear()
        text: Text = Align.center(
            Text.from_markup(
                f"{new_line.join([str(i) for i in message])}", justify="center"),
            vertical=height[1],
        )
        screen.update(Panel(text))
        sleep(1)

        for j in range(len(message)):
            clear()
            text: Text = Align.center(
                Text.from_markup(
                    f"{new_line.join([str(i) for i in message[j:]])}", justify="center"),
                vertical=height[2],
            )
            screen.update(Panel(text))
            sleep(1)

        clear()
        text: Text = Align.center(
            Text.from_markup(
                "", justify="center"),
            vertical=height[2],
        )
        screen.update(Panel(text))
        sleep(0.5)
        clear()
