import requests
import json
from rich.console import Console, Text
from hetzner_control.core import HetznerHandler
from typing import Dict, Optional, Any, Tuple, Union


def server_handler_exception(response: Dict[str, Any]) -> None:
    """
    Very simple handler exception.
    Output in console json error message.

    :param response: json error message
    :return: None
    """
    console = Console()
    error_text = Text()
    error_text.append("Error: ", style="bold red")
    error_text.append(response['error']['message'], style="red")
    console.print(error_text)


class ServerHandler(HetznerHandler):
    """
    Hetzner Handler class for actions with servers
    """

    def __init__(self):
        self.basic_headers = {
            "Authorization": "Bearer " + self.API_TOKEN,
            "Content-Type": "application/json",
        }
        self.api_link = f"{self.prefix}/servers"

    def get_all_servers(self) -> Union[Dict[str, Any], None]:
        """
        make a request to Hetzner for lists of servers you own in your account
        """
        resp = requests.get(
            url=self.api_link,
            headers=self.basic_headers)

        if resp.status_code != 200:
            server_handler_exception(resp.json())
            return None
        else:
            return resp.json()

    def create_server(
            self,
            name: str,
            image: str,
            location: str,
            server_type: str,
            automount: bool = False,
            start_after_create: bool = False,
    ) -> Union[Dict[str, Any], None]:
        """
         make a request to Hetzner for create a server with specific parameters

        :param name: server name
        :param image: server image
        :param location: server location
        :param server_type: id or name of the image the server is created from
        :param automount: auto-mount Volumes after attach
        :param start_after_create: start Server right after creation
        :return: response
        """
        post_data = {
            "name": name,
            "image": image,
            "location": location,
            "server_type": server_type,
            "automount": automount,
            "start_after_create": start_after_create
        }
        resp = requests.post(
            url=self.api_link,
            headers=self.basic_headers,
            data=json.dumps(post_data))

        if resp.status_code != 201:
            server_handler_exception(resp.json())
            return None
        else:
            return resp.json()

    def delete_server(self, id_server: int) -> Union[bool, None]:
        """
        make request to delete server by ID.

        :param id_server: uniq server id
        :return: True if server deleted else print error json message and return None
        """
        resp = requests.delete(
            url=f"{self.api_link}/{id_server}",
            headers=self.basic_headers
        )
        if resp.status_code != 200:
            server_handler_exception(resp.json())
            return None
        else:
            return True
