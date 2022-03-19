import typer
from rich.console import Console, Text
from rich.table import Table

from hetzner_control.core.server import ServerHandler

app = typer.Typer()


@app.callback()
def callback():
    """
    Operations with servers
    """


@app.command("list", help="Lists all servers you own")
def get_servers() -> None:
    """
    Make request to server list.
    Output to the console in the form of a table a list of all servers and some of their properties.

    :return: None
    """
    handler = ServerHandler()
    data = handler.get_all_servers()

    console = Console()
    table = Table(title="Server List")

    table.add_column("ID", justify="center", style="bold cyan")
    table.add_column("Status", justify="center", style="bold cyan")
    table.add_column("Name", justify="center")
    table.add_column("Server type", justify="center", style="magenta")
    table.add_column("CPU core", justify="center", style="magenta")
    table.add_column("Memory, GB", justify="center", style="magenta")
    table.add_column("Disk, GB", justify="center", style="magenta")
    table.add_column("Price", justify="center", style="green")

    for server in data['servers']:
        table.add_row(
            str(server['id']),
            server['status'],
            server['name'],
            server['server_type']['description'],
            str(server['server_type']['cores']),
            str(server['server_type']['memory']),
            str(server['server_type']['disk']),
            server['server_type']['prices'][0]['price_monthly']['gross'][:6],
        )
    console.print(table)


@app.command("create", help="Create a server with custom options")
def create_server(
        name: str = typer.Argument(..., help="Server name"),
        image: str = typer.Argument("ubuntu-20.04", help="Server build image"),
        location: str = typer.Argument("nbg1", help="ID or name of Location to create Server in"),
        server_type: str = typer.Argument("cx11", help="ID or name of the Server type"),
        automount: bool = typer.Argument(False, help="Auto-mount Volumes after attach"),
        start_after_create: bool = typer.Argument(False, help="Start Server right after creation"),
) -> None:
    """
    Make request to create server with specific options.
    Output in console status of this operation, also print root_password for server if
    ssh-key has not been set

    :param name: Server nam
    :param image: Server build image
    :param location: ID or name of Location to create Server in
    :param server_type: ID or name of the Server type
    :param automount: Auto-mount volumes after attach
    :param start_after_create: Start Server right after creation
    :return: None
    """
    handler = ServerHandler()
    data = handler.create_server(
        name=name,
        image=image,
        location=location,
        server_type=server_type,
        automount=automount,
        start_after_create=start_after_create
    )

    console = Console()
    text = Text("Server has been created\n", style="bold green")
    text.append("Your root_password: ", style="bold cyan")
    text.append(data["root_password"], style="black")
    console.print(text)


@app.command("delete", help="Delete a server")
def delete_server(
        id_server: int = typer.Argument(..., help="ID of the Server"),
) -> None:
    """
    Make request for deleting server by ID.
    Output in console status of this operation.

    :param id_server: uniq server ID
    :return: None
    """
    handler = ServerHandler()
    handler.delete_server(id_server=id_server)
    console = Console()
    text = Text("Server has been deleted", style="bold green")
    console.print(text)
