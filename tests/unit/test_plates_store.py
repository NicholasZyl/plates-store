import datetime

from freezegun import freeze_time

from src.domain.repositories import LicensePlatesRepository
from src.domain.services import PlatesStore


def test_it_can_add_license_plate(in_memory_repository: LicensePlatesRepository) -> None:
    plates_store = PlatesStore(in_memory_repository)
    plates_store.store("M-PP123")


def test_it_can_retrieve_stored_license_plates(in_memory_repository: LicensePlatesRepository) -> None:
    plates_store = PlatesStore(in_memory_repository)
    plates_store.store("M-PP123")

    plates = plates_store.retrieve()

    assert isinstance(plates, list)
    assert len(plates) == 1
    assert plates[0].number == "M-PP123"


@freeze_time("2020-09-18T13:21:21Z")
def test_it_stores_license_plate_with_actual_timestamp(in_memory_repository: LicensePlatesRepository) -> None:
    plates_store = PlatesStore(in_memory_repository)
    plates_store.store("M-PP123")

    plates = plates_store.retrieve()

    assert plates[0].timestamp == datetime.datetime(2020, 9, 18, 13, 21, 21)
