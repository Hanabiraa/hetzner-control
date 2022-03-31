import typer
from rich.console import Console
from rich.table import Table

from ..core.datacenters import DatacenterHandler

app = typer.Typer()
_handler = DatacenterHandler()


@app.callback()
def callback() -> None:
    """
    Information about datacenters available on platform
    """


@app.command("all", help="List all datacenters, which available in current moment")
def get_all_datacenters() -> None:
    """
    Making request to datacenters list.
    Output to the console in the form of a table a list of all datacenters and some of their properties.

    :return: None
    """
    global _handler
    data = _handler.get_all_datacenters()

    table = Table()
    table.add_column("id", justify="center", style="green")
    table.add_column("Name", justify="center", style="magenta")
    table.add_column("Location name", justify="center", style="magenta")
    table.add_column("Country", justify="center", style="")
    table.add_column("City", justify="center", style="")
    table.add_column("Network zone", justify="center", style="")
    table.add_column("Description", justify="center", style="")

    for datacenter in data['datacenters']:
        table.add_row(
            f"{datacenter['id']}",
            f"{datacenter['name']}",
            f"{datacenter['location']['name']}",
            f"{datacenter['location']['country']}",
            f"{datacenter['location']['city']}",
            f"{datacenter['location']['network_zone']}",
            f"{datacenter['description']}",
        )

    console = Console()
    console.print(table)
