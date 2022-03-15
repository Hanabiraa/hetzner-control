import os


class HetznerHandler:
    """
    Abstract Handler class for other Handlers
    """
    API_TOKEN = os.getenv("HETZNER_API_TOKEN")
    prefix = "https://api.hetzner.cloud/v1"