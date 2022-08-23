import pytest
from freezegun import freeze_time
from sqlalchemy.orm import Session

from src.domain.entities import LicensePlate
from src.domain.repositories import LicensePlatesRepository, LicenseAlreadyStored
from src.infrastructure.orm import SqlAlchemyLicensePlatesRepository


def test_it_is_license_plate_repository(in_memory_db_session: Session) -> None:
    repository = SqlAlchemyLicensePlatesRepository(in_memory_db_session)

    assert isinstance(repository, LicensePlatesRepository)


def test_it_stores_license_plate(in_memory_db_session: Session) -> None:
    repository = SqlAlchemyLicensePlatesRepository(in_memory_db_session)
    plate = LicensePlate("M-PP123")
    repository.add(plate)

    plates = repository.get_all()

    assert len(plates) == 1
    assert plate in plates


@freeze_time("2020-09-18T13:21:21Z")
def test_it_fails_to_store_the_same_license_plate_with_same_timestamp_twice(in_memory_db_session: Session) -> None:
    repository = SqlAlchemyLicensePlatesRepository(in_memory_db_session)
    plate = LicensePlate("M-PP123")
    repository.add(plate)
    plate = LicensePlate("M-PP123")
    with pytest.raises(LicenseAlreadyStored):
        repository.add(plate)
