from persistence.package_dao import PackageDAO
from persistence.reservation_dao import ReservationDAO
from persistence.client_dao import ClientDAO
from persistence.status_dao import StatusDAO
import uuid

class BookingService:

    @staticmethod
    def make_reservation(client_email, package_id, number_of_people):
        client = ClientDAO.get_by_email(client_email)
        if not client:
            raise ValueError("Client not found. Please register first.")

        target_package = PackageDAO.get_by_id(package_id)
        if not target_package:
            raise ValueError("Package ID not found.")
        if not target_package.is_available(number_of_people):
            raise ValueError(f"Not enough available slots. Only {target_package.available_slots} left.")

        status = StatusDAO.get_by_name("Pending")
        if not status:
            raise ValueError("Default status 'Pending' is missing from database.")
        status_id = status.id_status

        code = f"RES-{uuid.uuid4().hex[:6].upper()}"

        res_id = ReservationDAO.create_reservation(
            client_id=client.id_client,
            package_id=package_id,
            number_of_people=number_of_people,
            reservation_code=code,
            status_id=status_id
        )
        return code, res_id