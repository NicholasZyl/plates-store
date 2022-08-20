import typing

from ..domain.entities import LicensePlate
from ..domain.repositories import LicensePlatesRepository


class PlatesStore:

    def __init__(self, repository: LicensePlatesRepository):
        self._repository = repository

    def store(self, plates_number: str) -> None:
        license_plate = LicensePlate(plates_number)
        self._repository.add(license_plate)

    def retrieve(self) -> typing.List[LicensePlate]:
        return self._repository.get_all()
