from sqlalchemy.orm import Session

from src.domain.entities import LicensePlate
from src.domain.repositories import LicensePlatesRepository
from src.infrastructure.orm import SqlAlchemyLicensePlatesRepository


def test_it_is_license_plate_repository(in_memory_db: Session) -> None:
    repository = SqlAlchemyLicensePlatesRepository(in_memory_db)

    assert isinstance(repository, LicensePlatesRepository)


def test_it_stores_license_plate(in_memory_db: Session) -> None:
    repository = SqlAlchemyLicensePlatesRepository(in_memory_db)
    plate = LicensePlate("M-PP123")
    repository.add(plate)

    plates = repository.get_all()

    assert len(plates) == 1
    assert plate in plates
