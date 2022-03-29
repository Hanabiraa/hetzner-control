import typer
from rich.console import Console
from rich.table import Table

from ..core.server_types import ServerTypesHandler

app = typer.Typer()
_handler = ServerTypesHandler()
_console = Console()


@app.callback()
def callback() -> None:
    """
    Information about server types
    """


@app.command("all", help="Information about all server types")
def get_all_server_types() -> None:
    """
    Print as table specification for all server types
    """
    global _handler
    data = _handler.get_all_server_types()["server_types"]

    table = Table(title="Server types")
    table.add_column("id", justify="center", style="bold cyan")
    table.add_column("Name", justify="center")
    table.add_column("CPU type", justify="center")
    table.add_column("CPU Cores", justify="center", style="magenta")
    table.add_column("Disk", justify="center", style="magenta")
    table.add_column("Memory", justify="center", style="magenta")
    table.add_column("Storage type", justify="center")

    for type_ in data:
        table.add_row(
            f"{type_['id']}",
            f"{type_['name']}",
            f"{type_['cpu_type']}",
            f"{type_['cores']}",
            f"{type_['disk']}",
            f"{type_['memory']}",
            f"{type_['storage_type']}",
        )
    global _console
    _console.print(table)


@app.command("select", help="Information for a specific server type by ID")
def get_server_type(
        id: int = typer.Argument(..., help="Server type id"),
) -> None:
    """
     Print as table specification for server type by ID
    """
    global _handler
    data = _handler.get_server_type(id)["server_type"]

    table = Table(title=f"Server types for {id}")
    table.add_column("Name", justify="center")
    table.add_column("CPU type", justify="center")
    table.add_column("CPU Cores", justify="center", style="magenta")
    table.add_column("Disk", justify="center", style="magenta")
    table.add_column("Memory", justify="center", style="magenta")
    table.add_column("Storage type", justify="center")

    table.add_row(
        f"{data['name']}",
        f"{data['cpu_type']}",
        f"{data['cores']}",
        f"{data['disk']}",
        f"{data['memory']}",
        f"{data['storage_type']}",
    )
    global _console
    _console.print(table)
