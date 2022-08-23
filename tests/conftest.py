from typing import Generator

import pytest

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, Session, clear_mappers

from src.domain.repositories import LicensePlatesRepository
from src.infrastructure.orm import SqlAlchemyLicensePlatesRepository, metadata, start_mappers


@pytest.fixture(scope="module")
def in_memory_db_engine() -> Generator[Engine, None, None]:
    engine = create_engine("sqlite:///:memory:")
    metadata.create_all(engine)
    start_mappers()
    yield engine
    clear_mappers()


@pytest.fixture()
def in_memory_db_session(in_memory_db_engine: Engine) -> Session:
    return sessionmaker(bind=in_memory_db_engine)()


@pytest.fixture()
def in_memory_repository(in_memory_db_session: Session) -> LicensePlatesRepository:
    return SqlAlchemyLicensePlatesRepository(in_memory_db_session)


@pytest.fixture()
def _with_clean_postgres_db() -> None:
    print("Clean postgres")
    # engine = create_engine("postgresql://api:qwerty1234@localhost:54321/plates_store", echo=True)
    # metadata.create_all(engine)
    # metadata.drop_all(engine)
