import typer
from hetzner_control.constants import __app_name__, __version__

app = typer.Typer()


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

    $HETZNER_API_KEY = your_api_key
    """


def main():
    app()
