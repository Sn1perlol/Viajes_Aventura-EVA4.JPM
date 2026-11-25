from utils.validators import clear_screen
from persistence.package_dao import PackageDAO

def menu_package():
    while True:
        clear_screen()
        print("===================================")
        print("         AVAILABLE PACKAGES        ")
        print("===================================")
        
        packages = PackageDAO.get_all()
        if not packages:
            print("No packages available at the moment.")
        else:
            for pkg in packages:
                print(pkg)
                
        print("\n0. Back to main menu")
        option = input("\nSelect an option: ").strip()
        
        if option == "0":
            return