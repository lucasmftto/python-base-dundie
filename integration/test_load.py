import pytest
from click.testing import CliRunner
from dundie.cli import load, main

cmd = CliRunner()


@pytest.mark.integration
@pytest.mark.medium
def test_load_positive_call_load_command():
    """integration test for load function"""
    out = cmd.invoke(load, "./tests/assets/people.csv")

    assert "Dundie Mifflin Associates" in out.output


@pytest.mark.integration
@pytest.mark.medium
@pytest.mark.parametrize("wrong_command", ["loady", "carrega", "start"])
def test_load_negative_call_load_command(wrong_command):
    """integration test for load function"""
    out = cmd.invoke(main, wrong_command, "./tests/assets/people.csv")
    assert out.exit_code != 0
    assert f"No such command '{wrong_command}'." in out.output
