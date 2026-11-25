import hashlib
import secrets

class Client:
    def __init__(self, first_name, last_name, email, password, id_client=None, is_hashed=False):
        self._id_client = id_client
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        
        if is_hashed:
            self._password_hash = password
        else:
            self._password_hash = self._hash_password(password)
            
        self.validate()

    def _hash_password(self, password):
        if not password or not password.strip():
            raise ValueError("Password cannot be empty.")
        salt = secrets.token_bytes(16)
        pwd_hash = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 600000)
        return salt.hex() + ":" + pwd_hash.hex()

    def validate(self):
        if not self._first_name or not self._first_name.strip():
            raise ValueError("First name cannot be empty.")
        if not self._last_name or not self._last_name.strip():
            raise ValueError("Last name cannot be empty.")
        if "@" not in self._email or "." not in self._email:
            raise ValueError("Invalid email format.")
        if not self._password_hash:
            raise ValueError("Password hash is required.")

    @property
    def id_client(self): return self._id_client
    @property
    def first_name(self): return self._first_name
    @property
    def last_name(self): return self._last_name
    @property
    def email(self): return self._email
    @property
    def password_hash(self): return self._password_hash

    def __str__(self):
        return f"Client({self._id_client}: {self._first_name} {self._last_name} - {self._email})"