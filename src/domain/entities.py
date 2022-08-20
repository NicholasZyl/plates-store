import datetime


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
        if plate_number == "" or "-" not in plate_number:
            raise InvalidGermanLicensePlateNumber()
