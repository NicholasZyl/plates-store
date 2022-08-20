import datetime
import re


class InvalidGermanLicensePlateNumber(Exception):
    """
    Raised when plate number is not a valid German License plate.
    """


class LicensePlate:
    def __init__(self, plate_number: str):
        LicensePlate._validate_plate_number(plate_number)
        self.number = plate_number
        self.timestamp = datetime.datetime.now()

    @staticmethod
    def _validate_plate_number(plate_number: str) -> None:
        match = re.search(r'^[A-Z]{1,3}\-[A-Z]{1,2}[1-9]\d{,3}$', plate_number)
        if not match:
            raise InvalidGermanLicensePlateNumber()
