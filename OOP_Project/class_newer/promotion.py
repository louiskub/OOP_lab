from time import timedelta

class Promotion:
    def __init__(self, start_date, end_date, discount):
        self.__start_date = start_date
        self.__end_date = end_date
        self.__discount = discount
    def get_available_date(self):
        date_list = [
            self.__start_date + timedelta(days=x)
            for x in range((self.__end_date - self.__start_date).days + 1)
        ]
        return date_list
    def cal_new_total(self, total):
        return

class PercentCoupon(Promotion):
    def __init__(self, start_date, end_date, code, discount):
        super().__init__(start_date, end_date, discount)
        self.__code = code

    def cal_new_total(self, total):
        return total*(100-self.discount)/100

class AmountCoupon(Promotion):
    def __init__(self, code, discount, min_purchase, start_date: date, end_date : date):
        self.__code = code
        self.__discount = discount
        self.__end_date = end_date
        self.__min_purchase = min_purchase  # ยอดซื้อขั้นต่ำ
    
    def is_expired(self):
        today = datetime.now().date()
        return today > self.__end_date

    @property
    def code(self):
        return self.__code
    
    @property
    def discount(self):
        return self.__discount
    
    @property
    def min_purchase(self):
        return self.__min_purchase
    
    def get_discount_amount(self):
        return self.__discount