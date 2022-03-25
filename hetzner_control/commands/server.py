import typer
from rich.console import Console, Text
from rich.table import Table

from ..core.server import ServerHandler

app = typer.Typer()
_handler = ServerHandler()
_console = Console()


@app.callback()
def callback():
    """
    Operations with servers
    """


@app.command("list", help="Lists all servers you own")
def get_servers() -> None:
    """
    Making request to server list.
    Output to the console in the form of a table a list of all servers and some of their properties.

    :return: None
    """
    global _handler
    data = _handler.get_all_servers()

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
            f"{server['id']}",
            f"{server['status']}",
            f"{server['name']}",
            f"{server['server_type']['description']}",
            f"{server['server_type']['cores']}",
            f"{server['server_type']['memory']}",
            f"{server['server_type']['disk']}",
            f"{server['server_type']['prices'][0]['price_monthly']['gross'][:6]}",
        )

    global _console
    _console.print(table)


@app.command("info", help="Get a detailed description of the server by its ID")
def get_server(
        id_server: int = typer.Argument(..., help="ID of the Server"),
) -> None:
    """
    Getting detailed server info by ID

    :param id_server: server ID
    return None
    """
    global _handler
    data = _handler.get_server(id_server=id_server)['server']

    table_base = Table(title=f"Base info for {data['id']} server", style="bold")
    table_base.add_column("Created Date", justify="center", style="green")
    table_base.add_column("Backup time", justify="center", style="green")
    table_base.add_column("Datacenter", justify="center", style="")
    table_base.add_column("Image", justify="center", style="")
    table_base.add_column("ISO", justify="center", style="")
    table_base.add_column("Labels", justify="center", style="")
    table_base.add_column("Volumes", justify="center", style="")
    table_base.add_column("Status", justify="center", style=f"bold {'red' if data['status'] == 'off' else 'green'}")

    table_net = Table(title=f"Network info", style="bold")
    table_net.add_column("IPv4, MB", justify="center", style="bold cyan")
    table_net.add_column("IPv6", justify="center", style="bold cyan")
    table_net.add_column("Ingoing traffic, MB", justify="center", style="magenta")
    table_net.add_column("Outgoing traffic, MB", justify="center", style="magenta")
    table_net.add_column("Load balancers", justify="center", style="")

    table_base.add_row(
        f"{data['created']}",
        f"{data['backup_window']}",
        f"{data['datacenter']['name']}",
        f"{(data['image']['name'] if data['image'] else '-')}",
        f"{(data['iso']['description'] if data['iso'] else '-')}",
        f"{data['labels']}",
        f"{data['volumes']}",
        f"{data['status']}",
    )

    table_net.add_row(
        f"{data['public_net']['ipv4']['ip']}",
        f"{data['public_net']['ipv6']['ip']}",
        f"{data_ / 1000000 if (data_ := data['ingoing_traffic']) else 0}",
        f"{data_ / 1000000 if (data_ := data['outgoing_traffic']) else 0}",
        f"{data['load_balancers']}",
    )

    global _console
    _console.print(
        table_base,
        table_net,
        sep='\n'
    )


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
    Making request to create server with specific options.
    Output in console status of this operation, also print root_password for server if
    ssh-key has not been set

    :param name: Server name
    :param image: Server build image
    :param location: ID or name of Location to create Server in
    :param server_type: ID or name of the Server type
    :param automount: Auto-mount volumes after attach
    :param start_after_create: Start Server right after creation
    :return: None
    """
    global _handler
    data = _handler.create_server(
        name=name,
        image=image,
        location=location,
        server_type=server_type,
        automount=automount,
        start_after_create=start_after_create
    )

    global _console
    text = Text("Server has been created\n", style="bold green")
    text.append("Your root_password: ", style="bold cyan")
    text.append(data["root_password"], style="")
    _console.print(text)


@app.command("delete", help="Delete a server")
def delete_server(
        id_server: int = typer.Argument(..., help="ID of the Server"),
) -> None:
    """
    Making request for deleting server by ID.
    Output in console status of this operation.

    :param id_server: uniq server ID
    :return: None
    """
    global _handler
    _handler.delete_server(id_server=id_server)

    global _console
    text = Text("Server has been deleted", style="bold green")
    _console.print(text)


@app.command("down", help="Power off server by ID")
def shut_down_server(
        id_server: int = typer.Argument(..., help="ID of the Server"),
) -> None:
    """
    Making request to shut down server by ID.

    :param id_server: uniq server ID
    :return: None
    """
    global _handler
    data = _handler.server_down(id_server=id_server)

    global _console
    text = Text(
        f"Command {data['action']['command']}\nCommand status: {data['action']['status']}",
        style="bold green"
    )
    _console.print(text)


@app.command("up", help="Power on server by ID")
def shut_down_server(
        id_server: int = typer.Argument(..., help="ID of the Server"),
) -> None:
    """
    Making request to shut down server by ID.

    :param id_server: uniq server ID
    :return: None
    """
    global _handler
    data = _handler.server_up(id_server=id_server)

    global _console
    text = Text(
        f"Command {data['action']['command']}\nCommand status: {data['action']['status']}",
        style="bold green"
    )
    _console.print(text)
