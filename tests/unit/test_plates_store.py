import datetime

import typing
from freezegun import freeze_time

from src.domain.entities import LicensePlate
from src.domain.repositories import LicensePlatesRepository
from src.domain.services import PlatesStore


class FakeRepository(LicensePlatesRepository):

    def __init__(self, plates: typing.List[LicensePlate]):
        self._plates = plates

    def add(self, license_plate: LicensePlate) -> None:
        self._plates.append(license_plate)

    def get_all(self) -> typing.List[LicensePlate]:
        return self._plates


def test_it_can_add_license_plate() -> None:
    plates_store = PlatesStore(FakeRepository([]))
    plates_store.store("M-PP123")


def test_it_can_retrieve_stored_license_plates() -> None:
    plates_store = PlatesStore(FakeRepository([]))
    plates_store.store("M-PP123")

    plates = plates_store.retrieve()

    assert isinstance(plates, list)
    assert len(plates) == 1
    assert plates[0].number == "M-PP123"


@freeze_time("2020-09-18T13:21:21Z")
def test_it_stores_license_plate_with_actual_timestamp() -> None:
    plates_store = PlatesStore(FakeRepository([]))
    plates_store.store("M-PP123")

    plates = plates_store.retrieve()

    assert plates[0].timestamp == datetime.datetime(2020, 9, 18, 13, 21, 21)
