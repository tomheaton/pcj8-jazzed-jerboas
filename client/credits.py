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

height = ['bottom', 'middle', 'top']

team_name = [Text.assemble((
    r"""
:                |$$$$$$$$| |$$| |$$| |$$$$$$|               :
:                   |$$|    |$$| |$$| |$|                    :
:                   |$$|    |$$$$$$$| |$$$$|                 :
:                   |$$|    |$$| |$$| |$|                    :
:                   |$$|    |$$| |$$| |$$$$$$|               :
   """,
    'bold purple'), justify='center'), Text.assemble((
        r"""
:          |$| |$$$$$| |$$$$$| |$$$$$| |$$$$$| |$$$$$\       :
:          |$| |$$ $$|    /$$/    /$$/ |$|     |$$| \$\      :
:          |$| |$$$$$|   /$$/    /$$/  |$$$|   |$$| |$|      :
:       ___|$| |$| |$|  /$$/    /$$/   |$|     |$$| /$/      :
:      |$$$$$| |$| |$| |$$$$$| |$$$$$| |$$$$$| |$$$$$/       :
""", 'bold magenta'), justify='center'), Text.assemble((
            r"""
:    |$| |$$$$$| |$$$$$\  |$$$$\   /$$$$$\  |$$$$$|  /$$$$$| :
:    |$| |$|     |$$  $$| |$  $$| |$$   $$| |$$ $$| |$$\     :
:    |$| |$$$|   |$$$$$/  |$$$$/  |$$   $$| |$$$$$|  \$$$$$\ :
: ___|$| |$|     |$| \$\  |$  $$\ |$$   $$| |$| |$|      /$$|:
:|$$$$$| |$$$$$| |$|  \$\ |$$$$$/  \$$$$$/  |$| |$|  |$$$$$/ :
""", 'bold purple'), justify='center')]

jazzed_jerboas = ['[green]tomheaton[/]', '[purple]MikeNoCap[/]', '[purple]HiPeople21[/]',
                  '[purple]TahU28[/]', '[purple]ryoflux[/]', '[purple]b-a-b-i-s[/]']

message = 'Placeholder'


