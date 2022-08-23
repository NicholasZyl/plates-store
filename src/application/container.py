import os
import typing

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

from src.domain.services import PlatesStore
from src.infrastructure.orm import SqlAlchemyLicensePlatesRepository, start_mappers


class Container:
    engine: typing.Optional[Engine] = None
    store: typing.Optional[PlatesStore] = None

    def get_plates_store(self) -> PlatesStore:
        if not self.store:
            self.store = PlatesStore(
                SqlAlchemyLicensePlatesRepository(
                    sessionmaker(bind=self.get_db())()
                )
            )

        return self.store

    def set_db(self, engine: Engine) -> None:
        self.engine = engine

    def get_db(self) -> Engine:
        if not self.engine:
            start_mappers()
            self.engine = create_engine(container._get_db_uri())

        return self.engine

    @staticmethod
    def _get_db_uri() -> str:
        host = os.environ.get("DB_HOST")
        port = os.environ.get("DB_PORT")
        user = os.environ.get("DB_USER")
        password = os.environ.get("DB_PASSWORD")
        if not host or not port or not user or not password:
            raise Exception("Can't connect to the database.")

        db_name = "plates_store"

        return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"


container = Container()
