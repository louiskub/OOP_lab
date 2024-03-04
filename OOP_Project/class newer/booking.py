from service import OrderDetail, Cabana, Ticket


class Order:
    def __init__(self, visit_date, coupon):
        self.__visit_date = visit_date
        self.__order_detail_list = []
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

    def add_order_detail(self, item):
        for order_detail in self.__order_detail_list:
            if order_detail.item == item:
                order_detail.amount += 1
                return "Done"
        self.__selected_item_list.append(order_detail)
        return "Done"

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
