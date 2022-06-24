from typer.testing import CliRunner

from hetzner_control import __app_name__, __version__
from hetzner_control.cli import app

# runner = CliRunner()


# class TestCli:
#     def test_app_version(self):
#         result = runner.invoke(app, ["version"])
#         assert f"{__app_name__} {__version__}" in result.stdout
