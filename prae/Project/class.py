from datetime import datetime, time, timedelta

class Company:
    def __init__(self):
        self.__user_list = []
        self.__simcard_list = []
        self.__package_list = []
    
    def add_user(self, user):
        if isinstance(user, User):
            self.__user_list.append(user)
    
    def add_simcard(self, simcard):
        if isinstance(simcard, Simcard):
            self.__simcard_list.append(simcard)
            
    def add_package(self, package):
        if issubclass(package, Package):
            self.__package_list.append(package)
            
    def search_user_from_id(self, citizen_id):
        for user in self.__user_list:
            if citizen_id == user.citizen_id:
                return user
        return "Not Found"
    
    def search_package_from_phone_number(self, phone_number):
        for simcard in self.__simcard_list:
            if phone_number == simcard.phone_number:
                package_list = []
                if simcard.package != None:
                    package_list.append(simcard.package)
                    package_list.extend([add for add in simcard.additional_list])
                    return package_list
                else:
                    return "No Subscription"
        return "Not Found"               
                
class User:
    def __init__(self, citizen_id, name):
        self.__citizen_id = citizen_id
        self.__name = name
        self.__phone_number_list = []
        
    @property
    def citizen_id(self):
        return self.__citizen_id

class PhoneNumber:
    def __init__(self, number):
        self.__number = number
        self.__package = None
        self.__additional_list = []
        
    @property
    def number(self):
        return self.__number
    
    @property
    def package(self):
        return self.__package
    
    @property
    def additional_list(self):
        return self.__additional_list
        
class PostPaid(PhoneNumber):
    def add_package(self, package):
        if isinstance(package, Monthly):
            self.package = package
        else:
            return "Error"

    def add_additional_package(self, package):
        pass

class PrePaid(PhoneNumber):
    def __init__(self, name):
        Package.__init__(self, name)
        self.__balance = 0
        self.__suspended_date = None
    
    def add_package(self, package):
        if isinstance(package, TopUp):
            self.package = package
        else:
            return "Error"
        
    def add_additional_package(self, package):
        pass    

class Simcard:
	def __init__(self, phone_number, type):
		self.__phone_number = phone_number
		self.__type = type #postpaid or prepaid 

	@property
	def phone_number(self):
		return self.__phone_number

class Package:
    def __init__(self, price, net_speed, net_volume, call_volume, period):
        self.__price = price
        self.__net_speed = net_speed
        self.__net_volume = net_volume
        self.__call_volume = call_volume
        self.__period = period
        self.__billing_date = None
        
class Monthly (Package):
    pass

class AdditionalMonthly (Package):
    pass

class TopUp (Package):
    pass
        
class Roaming (Package):
    def __init__(self, price, net_speed, net_volume, call_volume, billing_date, period):
        Package.__init__(self, price, net_speed, net_volume, call_volume, billing_date, period)
        self.__country_list = []

class Transaction:
    pass

class Bill:
    def __init__(self, total, last_payment_date):
        self.__total = total
        self.__last_payment_date = last_payment_date
        
##################################################################################
dkub = Company()
dkub.add_user(User('1-1101-12345-12-0','Harry Potter'))
dkub.add_user(User('1-1101-12345-13-0','Hermione Jean Granger'))
dkub.add_user(User('1-1101-12345-14-0','Peter Parker'))
dkub.add_user(User('1-1101-12345-15-0','Stephen Curry'))

harry = dkub.search_user_from_id('1-1101-12345-12-0')
hermione= dkub.search_user_from_id('1-1101-12345-13-0')
peter = dkub.search_user_from_id('1-1101-12345-14-0')
stephen = dkub.search_user_from_id('1-1101-12345-15-0')