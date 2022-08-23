import abc

import typing

from ..domain.entities import LicensePlate


class LicenseAlreadyStored(Exception):
    """
    Raised when given license plate is already stored.
    """


class LicensePlatesRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, license_plate: LicensePlate) -> None:
        """
        Add license plate to the repository.

        :param license_plate:
        :return:
        """

    @abc.abstractmethod
    def get_all(self) -> typing.List[LicensePlate]:
        """
        Get all stored license plates.

        :return:
        """
