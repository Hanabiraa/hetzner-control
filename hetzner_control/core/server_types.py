from typing import Dict, Any

import requests

from . import HetznerHandler, ExMessageHandler


class ServerTypesHandler(HetznerHandler):
    """
    Hetzner Handler class that provides reference information about server types
    """

    def __init__(self):
        self.api_link = f"{self.get_prefix()}/server_types"
        self.headers = self.get_headers()

    def get_all_server_types(self) -> Dict[str, Any]:
        """
        Making request to server for information about all server types

        :return: json response as Dict[str, Any]
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

    def get_server_type(self, id_: int) -> Dict[str, Any]:
        """
        Making request to server for information about server type by ID

        :return: json response as Dict[str, Any]
        """
        resp = requests.get(
            url=f"{self.api_link}/{id_}",
            headers=self.headers
        )

        if resp.status_code != 200:
            raise ExMessageHandler(
                self.create_exception_message(resp.json()),
                terminate_after=True
            )
        return resp.json()
