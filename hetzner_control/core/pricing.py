import requests
from typing import Dict, Any, Union

from . import HetznerHandler, ExMessageHandler


class PricingHandler(HetznerHandler):
    """
    Hetzner Handler class
    for prices for all resources available on the platform.
    """

    def __init__(self):
        self.api_link = f"{self.get_prefix()}/pricing"
        self.basic_headers = {
            "Authorization": "Bearer " + self.get_api_token(),
            "Content-Type": "application/json",
        }

    def get_all_prices(self) -> Dict[str, Any]:
        """
        Making request to server for prices
         for all resources available on the platform.

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
