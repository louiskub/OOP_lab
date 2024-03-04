class Order:
    def __init__(self, visit_date, coupon):
        self.__visit_date = visit_date
        self.__selected_item_list = []
        self.__total = 0
        self.__coupon = None

    @property
    def visit_date(self):
        return self.__visit_date
    @property
    def selected_item_list(self):
        return self.__selected_item_list   
    @property
    def total(self):
        return self.__total
    def add_select(self, lst):
        self.__selected_item_list = lst

class Booking :
    def __init__(self, customer, booking_id, order, order_datetime):
        self.__customer = customer
        self.__booking_id = booking_id
        self.__order = order
        self.__order_datetime = order_datetime
        self.__status = False #ispaid ?
        
    @property
    def booking_id(self):
        return self.__booking_id
    @property
    def order(self):
        return self.__order
    @property
    def customer(self):
        return self.__customer
    
    def update_status(self):
        self.__status = True
        return "Done" 
    
    def get_booking_detail(self):
        order = self.__order
        customer = self.__customer
        return {"detail": order, "customer": [customer.name, customer.email]}


