from datetime import timedelta, date

class Promotion:
    def __init__(self, start_date, end_date):
        self.__start_date = start_date
        self.__end_date = end_date

    def is_expired(self):
        return date.today() > self.__end_date

class PercentCoupon(Promotion):
    def __init__(self, start_date, end_date, code, discount, min_purchase=0, max_discount=3000):
        super().__init__(start_date, end_date)
        self.__discount = discount # % 40 = 0.4
        self.__code = code
        self.__min_purchase = min_purchase
        self.__max_discount = max_discount
    @property
    def code(self):
        return self.__code
    @property
    def min_purchase(self):
        return self.__min_purchase # optional
    # @property
    # def max_discount(self):     #optional
    #     return self.__max_discount
    def get_discount(self, total):
        discount = int(self.__discount * total)
        return discount if discount <= self.__max_discount else self.__max_discount

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
    def get_discount(self, total):
        return self.__discount
    
if '__main__' == __name__:
    coupon = AmountCoupon(date.today(), date.today(), "louis", 200, 100)
    print(coupon.discount)
