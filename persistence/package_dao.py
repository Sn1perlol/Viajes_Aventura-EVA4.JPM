from persistence.connection import open_connection, sql_marker
from domain.package import Package

class PackageDAO:
    @staticmethod
    def get_all():
        conn = open_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, start_date, end_date, price, available_slots, transport_id, status_id FROM Package")
            rows = cursor.fetchall()
            return [Package(row[1], row[2], row[3], row[4], row[5], row[6], row[7], id_package=row[0]) for row in rows]
        finally:
            conn.close()
            
    @staticmethod
    def get_by_id(package_id):
        conn = open_connection()
        try:
            cursor = conn.cursor()
            marker = sql_marker()
            cursor.execute(f"SELECT id, name, start_date, end_date, price, available_slots, transport_id, status_id FROM Package WHERE id = {marker}", (package_id,))
            row = cursor.fetchone()
            if row is None:
                return None
            return Package(row[1], row[2], row[3], row[4], row[5], row[6], row[7], id_package=row[0])
        finally:
            conn.close()