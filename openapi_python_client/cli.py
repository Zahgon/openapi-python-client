import codecs
from collections.abc import Sequence
from pathlib import Path
from pprint import pformat

import typer

from openapi_python_client import MetaType, __version__
from openapi_python_client.config import Config, ConfigFile
from openapi_python_client.parser.errors import ErrorLevel, GeneratorError, ParseError

app = typer.Typer(name="openapi-python-client")


def _version_callback(value: bool) -> None:
    pass


def _process_config(
    *,
    url: str | None,
    path: Path | None,
    config_path: Path | None,
    meta_type: MetaType,
    file_encoding: str,
    overwrite: bool,
    output_path: Path | None,
) -> Config:
    pass


# noinspection PyUnusedLocal


@app.callback()
def cli(
    version: bool = typer.Option(False, "--version", callback=_version_callback, help="Print the version and exit"),
) -> None:
    """Generate a Python client from an OpenAPI document"""


def _print_parser_error(err: GeneratorError, color: str) -> None:
    pass


def handle_errors(errors: Sequence[GeneratorError], fail_on_warning: bool = False) -> None:
    """Turn custom errors into formatted error messages"""
    pass


@app.command()
def generate(
    url: str | None = typer.Option(None, help="A URL to read the OpenAPI document from"),
    path: Path | None = typer.Option(None, help="A path to the OpenAPI document"),
    custom_template_path: Path | None = typer.Option(
        None,
        help="A path to a directory containing custom template(s)",
        file_okay=False,
        dir_okay=True,
        readable=True,
        resolve_path=True,
    ),  # type: ignore
    meta: MetaType = typer.Option(
        MetaType.POETRY,
        help="The type of metadata you want to generate.",
    ),
    file_encoding: str = typer.Option("utf-8", help="Encoding used when writing generated"),
    config_path: Path | None = typer.Option(None, "--config", help="Path to the config file to use"),
    fail_on_warning: bool = False,
    overwrite: bool = typer.Option(False, help="Overwrite the existing client if it exists"),
    output_path: Path | None = typer.Option(
        None,
        help="Path to write the generated code to. "
        "Defaults to the OpenAPI document title converted to kebab or snake case (depending on meta type). "
        "Can also be overridden with `project_name_override` or `package_name_override` in config.",
    ),
) -> None:
    """Generate a new OpenAPI Client library"""
    pass
