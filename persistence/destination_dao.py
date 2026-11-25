from persistence.connection import open_connection, sql_marker
from domain.destination import Destination

class DestinationDAO:
    @staticmethod
    def insert(destination: Destination):
        conn = None
        try:
            conn = open_connection()
            cursor = conn.cursor()
            marker = sql_marker()
            sql = (f"INSERT INTO Destination (name, country, description, status) "
                   f"VALUES ({marker}, {marker}, {marker}, {marker})")
            cursor.execute(sql, (destination.name, destination.country, destination.description, destination.status))
            conn.commit()
            destination._id_destination = cursor.lastrowid
            return destination
        except Exception:
            if conn: conn.rollback()
            raise
        finally:
            if conn: conn.close()

    @staticmethod
    def get_all():
        conn = open_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, country, description, status FROM Destination")
            rows = cursor.fetchall()
            return [Destination(row[1], row[2], row[3], row[4], id_destination=row[0]) for row in rows]
        finally:
            conn.close()