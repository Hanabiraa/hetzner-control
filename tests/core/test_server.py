import os
from unittest import mock

import pytest
import responses
from responses import matchers

from hetzner_control.core.server import ServerHandler


@pytest.fixture(autouse=True)
def mock_settings_env_vars():
    """
    Mock real environment variable
    """
    with mock.patch.dict(os.environ, {"HETZNER_API_TOKEN": "1111"}):
        yield


class TestGetAllServers:
    """
    For test ServerHandler.get_all_servers() method for good/bad response
    """
    url = "https://api.hetzner.cloud/v1/servers"
    headers = {
        "Authorization": "Bearer 1111",
        "Content-Type": "application/json"
    }

    @responses.activate
    def test_good_status(self):
        responses.add(
            method=responses.GET,
            url=self.url,
            json={"error": "not found"},
            status=200,
            content_type="application/json",
            match=[
                matchers.header_matcher(self.headers)
            ]
        )

        resp = ServerHandler().get_all_servers()
        assert resp["error"] == "not found"

    @responses.activate
    def test_bad_status(self):
        responses.add(
            method=responses.GET,
            url=self.url,
            json={"error": {"message": "bad status"}},
            status=500,
            content_type="application/json",
            match=[
                matchers.header_matcher(self.headers)
            ]
        )

        with pytest.raises(SystemExit):
            _ = ServerHandler().get_all_servers()


class TestGetServer:
    """
    For test ServerHandler.get_server() method for good/bad response
    """
    url = "https://api.hetzner.cloud/v1/servers/100"
    headers = {
        "Authorization": "Bearer 1111",
        "Content-Type": "application/json"
    }

    @responses.activate
    def test_good_status(self):
        responses.add(
            method=responses.GET,
            url=self.url,
            json={"error": "not found"},
            status=200,
            content_type="application/json",
            match=[
                matchers.header_matcher(self.headers)
            ]
        )

        resp = ServerHandler().get_server(id_server=100)
        assert resp["error"] == "not found"

    @responses.activate
    def test_bad_status(self):
        responses.add(
            method=responses.GET,
            url=self.url,
            json={"error": {"message": "bad status"}},
            status=500,
            content_type="application/json",
            match=[
                matchers.header_matcher(self.headers)
            ]
        )

        with pytest.raises(SystemExit):
            _ = ServerHandler().get_server(
                id_server=100
            )


class TestCreateServer:
    """
    For test ServerHandler.create_server() method for good/bad response
    """
    url = "https://api.hetzner.cloud/v1/servers"
    headers = {
        "Authorization": "Bearer 1111",
        "Content-Type": "application/json"
    }
    matchers_ = [
        matchers.header_matcher(headers),
        matchers.json_params_matcher({
            "name": "testing",
            "image": "ubuntu",
            "location": "nbg1",
            "server_type": "ccx2",
            "automount": False,
            "start_after_create": False
        })
    ]

    @responses.activate
    def test_good_status(self):
        responses.add(
            method=responses.POST,
            url=self.url,
            json={"error": "not found"},
            status=201,
            content_type="application/json",
            match=self.matchers_,
        )

        resp = ServerHandler().create_server(
            name="testing",
            image="ubuntu",
            location="nbg1",
            server_type="ccx2",
            automount=False,
            start_after_create=False,
        )
        assert resp["error"] == "not found"

    @responses.activate
    def test_bad_status(self):
        responses.add(
            method=responses.POST,
            url=self.url,
            json={"error": {"message": "bad status"}},
            status=500,
            content_type="application/json",
            match=self.matchers_,
        )

        with pytest.raises(SystemExit):
            _ = ServerHandler().create_server(
                name="testing",
                image="ubuntu",
                location="nbg1",
                server_type="ccx2",
                automount=False,
                start_after_create=False,
            )


class TestDeleteServer:
    """
    For test ServerHandler.delete_server() method for good/bad response
    """
    url = "https://api.hetzner.cloud/v1/servers/111"
    headers = {
        "Authorization": "Bearer 1111",
        "Content-Type": "application/json"
    }
    matchers_ = [
        matchers.header_matcher(headers),
    ]

    @responses.activate
    def test_good_status(self):
        responses.add(
            method=responses.DELETE,
            url=self.url,
            json={"error": "not found"},
            status=200,
            content_type="application/json",
            match=self.matchers_,
        )

        ServerHandler().delete_server(
            id_server=111
        )
        assert True

    @responses.activate
    def test_bad_status(self):
        responses.add(
            method=responses.DELETE,
            url=self.url,
            json={"error": {"message": "bad status"}},
            status=500,
            content_type="application/json",
            match=self.matchers_,
        )

        with pytest.raises(SystemExit):
            ServerHandler().delete_server(
                id_server=111
            )


class TestMakeAction:
    """
    For test ServerHandler.__make_action() method for good/bad response
    """
    url = "https://api.hetzner.cloud/v1/servers/111/actions/restart"
    headers = {
        "Authorization": "Bearer 1111",
        "Content-Type": "application/json"
    }
    matchers_ = [
        matchers.header_matcher(headers),
    ]

    @responses.activate
    def test_good_status(self):
        responses.add(
            method=responses.POST,
            url=self.url,
            json={"error": "not found"},
            status=201,
            content_type="application/json",
            match=self.matchers_,
        )

        resp = ServerHandler()._ServerHandler__make_action(
            id_server=111,
            action="restart",
            params=None
        )
        assert resp["error"] == "not found"

    @responses.activate
    def test_bad_status(self):
        responses.add(
            method=responses.POST,
            url=self.url,
            json={"error": {"message": "bad status"}},
            status=500,
            content_type="application/json",
            match=self.matchers_,
        )

        with pytest.raises(SystemExit):
            _ = ServerHandler()._ServerHandler__make_action(
                id_server=111,
                action="restart",
                params=None
            )
