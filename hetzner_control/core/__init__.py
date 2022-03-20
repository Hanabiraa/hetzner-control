import os
from typing import Dict, Any

from rich.console import Text

from hetzner_control.core.exceptions import ExMessageHandler


class HetznerHandler:
    """
    Abstract Handler class for other Handlers
    """

    @staticmethod
    def get_prefix():
        return "https://api.hetzner.cloud/v1"

    @staticmethod
    def get_api_token():
        token = os.getenv("HETZNER_API_TOKEN", default=None)

        if not token:
            message = Text()
            message.append("API TOKEN not found!\n", style="bold red")
            message.append("Please add in terminal configuration file like .bashrc (.zshrc, etc) this:\n")
            message.append(f"export HETZNER_API_TOKEN='your_api_token'", style="bold")
            raise ExMessageHandler(message, terminate_after=True)
        return token

    @staticmethod
    def create_exception_message(response: Dict[str, Any]) -> Text:
        """
        Wrapper function for generate rich.console.Text object with current colors
        from json response from server, if status code wrong

        :return: str like rich.console.Text object
        """
        message = Text()
        message.append("Error: ", style="bold red")
        message.append(response['error']['message'], style="red")
        return message
