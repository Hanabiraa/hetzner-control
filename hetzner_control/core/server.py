import json
from typing import Dict, Any, Union

import requests

from . import HetznerHandler
from .exceptions import ExMessageHandler


class ServerHandler(HetznerHandler):
    """
    Hetzner Handler class for actions with servers
    """

    def __init__(self):
        self.api_link = f"{self.get_prefix()}/servers"
        self.headers = self.get_headers()

    def get_all_servers(self) -> Union[Dict[str, Any], None]:
        """
        Making a request to Hetzner for lists of servers you own in your account
        """
        resp = requests.get(
            url=self.api_link,
            headers=self.headers
        )

        if resp.status_code != 200:
            raise ExMessageHandler(
                self.create_exception_message(resp.json()),
                terminate_after=True
            )
        return resp.json()

    def get_server(self, id_server: int) -> Dict[str, Any]:
        """
        make request to server for detailed info about server by ID

        :param id_server: server ID
        :return: json response as Dict[str, Any]
        """
        resp = requests.get(
            url=f"{self.api_link}/{id_server}",
            headers=self.headers
        )

        if resp.status_code != 200:
            raise ExMessageHandler(
                self.create_exception_message(resp.json()),
                terminate_after=True
            )
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
        Making a request to Hetzner for create a server with specific parameters

        :param name: server name
        :param image: server image
        :param location: server location
        :param server_type: id or name of the image the server is created from
        :param automount: auto-mount Volumes after attach
        :param start_after_create: start Server right after creation
        :return: json response as Dict[str, Any]
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
            headers=self.headers,
            data=json.dumps(post_data)
        )

        if resp.status_code != 201:
            raise ExMessageHandler(
                self.create_exception_message(resp.json()),
                terminate_after=True
            )
        return resp.json()

    def delete_server(self, id_server: int) -> None:
        """
        Making request to delete server by ID.

        :param id_server: uniq server id
        :return: True if server deleted else print error json message and return None
        """
        resp = requests.delete(
            url=f"{self.api_link}/{id_server}",
            headers=self.headers
        )

        if resp.status_code != 200:
            raise ExMessageHandler(
                self.create_exception_message(resp.json()),
                terminate_after=True
            )

    def server_down(self, id_server: int) -> Dict[str, Any]:
        """
        Makes request to shut down the server by id

        :param id_server: server ID
        :return: json response as Dict[str, Any]
        """
        data = self.__make_action(
            id_server=id_server,
            action="shutdown"
        )
        return data

    def server_up(self, id_server: int) -> Dict[str, Any]:
        """
        Making request to power on the server by id

        :param id_server: server ID
        :return: json response as Dict[str, Any]
        """
        data = self.__make_action(
            id_server=id_server,
            action="poweron"
        )
        return data

    def __make_action(
            self,
            id_server: int,
            action: str,
            params: Union[Dict[str, Any], None] = None
    ) -> Dict[str, Any]:
        """
        Making a request to perform a specific action on the server by ID

        :param id_server: server ID
        :param action: action to be taken on the server
        :param params: parameters that are required for certain actions

        :return: json response as Dict[str, Any]
        """
        resp = requests.post(
            url=f"{self.api_link}/{id_server}/actions/{action}",
            headers=self.headers,
            params=(params if params else {})
        )

        if resp.status_code != 201:
            raise ExMessageHandler(
                self.create_exception_message(resp.json()),
                terminate_after=True
            )
        return resp.json()
