class Status:
    def __init__(self, name, id_status=None):
        self._id_status = id_status
        self._name = name
        self.validate()

    def validate(self):
        if not self._name or not self._name.strip():
            raise ValueError("Status name cannot be empty.")

    @property
    def id_status(self): return self._id_status
    @property
    def name(self): return self._name

    def __str__(self):
        return f"{self._name}"