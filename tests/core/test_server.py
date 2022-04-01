import pytest
import responses

from hetzner_control.core.server import ServerHandler


class TestServerCore:
    @responses.activate
    def test_get_all_servers(self):
        server_handler = ServerHandler()
        responses.add(
            method=responses.GET,
            url=server_handler.api_link,
            json={"error": "not found"},
            status=200,
            content_type="application/json"
        )
        resp = server_handler.get_all_servers()
        assert resp["error"] == "not found"
