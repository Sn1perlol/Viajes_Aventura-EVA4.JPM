from datetime import datetime

class Package:
    def __init__(self, name, start_date, end_date, price, available_slots, transport_id, status_id, id_package=None):
        self._id_package = id_package
        self._name = name
        self._start_date = self._parse_date(start_date)
        self._end_date = self._parse_date(end_date)
        self._price = float(price)
        self._available_slots = int(available_slots)
        self._transport_id = int(transport_id)
        self._status_id = int(status_id)
        self.validate()

    def _parse_date(self, date_value):
        if isinstance(date_value, str):
            try:
                return datetime.fromisoformat(date_value)
            except ValueError:
                pass
        return date_value

    def validate(self):
        if not self._name or not self._name.strip():
            raise ValueError("Package name cannot be empty.")
        if self._price < 0:
            raise ValueError("Price cannot be negative.")
        if self._available_slots < 0:
            raise ValueError("Available slots cannot be negative.")
        if isinstance(self._start_date, datetime) and isinstance(self._end_date, datetime):
            if self._end_date < self._start_date:
                raise ValueError("End date cannot be before start date.")

    def is_available(self, requested_slots):
        return self._available_slots >= requested_slots

    @property
    def id_package(self): return self._id_package
    @property
    def name(self): return self._name
    @property
    def start_date(self): return self._start_date
    @property
    def end_date(self): return self._end_date
    @property
    def price(self): return self._price
    @property
    def available_slots(self): return self._available_slots
    @property
    def transport_id(self): return self._transport_id
    @property
    def status_id(self): return self._status_id

    def __str__(self):
        return f"ID: {self._id_package} | {self._name} | Slots: {self._available_slots} | Price: ${self._price:.2f}"