def credits() -> None:
    with console.screen() as screen:

        text = Align.center(
            Text.from_markup(
                f"[purple]--------------------[/purple][magenta]This was built by:[/magenta][purple]--------------------[/purple]", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(1)

        text = Align.center(
            Text.from_markup(
                f"[purple]--------------------[/purple][magenta]This was built by:[/magenta][purple]--------------------[/purple]\n{team_name[0]}", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(1)

        text = Align.center(
            Text.from_markup(
                f"[purple]--------------------[/purple][magenta]This was built by:[/magenta][purple]--------------------[/purple]\n{team_name[0]}\n{team_name[1]}", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(1)

        text = Align.center(
            Text.from_markup(
                f"[purple]--------------------[/purple][magenta]This was built by:[/magenta][purple]--------------------[/purple]\n{team_name[0]}\n{team_name[1]}\n{team_name[2]}", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(1)

        text = Align.center(
            Text.from_markup(
                f"[purple]--------------------[/purple][magenta]This was built by:[/magenta][purple]--------------------[/purple]\n{team_name[0]}\n{team_name[1]}\n{team_name[2]}\n{jazzed_jerboas[0]}", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(1)

        text = Align.center(
            Text.from_markup(
                f"[purple]--------------------[/purple][magenta]This was built by:[/magenta][purple]--------------------[/purple]\n{team_name[0]}\n{team_name[1]}\n{team_name[2]}\n{jazzed_jerboas[0]}\n{jazzed_jerboas[1]}", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(1)

        text = Align.center(
            Text.from_markup(
                f"[purple]--------------------[/purple][magenta]This was built by:[/magenta][purple]--------------------[/purple]\n{team_name[0]}\n{team_name[1]}\n{team_name[2]}\n{jazzed_jerboas[0]}\n{jazzed_jerboas[1]}\n{jazzed_jerboas[2]}", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(1)

        text = Align.center(
            Text.from_markup(
                f"{team_name[0]}\n{team_name[1]}\n{team_name[2]}\n{jazzed_jerboas[0]}\n{jazzed_jerboas[1]}\n{jazzed_jerboas[2]}\n{jazzed_jerboas[3]}", justify="center"),
            vertical=height[2],
        )
        screen.update(Panel(text))
        sleep(1)

        text = Align.center(
            Text.from_markup(
                f"{team_name[1]}\n{team_name[2]}\n{jazzed_jerboas[0]}\n{jazzed_jerboas[1]}\n{jazzed_jerboas[2]}\n{jazzed_jerboas[3]}\n{jazzed_jerboas[4]}", justify="center"),
            vertical=height[2],
        )
        screen.update(Panel(text))
        sleep(1)

        text = Align.center(
            Text.from_markup(
                f"{team_name[2]}\n{jazzed_jerboas[0]}\n{jazzed_jerboas[1]}\n{jazzed_jerboas[2]}\n{jazzed_jerboas[3]}\n{jazzed_jerboas[4]}\n{jazzed_jerboas[5]}", justify="center"),
            vertical=height[2],
        )
        screen.update(Panel(text))
        sleep(1)

        text = Align.center(
            Text.from_markup(
                f"{jazzed_jerboas[0]}\n{jazzed_jerboas[1]}\n{jazzed_jerboas[2]}\n{jazzed_jerboas[3]}\n{jazzed_jerboas[4]}\n{jazzed_jerboas[5]}", justify="center"),
            vertical=height[2],
        )
        screen.update(Panel(text))
        sleep(1)

        text = Align.center(
            Text.from_markup(
                f"{jazzed_jerboas[1]}\n{jazzed_jerboas[2]}\n{jazzed_jerboas[3]}\n{jazzed_jerboas[4]}\n{jazzed_jerboas[5]}", justify="center"),
            vertical=height[2],
        )
        screen.update(Panel(text))
        sleep(1)

        text = Align.center(
            Text.from_markup(
                f"{jazzed_jerboas[2]}\n{jazzed_jerboas[3]}\n{jazzed_jerboas[4]}\n{jazzed_jerboas[5]}", justify="center"),
            vertical=height[2],
        )
        screen.update(Panel(text))
        sleep(1)

        text = Align.center(
            Text.from_markup(
                f"{jazzed_jerboas[3]}\n{jazzed_jerboas[4]}\n{jazzed_jerboas[5]}", justify="center"),
            vertical=height[2],
        )
        screen.update(Panel(text))
        sleep(1)

        text = Align.center(
            Text.from_markup(
                f"{jazzed_jerboas[4]}\n{jazzed_jerboas[5]}", justify="center"),
            vertical=height[2],
        )
        screen.update(Panel(text))
        sleep(1)

        text = Align.center(
            Text.from_markup(
                f"{jazzed_jerboas[5]}", justify="center"),
            vertical=height[2],
        )
        screen.update(Panel(text))
        sleep(1)

        text = Align.center(
            Text.from_markup(
                f"", justify="center"),
            vertical=height[2],
        )
        screen.update(Panel(text))
        sleep(1)

        text = Align.center(
            Text.from_markup(
                f"{message}", justify="center"),
            vertical=height[0],
        )
        screen.update(Panel(text))
        sleep(1)

        text = Align.center(
            Text.from_markup(
                f"{message}", justify="center"),
            vertical=height[1],
        )
        screen.update(Panel(text))
        sleep(1)

        text = Align.center(
            Text.from_markup(
                f"{message}", justify="center"),
            vertical=height[2],
        )
        screen.update(Panel(text))
        sleep(1)

        text = Align.center(
            Text.from_markup(
                f"", justify="center"),
            vertical=height[2],
        )
        screen.update(Panel(text))
        sleep(1)


credits()
