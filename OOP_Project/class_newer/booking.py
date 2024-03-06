from service import Cabana, Ticket, Locker, Towel
class Booking:
    __ID = 100000

    def __init__(self, customer, order, booking_date):
        self.__id = Booking.__ID
        self.__customer = customer
        self.__order = order
        self.__booking_date = booking_date
        self.__status = False
        Booking.__ID += 1
    
    @property
    def id(self):
        return self.__id
    @property
    def order(self):
        return self.__order
    @property
    def customer(self):
        return self.__customer
    @property
    def order_datetime(self):
        return self.__booking_date

    def update_status(self):
        self.__status = True
        return "Done"

    def to_dict(self):
        return {
            "booking_id": self.__id,
            "customer": self.__customer.to_dict(),
            "order": self.__order.to_dict(),
            "booking_date": self.__booking_date,
            "status": self.__status
        }
    def get_booking_detail(self):
        order = self.__order
        customer = self.__customer
        return {"detail": order, "customer": [customer.name, customer.email]}
