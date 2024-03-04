from time import timedelta

class Promotion:
    def __init__(self, discount, start_date, end_date, min_purchase):
        self.__discount = discount
        self.__start_date = start_date
        self.__end_date = end_date
        self.__min_purchase = min_purchase

    def get_available_date(self):
        date_list = [
            self.__start_date + timedelta(days=x)
            for x in range((self.__end_date - self.__start_date).days + 1)
        ]
        return date_list


class SpecialCoupon(Promotion):
    def __init__(self, code, type, discount, exp_date, time_delta):
        super().__init__()
