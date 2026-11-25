from persistence.connection import open_connection, sql_marker

class PackageDestinationDAO:
    @staticmethod
    def add_destination(package_id: int, destination_id: int):
        conn = None
        try:
            conn = open_connection()
            cursor = conn.cursor()
            marker = sql_marker()
            sql = f"INSERT INTO Package_Destination (package_id, destination_id) VALUES ({marker}, {marker})"
            cursor.execute(sql, (package_id, destination_id))
            conn.commit()
            return True
        except Exception:
            if conn: conn.rollback()
            raise
        finally:
            if conn: conn.close()

    @staticmethod
    def get_destinations_by_package(package_id: int):
        conn = open_connection()
        try:
            cursor = conn.cursor()
            marker = sql_marker()
            sql = f"""
                SELECT d.id, d.name, d.country, d.description, d.status 
                FROM Destination d
                INNER JOIN Package_Destination pd ON d.id = pd.destination_id
                WHERE pd.package_id = {marker}
            """
            cursor.execute(sql, (package_id,))
            rows = cursor.fetchall()
            from domain.destination import Destination
            return [Destination(row[1], row[2], row[3], row[4], id_destination=row[0]) for row in rows]
        finally:
            conn.close()