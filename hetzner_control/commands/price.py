import typer
from rich.console import Console
from rich.table import Table

from ..core.pricing import PricingHandler

app = typer.Typer()
handler = PricingHandler()
data = handler.get_all_prices()["pricing"]
currency = data["currency"]
vat = f"{float(data['vat_rate']):6.4f}"
console = Console()


@app.callback()
def callback():
    """
    Print as table prices for all or a specific resource
    """


@app.command("all", help="Information about price for all resources")
def get_all_prices():
    """
    Print price for all resources available on the platform
    """
    get_float_ip_price()
    get_float_ips_price()
    get_image_price()
    get_load_balancers_price()
    get_server_backup_price()
    get_server_types_price()
    get_traffic_price()
    get_volume_price()


@app.command("float_ip", help="Information about price for floating IP")
def get_float_ip_price():
    """
    Printing floating IP price as Table in console.
    """
    floating_ip_price = Table(title="Floating IP")
    floating_ip_price.add_column(f"Month, {currency}\nWithout VAT", justify="center", style="bold green")
    floating_ip_price.add_column(f"Month, {currency}\nWith VAT", justify="center", style="bold green")
    floating_ip_price.add_column("VAT, %", justify="center", style="bold")

    global data
    global vat
    ip_ = data["floating_ip"]
    floating_ip_price.add_row(
        f"{float(ip_['price_monthly']['net']):6.4f}",
        f"{float(ip_['price_monthly']['gross']):6.4f}",
        vat
    )
    global console
    console.print(floating_ip_price)


@app.command("float_ips", help="Information about price for floating IPs")
def get_float_ips_price():
    """
    Printing floating IPs price as Table in console
    """
    floating_ips_price = Table(title="Floating IPs")
    floating_ips_price.add_column("Type", justify="center")
    floating_ips_price.add_column("Location", justify="center")
    floating_ips_price.add_column(f"Month, {currency}\nWithout VAT", justify="center", style="bold green")
    floating_ips_price.add_column(f"Month, {currency}\nWith VAT", justify="center", style="bold green")
    floating_ips_price.add_column("VAT, %", justify="center", style="bold")

    global data
    global vat
    ips_ = data["floating_ips"]
    for i, ips_type in enumerate(ips_):
        for j, location_type in enumerate(ips_type['prices']):
            floating_ips_price.add_row(
                f"{ips_type['type'] if not j else ''}",
                f"{location_type['location']}",
                f"{float(location_type['price_monthly']['net']):6.4f}",
                f"{float(location_type['price_monthly']['gross']):6.4f}",
                vat
            )
    global console
    console.print(floating_ips_price)


@app.command("image", help="Information about price for image")
def get_image_price():
    """
    Printing image price as Table in console
    """
    image_price = Table(title="Image")
    image_price.add_column(f"Month, {currency}\nPrice per GB\nWithout VAT", justify="center", style="bold green")
    image_price.add_column(f"Month, {currency}\nPrice per GB\nWith VAT", justify="center", style="bold green")
    image_price.add_column("VAT, %", justify="center", style="bold")

    global data
    global vat
    image_ = data["image"]
    image_price.add_row(
        f"{float(image_['price_per_gb_month']['net']):6.4f}",
        f"{float(image_['price_per_gb_month']['gross']):6.4f}",
        vat
    )
    global console
    console.print(image_price)


@app.command("load_balancer", help="Information about price and types for load balancer")
def get_load_balancers_price():
    """
    Printing load balancers types and price as Table in console
    """
    load_balance_price = Table(title="Load Balancers")
    load_balance_price.add_column(f"id", justify="center", style="bold")
    load_balance_price.add_column(f"Name", justify="center", style="")
    load_balance_price.add_column(f"Location", justify="center", style="")
    load_balance_price.add_column(f"Hour, {currency}\nWithout VAT", justify="center", style="bold green")
    load_balance_price.add_column(f"Hour, {currency}\nWith VAT", justify="center", style="bold green")
    load_balance_price.add_column(f"Month, {currency}\nWithout VAT", justify="center", style="bold green")
    load_balance_price.add_column(f"Month, {currency}\nWith VAT", justify="center", style="bold green")
    load_balance_price.add_column("VAT, %", justify="center", style="bold")

    global data
    global vat
    lb_ = data["load_balancer_types"]
    for i, lb_type in enumerate(lb_):
        for j, location_type in enumerate(lb_type['prices']):
            load_balance_price.add_row(
                f"{lb_type['id'] if not j else ''}",
                f"{lb_type['name'] if not j else ''}",
                f"{location_type['location']}",
                f"{float(location_type['price_hourly']['net']):6.4f}",
                f"{float(location_type['price_hourly']['gross']):6.4f}",
                f"{float(location_type['price_monthly']['net']):6.4f}",
                f"{float(location_type['price_monthly']['gross']):6.4f}",
                vat
            )
    global console
    console.print(load_balance_price)


