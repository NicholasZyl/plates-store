import pytest
import typing

from src.domain.entities import LicensePlate
from src.domain.repositories import LicensePlatesRepository


class FakeRepository(LicensePlatesRepository):

    def __init__(self, plates: typing.List[LicensePlate]):
        self._plates = plates

    def add(self, license_plate: LicensePlate) -> None:
        self._plates.append(license_plate)

    def get_all(self) -> typing.List[LicensePlate]:
        return self._plates


@pytest.fixture()
def in_memory_repository() -> LicensePlatesRepository:
    return FakeRepository([])
