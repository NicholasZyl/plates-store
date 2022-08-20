import typing

from src.domain.repositories import LicensePlatesRepository
from src.domain.services import PlatesStore


class Container:
    repository: typing.Optional[LicensePlatesRepository] = None
    store: typing.Optional[PlatesStore] = None

    def get_plates_store(self) -> PlatesStore:
        if not self.repository:
            raise Exception("Unknown repository to use.")

        if not self.store:
            self.store = PlatesStore(
                self.repository
            )

        return self.store

    def set_repository(self, repository: LicensePlatesRepository) -> None:
        self.repository = repository


container = Container()
