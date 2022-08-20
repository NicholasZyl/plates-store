import abc

import typing

from ..domain.entities import LicensePlate


class LicensePlatesRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, license_plate: LicensePlate) -> None:
        pass

    @abc.abstractmethod
    def get_all(self) -> typing.List[LicensePlate]:
        pass
