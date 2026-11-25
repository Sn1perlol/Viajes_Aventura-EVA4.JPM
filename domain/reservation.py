class Reservation:
    def __init__(self, reservation_date, number_of_people, reservation_code, client_id, package_id, status_id, id_reservation=None):
        self._id_reservation = id_reservation
        self._reservation_date = reservation_date
        self._number_of_people = int(number_of_people)
        self._reservation_code = reservation_code
        self._client_id = int(client_id)
        self._package_id = int(package_id)
        self._status_id = int(status_id)
        self.validate()

    def validate(self):
        if self._number_of_people <= 0:
            raise ValueError("Number of people must be greater than zero.")
        if not self._reservation_code or not self._reservation_code.strip():
            raise ValueError("Reservation code is required.")
        if self._client_id <= 0 or self._package_id <= 0 or self._status_id <= 0:
            raise ValueError("Client ID, Package ID, and Status ID must be valid positive integers.")

    @property
    def id_reservation(self): return self._id_reservation
    @property
    def package_id(self): return self._package_id
    @property
    def number_of_people(self): return self._number_of_people
    @property
    def reservation_code(self): return self._reservation_code
    @property
    def client_id(self): return self._client_id
    @property
    def status_id(self): return self._status_id

    def __str__(self):
        return f"Reservation {self._reservation_code} | People: {self._number_of_people} | Package ID: {self._package_id}"