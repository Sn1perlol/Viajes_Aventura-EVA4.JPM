from utils.validators import clear_screen, request_data, validate_email, validate_required
from persistence.client_dao import ClientDAO
from domain.client import Client

def menu_client():
    while True:
        clear_screen()
        print("===================================")
        print("       CLIENT MANAGEMENT           ")
        print("===================================")
        print("1. Register a new client")
        print("0. Back to main menu")
        
        option = input("\nSelect an option: ").strip()
        clear_screen()
        
        if option == "0":
            return
        elif option == "1":
            try:
                first_name = request_data("First Name: ", lambda v: validate_required(v, "First Name"))
                last_name = request_data("Last Name: ", lambda v: validate_required(v, "Last Name"))
                email = request_data("Email: ", validate_email)
                password = request_data("Password: ", lambda v: validate_required(v, "Password"))
                
                new_client = Client(first_name, last_name, email, password)
                ClientDAO.insert(new_client)
                print(f"\n[SUCCESS] Client registered with ID: {new_client.id_client}")
            except Exception as e:
                print(f"\n[ERROR] Could not register client: {e}")
            input("\nPress Enter to continue...")