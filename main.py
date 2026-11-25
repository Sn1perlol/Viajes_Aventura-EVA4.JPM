import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from persistence.create_db import create_tables
from persistence.seed_data import seed_data
from menus.menu_client import menu_client
from menus.menu_reservation import menu_reservation

def main():
    create_tables()
    seed_data()
    
    while True:
        print("\n=== TRAVEL AGENCY SYSTEM ===")
        print("1. Client Management")
        print("2. Reservation Menu")
        print("0. Exit")
        option = input("\nOption: ").strip()
        
        if option == "1":
            menu_client()
        elif option == "2":
            menu_reservation()
        elif option == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()