from flask import Blueprint

from src.application.container import container
from src.infrastructure.orm import metadata

init_command = Blueprint('init', __name__)


@init_command.cli.command()  # type: ignore
def init_db() -> None:
    metadata.create_all(container.get_db())
