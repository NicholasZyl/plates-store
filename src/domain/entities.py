import datetime


class LicensePlate:
    def __init__(self, plate_number: str):
        self.number = plate_number
        self.timestamp = datetime.datetime.now()
