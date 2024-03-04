from pointhistory import PointsHistory
from booking import Booking
from datetime import datetime
from reward import Reward
class Customer:
    def __init__(self, name, email, phone_number):
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number
        self.__booking_list = []
    
    @property
    def name(self):
        return self.__name
    @property
    def email(self):
        return self.__email
    
    def add_booking(self, booking):
        if not isinstance(booking, Booking):
            return None
        self.__booking_list.append(booking)
        return "Done"
        
class Member(Customer):
    def __init__(self, name, email, phone_number, birthday, nationality):
        super().__init__(name, email, phone_number)
        self.__id = 0
        self.__birthday = birthday
        self.__nationality = nationality
        self.__point = 0
        self.__password = None
        self.__points_history_list = []
        self.__reward_history_list = []

    def __add__(self, amounts):
        if amounts > 0:
            self.__point += amounts
            self.add_points_history(amounts, self.__point)
            return "Success"
        else:
            return "Invalid Amounts"

    def add_points_history(self, amount, point_after):
        points_history =  PointsHistory(amount, point_after, datetime.now)
        self.__points_history_list.append(points_history)
        return "Done"

    def __sub__(self, amounts):
        if self.__point >= amounts > 0:
            self.__point -= amounts
            return "Success"
        else:
            return "Not enough points"

    def check_password(self, password):
        for char in password:
            if char.isnumeric() or char.isalpha() or char == ".":
                continue
            return False

    def add_password(self, password):
        if len(password) >= 8 and self.check_password(password) != False:
            self.__password = password
            return "Success"
        elif len(password) < 8:
            return "Please use a password with at least 8 characters."
        elif self.check_password(password) == False:
            return "Please use passwords that contain only the letters 0-9, a-z, A-Z, or (.)"
        else:
            return "Please use a password with at least 8 characters and only the letters 0-9, a-z, A-Z, or (.)"

    def add_points_history(self, history):
        if isinstance(history, PointsHistory):
            self.__points_history_list.append(history)
        else:
            return "Error"


class PointsHistory:
    def __init__(self, amounts, point_after, datetime):
        self.__amounts = amounts
        self.__point_after = point_after
        self.__datetime = datetime
        self.__reward = None  # Only 1 reward can be redeemed at a time

    def add_reward(self, reward):
        if isinstance(reward, Reward):
            self.__reward = reward
        else:
            return "Error"