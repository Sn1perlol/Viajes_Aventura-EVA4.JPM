from persistence.connection import open_connection, get_engine

def create_tables():
    conn = None
    try:
        conn = open_connection()
        cursor = conn.cursor()
        
        if get_engine() == "sqlite":
            tables = [
                """CREATE TABLE IF NOT EXISTS Client (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL, last_name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE, password_hash TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )""",
                """CREATE TABLE IF NOT EXISTS Transport_Type (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL
                )""",
                """CREATE TABLE IF NOT EXISTS Destination (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL,
                    country TEXT NOT NULL, description TEXT, status TEXT NOT NULL
                )""",
                """CREATE TABLE IF NOT EXISTS Status (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL
                )""",
                """CREATE TABLE IF NOT EXISTS Package (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL,
                    start_date TEXT NOT NULL, end_date TEXT NOT NULL,
                    price REAL NOT NULL, available_slots INTEGER NOT NULL,
                    transport_id INTEGER NOT NULL, status_id INTEGER NOT NULL,
                    FOREIGN KEY (transport_id) REFERENCES Transport_Type(id),
                    FOREIGN KEY (status_id) REFERENCES Status(id)
                )""",
                """CREATE TABLE IF NOT EXISTS Package_Destination (
                    package_id INTEGER NOT NULL, destination_id INTEGER NOT NULL,
                    PRIMARY KEY (package_id, destination_id),
                    FOREIGN KEY (package_id) REFERENCES Package(id) ON DELETE CASCADE,
                    FOREIGN KEY (destination_id) REFERENCES Destination(id) ON DELETE CASCADE
                )""",
                """CREATE TABLE IF NOT EXISTS Reservation (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    reservation_date TEXT NOT NULL, number_of_people INTEGER NOT NULL,
                    reservation_code TEXT NOT NULL UNIQUE, client_id INTEGER NOT NULL,
                    package_id INTEGER NOT NULL, status_id INTEGER NOT NULL,
                    FOREIGN KEY (client_id) REFERENCES Client(id),
                    FOREIGN KEY (package_id) REFERENCES Package(id),
                    FOREIGN KEY (status_id) REFERENCES Status(id)
                )"""
            ]
        else:
            tables = [
                """CREATE TABLE IF NOT EXISTS Client (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    first_name VARCHAR(50) NOT NULL, last_name VARCHAR(50) NOT NULL,
                    email VARCHAR(100) NOT NULL UNIQUE, password_hash VARCHAR(255) NOT NULL,
                    created_at DATETIME NOT NULL
                )""",
                """CREATE TABLE IF NOT EXISTS Transport_Type (
                    id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50) NOT NULL
                )""",
                """CREATE TABLE IF NOT EXISTS Destination (
                    id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100) NOT NULL,
                    country VARCHAR(50) NOT NULL, description TEXT, status VARCHAR(20) NOT NULL
                )""",
                """CREATE TABLE IF NOT EXISTS Status (
                    id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50) NOT NULL
                )""",
                """CREATE TABLE IF NOT EXISTS Package (
                    id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100) NOT NULL,
                    start_date DATETIME NOT NULL, end_date DATETIME NOT NULL,
                    price DECIMAL(10,2) NOT NULL, available_slots INT NOT NULL,
                    transport_id INT NOT NULL, status_id INT NOT NULL,
                    FOREIGN KEY (transport_id) REFERENCES Transport_Type(id),
                    FOREIGN KEY (status_id) REFERENCES Status(id)
                )""",
                """CREATE TABLE IF NOT EXISTS Package_Destination (
                    package_id INT NOT NULL, destination_id INT NOT NULL,
                    PRIMARY KEY (package_id, destination_id),
                    FOREIGN KEY (package_id) REFERENCES Package(id) ON DELETE CASCADE,
                    FOREIGN KEY (destination_id) REFERENCES Destination(id) ON DELETE CASCADE
                )""",
                """CREATE TABLE IF NOT EXISTS Reservation (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    reservation_date DATETIME NOT NULL, number_of_people INT NOT NULL,
                    reservation_code VARCHAR(20) NOT NULL UNIQUE, client_id INT NOT NULL,
                    package_id INT NOT NULL, status_id INT NOT NULL,
                    FOREIGN KEY (client_id) REFERENCES Client(id),
                    FOREIGN KEY (package_id) REFERENCES Package(id),
                    FOREIGN KEY (status_id) REFERENCES Status(id)
                )"""
            ]
            
        for sql in tables:
            cursor.execute(sql)
        conn.commit()
        print("Tables created successfully.")
    except Exception as e:
        if conn: conn.rollback()
        print(f"Error creating tables: {e}")
        raise
    finally:
        if conn: conn.close()