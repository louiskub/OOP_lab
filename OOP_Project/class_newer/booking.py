from service import OrderDetail, Cabana, Ticket, Locker, Towel

class Order:
    def __init__(self, visit_date):
        self.__visit_date = visit_date
        self.__order_detail = []
        self.__total = 0
        self.__promotion = None

    def __str__(self):
        return f"{[order for order in self.__order_detail]}\nTOTAL: {self.__total}"
    @property
    def visit_date(self):
        return self.__visit_date
    @property
    def order_detail_list(self):
        return self.__order_detail_list
    @property
    def total(self):
        total = 0
        for items in self.__order_detail:
            total += items.total_price
        self.__total = total
        return self.__total
    
    def add_item(self, item) : # Press the add button
        if isinstance(item, Cabana):
            for items in self.__order_detail:
                if isinstance(items.item, Cabana):
                    return self
        elif isinstance(item, (Locker, Towel, Ticket)):
            for items in self.__order_detail:
                if items.item == item:
                    items + 1
                    return self
        self.__order_detail.append(OrderDetail(item))         
        return self
    
    def remove_item(self, item) : # Press the reduce button
        for items in self.__order_detail:
            if item == items.item:
                items - 1
                if items.amount == 0:
                    self.__order_detail.remove(items)
                return self
        return self

    def check_still_available(self) -> bool:
        for order_detail in self.__order_detail_list:
            item = order_detail.item
            if isinstance(item, Cabana):
                return not item.is_reseve  # ถ้าจองแล้ว = ไม่ว่าง
            elif not isinstance(item, Ticket):
                return item.remaining_amount >= order_detail.amount
        return True

    def reserve(self):
        for order_detail in self.__order_detail_list:
            item = order_detail.item
            if isinstance(item, Cabana):
                item.is_reseve = True
            elif not isinstance(self.__item, Ticket):
                item.remaining_amount -= order_detail.amount
        return "Done"
    
    def cancel_reseve(self):
        for order_detail in self.__order_detail_list:
            item = order_detail.item
            if isinstance(item, Cabana):
                item.is_reseve = False
            elif not isinstance(self.__item, Ticket):
                item.remaining_amount += order_detail.amount
        return "Done"

    def show_order_detail(self):
        return [detail.order_detail_dict() for detail in self.__order_detail_list]

class Booking:
    def __init__(self, customer, booking_id, order, order_datetime):
        self.__customer = customer
        self.__booking_id = booking_id
        self.__order = order
        self.__order_datetime = order_datetime
        self.__status = False  # ispaid ?

    @property
    def booking_id(self):
        return self.__booking_id
    @property
    def order(self):
        return self.__order
    @property
    def customer(self):
        return self.__customer

    @property
    def order_datetime(self):
        return self.__order_datetime

    def order_date_to_string(self):
        return self.__order_datetime.date()

    def update_status(self):
        self.__status = True
        return "Done"

    def get_booking_detail(self):
        order = self.__order
        customer = self.__customer
        return {"detail": order, "customer": [customer.name, customer.email]}
