import datetime

import pytest
from freezegun import freeze_time

from src.domain.entities import LicensePlate, InvalidGermanLicensePlateNumber


def test_it_is_created_from_string() -> None:
    license_plate = LicensePlate("M-PP123")

    assert isinstance(license_plate, LicensePlate)


def test_it_has_a_number() -> None:
    number = "M-PP123"
    license_plate = LicensePlate(number)

    assert license_plate.number == number


@freeze_time("2020-09-18T13:21:21Z")
def test_it_has_a_timestamp_equal_to_creation_time() -> None:
    license_plate = LicensePlate("M-PP123")

    assert license_plate.timestamp == datetime.datetime(2020, 9, 18, 13, 21, 21)


def test_it_cannot_have_empty_number() -> None:
    with pytest.raises(InvalidGermanLicensePlateNumber):
        LicensePlate("")


def test_number_must_have_a_hyphen() -> None:
    with pytest.raises(InvalidGermanLicensePlateNumber):
        LicensePlate("MPP123")
