import typing

from sqlalchemy import Table, MetaData, Column, String, DateTime
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, mapper

from src.domain.entities import LicensePlate
from src.domain.repositories import LicensePlatesRepository, LicenseAlreadyStored


class SqlAlchemyLicensePlatesRepository(LicensePlatesRepository):

    def __init__(self, session: Session):
        self._session = session

    def add(self, license_plate: LicensePlate) -> None:
        try:
            self._session.add(license_plate)
            self._session.commit()
        except SQLAlchemyError:
            self._session.rollback()
            raise LicenseAlreadyStored()

    def get_all(self) -> typing.List[LicensePlate]:
        plates: typing.List[LicensePlate] = self._session.query(LicensePlate).all()
        return plates


metadata = MetaData()


license_plates = Table(
    "license_plates",
    metadata,
    Column("number", String(10), primary_key=True, index=True),
    Column("timestamp", DateTime(), primary_key=True)
)


def start_mappers() -> None:
    mapper(LicensePlate, license_plates)
