from services.booking_service import BookingService
from utils.validators import clear_screen, request_data, validate_positive_int, validate_email
from persistence.package_dao import PackageDAO
from persistence.package_destination_dao import PackageDestinationDAO

def menu_reservation():
    while True:
        clear_screen()
        print("===================================")
        print("       BOOKING MANAGEMENT          ")
        print("===================================")
        print("1. View available packages")
        print("2. Make a new reservation")
        print("0. Back to main menu")
        
        option = input("\nSelect an option: ").strip()
        clear_screen()
        
        if option == "0":
            return
        elif option == "1":
            packages = PackageDAO.get_all()
            print("--- AVAILABLE PACKAGES ---")
            if not packages:
                print("No packages available.")
            else:
                for pkg in packages:
                    print(f"\n{pkg}")
                    destinations = PackageDestinationDAO.get_destinations_by_package(pkg.id_package)
                    if destinations:
                        dest_names = ", ".join([d.name for d in destinations])
                        print(f"   -> Destinations: {dest_names}")
                    else:
                        print("   -> Destinations: Not assigned yet.")
            input("\nPress Enter to continue...")
            
        elif option == "2":
            try:
                email = request_data("Client Email: ", validate_email)
                package_id = request_data("Package ID: ", lambda v: validate_positive_int(v, "Package ID"))
                people = request_data("Number of People: ", lambda v: validate_positive_int(v, "Number of People"))
                
                code, res_id = BookingService.make_reservation(email, package_id, people)
                
                print(f"\n[SUCCESS] Reservation created!")
                print(f"Reservation ID: {res_id}")
                print(f"Code: {code}")
            except Exception as e:
                print(f"\n[ERROR] Could not complete reservation: {e}")
            input("\nPress Enter to continue...")