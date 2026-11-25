from persistence.connection import open_connection, sql_marker
from domain.client import Client
from datetime import datetime

class ClientDAO:
    @staticmethod
    def insert(client: Client):
        conn = None
        try:
            conn = open_connection()
            cursor = conn.cursor()
            marker = sql_marker()
            
            sql = (f"INSERT INTO Client (first_name, last_name, email, password_hash, created_at) "
                   f"VALUES ({marker}, {marker}, {marker}, {marker}, {marker})")
            
            now = datetime.now().isoformat()
            cursor.execute(sql, (client.first_name, client.last_name, client.email, client.password_hash, now))
            conn.commit()
            
            client._id_client = cursor.lastrowid
            return client
        except Exception:
            if conn: conn.rollback()
            raise
        finally:
            if conn: conn.close()

    @staticmethod
    def get_by_email(email: str):
        conn = open_connection()
        try:
            cursor = conn.cursor()
            marker = sql_marker()
            cursor.execute(f"SELECT id, first_name, last_name, email, password_hash FROM Client WHERE email = {marker}", (email,))
            row = cursor.fetchone()
            if row is None:
                return None
            return Client(row[1], row[2], row[3], row[4], id_client=row[0], is_hashed=True)
        finally:
            conn.close()