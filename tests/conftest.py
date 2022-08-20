from typing import Generator

import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, clear_mappers

from src.domain.repositories import LicensePlatesRepository
from src.infrastructure.orm import SqlAlchemyLicensePlatesRepository, metadata, start_mappers


@pytest.fixture()
def in_memory_db() -> Generator[Session, None, None]:
    engine = create_engine("sqlite:///:memory:")
    metadata.create_all(engine)
    start_mappers()
    yield sessionmaker(bind=engine)()
    clear_mappers()


@pytest.fixture()
def in_memory_repository(in_memory_db: Session) -> LicensePlatesRepository:
    return SqlAlchemyLicensePlatesRepository(in_memory_db)
