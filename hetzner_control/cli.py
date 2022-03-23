import typer

import hetzner_control.commands.info as info
import hetzner_control.commands.server as server
from hetzner_control import __app_name__, __version__

app = typer.Typer()
app.add_typer(server.app, name="server")
app.add_typer(info.app, name="info")


@app.command("version")
def get_version():
    """
    Show app version
    """
    typer.echo(f"{__app_name__} {__version__}")


@app.callback()
def callback():
    """
    CLI app for managing servers on the Hetzner cloud platform

    To use this application, you need an API token, so
    add the given environment variable to your terminal config file

    $HETZNER_API_TOKEN = your_api_key
    """


def main():
    app()
