from persistence.connection import open_connection, sql_marker
from domain.status import Status

class StatusDAO:
    @staticmethod
    def get_all():
        conn = open_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name FROM Status")
            return [Status(row[1], id_status=row[0]) for row in cursor.fetchall()]
        finally:
            conn.close()
            
    @staticmethod
    def get_by_name(name):
        conn = open_connection()
        try:
            cursor = conn.cursor()
            marker = sql_marker()
            cursor.execute(f"SELECT id, name FROM Status WHERE name = {marker}", (name,))
            row = cursor.fetchone()
            if row:
                return Status(row[1], id_status=row[0])
            return None
        finally:
            conn.close()