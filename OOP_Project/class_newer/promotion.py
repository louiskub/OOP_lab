from datetime import timedelta, date

class Promotion:
    def __init__(self, start_date, end_date):
        self.__start_date = start_date
        self.__end_date = end_date

    def is_expired(self):
        return date.today() > self.__end_date

class PercentCoupon(Promotion):
    def __init__(self, start_date, end_date, code, discount, min_purchase=0):
        super().__init__(start_date, end_date)
        self.__discount = discount # % 40
        self.__code = code
        self.__min_purchase = min_purchase
    @property
    def code(self):
        return self.__code
    
    def get_discount(self, total):
        return total*(self.__discount)/100

class AmountCoupon(Promotion):
    def __init__(self, start_date, end_date, code, discount, min_purchase):
        super().__init__(start_date, end_date)
        self.__code = code
        self.__discount = discount
        self.__min_purchase = min_purchase

    @property
    def code(self):
        return self.__code
    @property
    def min_purchase(self):
        return self.__min_purchase
    def get_discount(self):
        return self.__discount
    
if '__main__' == __name__:
    coupon = AmountCoupon(date.today(), date.today(), "louis", 200, 100)
    print(coupon.discount)
