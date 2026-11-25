from persistence.connection import open_connection, sql_marker
from datetime import datetime, timedelta

def seed_data():
    conn = None
    try:
        conn = open_connection()
        cursor = conn.cursor()
        marker = sql_marker()

        cursor.execute("SELECT COUNT(*) FROM Status")
        if cursor.fetchone()[0] == 0:
            cursor.execute(f"INSERT INTO Status (name) VALUES ({marker})", ('Pending',))
            cursor.execute(f"INSERT INTO Status (name) VALUES ({marker})", ('Confirmed',))
            cursor.execute(f"INSERT INTO Status (name) VALUES ({marker})", ('Cancelled',))

        cursor.execute("SELECT COUNT(*) FROM Transport_Type")
        if cursor.fetchone()[0] == 0:
            cursor.execute(f"INSERT INTO Transport_Type (name) VALUES ({marker})", ('Flight',))
            cursor.execute(f"INSERT INTO Transport_Type (name) VALUES ({marker})", ('Bus',))

        cursor.execute("SELECT COUNT(*) FROM Destination")
        if cursor.fetchone()[0] == 0:
            cursor.execute(f"INSERT INTO Destination (name, country, description, status) VALUES ({marker}, {marker}, {marker}, {marker})", 
                           ('Patagonia', 'Argentina', 'Beautiful mountains', 'active'))
            cursor.execute(f"INSERT INTO Destination (name, country, description, status) VALUES ({marker}, {marker}, {marker}, {marker})", 
                           ('Machu Picchu', 'Peru', 'Inca ruins', 'active'))

        cursor.execute("SELECT COUNT(*) FROM Package")
        if cursor.fetchone()[0] == 0:
            start = (datetime.now() + timedelta(days=10)).isoformat()
            end = (datetime.now() + timedelta(days=17)).isoformat()
            cursor.execute(
                f"INSERT INTO Package (name, start_date, end_date, price, available_slots, transport_id, status_id) "
                f"VALUES ({marker}, {marker}, {marker}, {marker}, {marker}, {marker}, {marker})",
                ("Adventure in Patagonia", start, end, 1500.00, 20, 1, 1)
            )
            pkg1_id = cursor.lastrowid
            
            cursor.execute(
                f"INSERT INTO Package (name, start_date, end_date, price, available_slots, transport_id, status_id) "
                f"VALUES ({marker}, {marker}, {marker}, {marker}, {marker}, {marker}, {marker})",
                ("Machu Picchu Express", start, end, 850.00, 15, 1, 1)
            )
            pkg2_id = cursor.lastrowid

            cursor.execute(f"INSERT INTO Package_Destination (package_id, destination_id) VALUES ({marker}, {marker})", (pkg1_id, 1))
            cursor.execute(f"INSERT INTO Package_Destination (package_id, destination_id) VALUES ({marker}, {marker})", (pkg2_id, 2))

        conn.commit()
    except Exception as e:
        if conn: conn.rollback()
        print(f"Error seeding data: {e}")
        raise
    finally:
        if conn: conn.close()