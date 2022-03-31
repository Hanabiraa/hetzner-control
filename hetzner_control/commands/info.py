import typer

import hetzner_control.commands.datacenters as datacenters
import hetzner_control.commands.price as price
import hetzner_control.commands.server_types as server_types

app = typer.Typer()
app.add_typer(price.app, name="price")
app.add_typer(server_types.app, name="server")
app.add_typer(datacenters.app, name="datacenter")


@app.callback()
def callback() -> None:
    """
    Information about available data centers, images, ISOs and more
    """
