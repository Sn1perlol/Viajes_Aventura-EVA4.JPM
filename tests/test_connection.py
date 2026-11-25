import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from persistence.create_db import create_tables
from persistence.connection import open_connection

def test_database_connection():
    print("[TEST] Starting database connection test...")
    try:
        create_tables()
        connection = open_connection()
        cursor = connection.cursor()

        if "sqlite" in str(type(connection)).lower():
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
        else:
            cursor.execute("SHOW TABLES;")
            tables = cursor.fetchall()
            
        print("[OK] Connection established.")
        print(f"[OK] Tables found: {[t[0] for t in tables]}")
        connection.close()
        print("[OK] Connection test completed successfully.")
    except Exception as e:
        print(f"[FAIL] Connection test failed: {e}")

if __name__ == "__main__":
    test_database_connection()