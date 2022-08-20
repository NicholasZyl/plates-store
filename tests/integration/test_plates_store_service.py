import datetime

import pytest
from freezegun import freeze_time

from src.domain.entities import LicensePlate
from src.domain.repositories import LicensePlatesRepository
from src.domain.services import PlatesStore


@pytest.mark.skip(reason="Work in progress on integration level")
@freeze_time("2020-09-18T13:21:21Z")
def test_it_is_possible_to_store_and_retrieve_plates(in_memory_repository: LicensePlatesRepository) -> None:
    license_plate = "M-PP123"

    plates_store = PlatesStore(in_memory_repository)
    plates_store.store(license_plate)
    plates = plates_store.retrieve()

    assert len(plates) == 1
    assert isinstance(plates[0], LicensePlate)
    assert plates[0].number == license_plate
    assert plates[0].timestamp == datetime.datetime(2020, 9, 18, 13, 21, 21)