@app.command("backup", help="Information about price for server backup")
def get_server_backup_price():
    """
    Printing server backups price as Table in console
    """
    server_backup_price = Table(title="Server backup")
    server_backup_price.add_column("Percentage, %", justify="center", style="bold")
    server_backup_price.add_column("About")

    global data
    global vat
    server_backup_ = data['server_backup']
    server_backup_price.add_row(
        f"{float(server_backup_['percentage']):6.4f}",
        "increase base Server costs by specific percentage"
    )
    global console
    console.print(server_backup_price)


@app.command("server", help="Information about price and types for server")
def get_server_types_price():
    """
    Printing server configurations price as Table in console
    """
    server_types_price = Table(title="Server types")
    server_types_price.add_column(f"id", justify="center", style="bold")
    server_types_price.add_column(f"Name", justify="center", style="")
    server_types_price.add_column(f"Location", justify="center", style="")
    server_types_price.add_column(f"Hour, {currency}\nWithout VAT", justify="center", style="bold green")
    server_types_price.add_column(f"Hour, {currency}\nWith VAT", justify="center", style="bold green")
    server_types_price.add_column(f"Month, {currency}\nWithout VAT", justify="center", style="bold green")
    server_types_price.add_column(f"Month, {currency}\nWith VAT", justify="center", style="bold green")
    server_types_price.add_column("VAT, %", justify="center", style="bold")

    global data
    global vat
    servers_ = data["server_types"]
    for i, server_type_ in enumerate(servers_):
        for j, location_type in enumerate(server_type_['prices']):
            server_types_price.add_row(
                f"{server_type_['id'] if not j else ''}",
                f"{server_type_['name'] if not j else ''}",
                f"{location_type['location']}",
                f"{float(location_type['price_hourly']['net']):6.4f}",
                f"{float(location_type['price_hourly']['gross']):6.4f}",
                f"{float(location_type['price_monthly']['net']):6.4f}",
                f"{float(location_type['price_monthly']['gross']):6.4f}",
                vat
            )
    global console
    console.print(server_types_price)


@app.command("traffic", help="Information about traffic price")
def get_traffic_price():
    """
    Printing traffic price as Table in console
    """
    traffic_price = Table(title="Traffic")
    traffic_price.add_column(f"per TB, {currency}\nWithout VAT", justify="center", style="bold green")
    traffic_price.add_column(f"per TB, {currency}\nWith VAT", justify="center", style="bold green")

    global data
    global vat
    traffic_ = data["traffic"]
    traffic_price.add_row(
        f"{float(traffic_['price_per_tb']['net']):6.4f}",
        f"{float(traffic_['price_per_tb']['gross']):6.4f}"
    )
    global console
    console.print(traffic_price)


@app.command("volume", help="Information about volume price")
def get_volume_price():
    """
    Printing volume price as Table in console
    """
    volume_price = Table(title="Volume")
    volume_price.add_column(f"Month, {currency}\nper GB\nWithout VAT", justify="center", style="bold green")
    volume_price.add_column(f"per GB, {currency}\nper GB\nWith VAT", justify="center", style="bold green")

    global data
    global vat
    volume_ = data["volume"]
    volume_price.add_row(
        f"{float(volume_['price_per_gb_month']['net']):6.4f}",
        f"{float(volume_['price_per_gb_month']['gross']):6.4f}"
    )
    global console
    console.print(volume_price)
