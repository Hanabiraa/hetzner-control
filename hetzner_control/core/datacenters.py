from typing import Dict, Any

import requests

from . import HetznerHandler, ExMessageHandler


class DatacenterHandler(HetznerHandler):
    """
    Hetzner Handler class that provides reference information about datacenters
    """

    def __init__(self):
        self.api_link = f"{self.get_prefix()}/datacenters"
        self.headers = self.get_headers()

    def get_all_datacenters(self) -> Dict[str, Any]:
        """
        Making request to server for information about all available datacenters

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
