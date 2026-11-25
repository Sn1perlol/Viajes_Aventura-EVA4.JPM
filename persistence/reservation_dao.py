from persistence.connection import open_connection, sql_marker
from datetime import datetime

class ReservationDAO:
    @staticmethod
    def create_reservation(client_id, package_id, number_of_people, reservation_code, status_id):
        conn = None
        try:
            conn = open_connection()
            cursor = conn.cursor()
            marker = sql_marker()
            
            sql = (f"INSERT INTO Reservation (reservation_date, number_of_people, reservation_code, client_id, package_id, status_id) "
                   f"VALUES ({marker}, {marker}, {marker}, {marker}, {marker}, {marker})")
            
            now = datetime.now().isoformat()
            cursor.execute(sql, (now, number_of_people, reservation_code, client_id, package_id, status_id))
            res_id = cursor.lastrowid
            
            cursor.execute(f"UPDATE Package SET available_slots = available_slots - {marker} WHERE id = {marker}", (number_of_people, package_id))
            
            conn.commit()
            return res_id
        except Exception:
            if conn: conn.rollback()
            raise
        finally:
            if conn: conn.close()