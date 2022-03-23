import requests
from typing import Dict, Any, Union

from . import HetznerHandler, ExMessageHandler


class DatacenterHandler(HetznerHandler):
    """
    Hetzner Handler class for various reference
     information regarding data centers, images, etc.
    """

    def __init__(self):
        self.api_link = f"{self.get_prefix()}/datacenters"
        self.basic_headers = {
            "Authorization": "Bearer " + self.get_api_token(),
            "Content-Type": "application/json",
        }

    def get_all_datacenters(self) -> Dict[str, Any]:
        """
        Making request to server for information about all available datacenters

        :return: json response as Dict[str, Any]
        """
        resp = requests.get(
            url=self.api_link,
            headers=self.basic_headers
        )

        if resp.status_code != 200:
            raise ExMessageHandler(
                self.create_exception_message(resp.json()),
                terminate_after=True
            )
        return resp.json()
