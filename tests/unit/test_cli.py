"""Test the click cli"""
from click.testing import CliRunner

from porringer.application.click import application


class TestCLI:
    """_summary_"""

    def test_version(self) -> None:
        """_summary_"""
        runner = CliRunner()
        result = runner.invoke(application, ["--version"])

        assert result.exit_code == 0
        assert result.output

    def test_self_update(self) -> None:
        """_summary_"""
        runner = CliRunner()
        result = runner.invoke(application, ["self", "update"])

        assert result.exit_code == 0
        assert not result.output
