import typing

from ..domain.entities import LicensePlate, InvalidGermanLicensePlateNumber
from ..domain.repositories import LicensePlatesRepository


class NonProcessablePlateNumber(Exception):
    """
    Raised when plate number cannot be processed.
    """


class PlatesStore:

    def __init__(self, repository: LicensePlatesRepository):
        self._repository = repository

    def store(self, plates_number: str) -> None:
        try:
            license_plate = LicensePlate(plates_number)
        except InvalidGermanLicensePlateNumber:
            raise NonProcessablePlateNumber("Not a valid German plate number")

        self._repository.add(license_plate)

    def retrieve(self) -> typing.List[LicensePlate]:
        return self._repository.get_all()
