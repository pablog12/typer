import subprocess
from pathlib import Path

import typer
from typer.testing import CliRunner

from parameter_types.path import tutorial002 as mod

runner = CliRunner()

app = typer.Typer()
app.command()(mod.main)

config_file = Path("./config.txt")


def test_not_exists():
    if config_file.exists():  # pragma no cover
        config_file.unlink()
    result = runner.invoke(app, ["--config", f"{config_file}"])
    assert result.exit_code != 0
    assert (
        'Error: Invalid value for "--config": File "config.txt" does not exist.'
        in result.output
    )


def test_exists():
    config_file.write_text("some settings")
    result = runner.invoke(app, ["--config", f"{config_file}"])
    config_file.unlink()
    assert result.exit_code == 0
    assert "Config file contents: some settings" in result.output


def test_dir():
    result = runner.invoke(app, ["--config", "./"])
    assert result.exit_code != 0
    assert (
        'Error: Invalid value for "--config": File "./" is a directory.'
        in result.output
    )


def test_script():
    result = subprocess.run(
        ["coverage", "run", mod.__file__, "--help"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
    )
    assert "Usage" in result.stdout
