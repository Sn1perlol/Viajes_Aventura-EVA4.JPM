class Destination:
    def __init__(self, name, country, description, status="active", id_destination=None):
        self._id_destination = id_destination
        self._name = name
        self._country = country
        self._description = description
        self._status = status
        self.validate()

    def validate(self):
        if not self._name or not self._country:
            raise ValueError("Destination name and country are required.")
        if self._status not in ["active", "inactive"]:
            raise ValueError("Status must be 'active' or 'inactive'.")

    @property
    def id_destination(self): return self._id_destination
    @property
    def name(self): return self._name
    @property
    def country(self): return self._country
    @property
    def description(self): return self._description
    @property
    def status(self): return self._status

    def __str__(self):
        return f"{self._name} ({self._country})"