import os
from unittest import mock

import pytest
import responses
from responses import matchers

from hetzner_control.core.datacenters import DatacenterHandler


@pytest.fixture(autouse=True)
def mock_settings_env_vars():
    """
    Mock real environment variable
    """
    with mock.patch.dict(os.environ, {"HETZNER_API_TOKEN": "1111"}):
        yield


class TestGetAllDatacenters:
    """
    For test DatacenterHandler.get_all_datacenters() method for good/bad response
    """
    url = "https://api.hetzner.cloud/v1/datacenters"
    headers = {
        "Authorization": "Bearer 1111",
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

        resp = DatacenterHandler().get_all_datacenters()
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
            _ = DatacenterHandler().get_all_datacenters()
