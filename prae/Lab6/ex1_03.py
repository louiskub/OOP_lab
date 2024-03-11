from datetime import datetime, time, timedelta

# Class Code
class User:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__account_list = []
    
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def account_list(self):
        return self.__account_list
    
    def add_account(self, account):
        if isinstance(account, Account):
            self.__account_list.append(account)
        
class Account:
    def __init__(self, id, user, balance, card = None):
        self.__id = id
        self.__user = user
        self.__balance = balance
        self.__card = card
        self.__transaction_list = []
        self.__max_per_day = 40000
    
    @property
    def id(self):
        return self.__id
        
    @property
    def user(self):
        return self.__user
    
    @property
    def card(self):
        return self.__card
    
    @property
    def transaction_list(self):
        return self.__transaction_list
    
    def reset_max_per_day(self):
        self.__max_per_day = 40000
        
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
    
    def get_max_per_day(self):
        return self.__max_per_day
    
    def set_max_per_day(self, max_per_day):
        if max_per_day >= 0:
            self.__max_per_day = max_per_day
                    
    balance = property(get_balance, set_balance)
    max_per_day = property(get_max_per_day, set_max_per_day) 
   
class Card:
    def __init__(self, id, pin):
        self.__id = id
        self.__pin = pin
    
    @property
    def id(self):
        return self.__id
    
    @property
    def pin(self):
        return self.__pin

class Bank:
    __atm_card_fee = 150
    
    def __init__(self):
        self.__user_list = []
        self.__atm_list = []
        
    @property
    def user_list(self):
        return self.__user_list
    
    @property
    def atm_list(self):
        return self.__atm_list
    
    @property
    def atm_card_fee(self):
        return self.__atm_card_fee
       
    def add_user(self, user):
        if isinstance(user, User):
            self.__user_list.append(user)
        
    def add_atm(self, atm):
        if isinstance(atm, ATM):
            self.__atm_list.append(atm)                      

class Transaction:
    def __init__(self, type, amounts, date_time, atm_id, transfer_account = None):
        self.__type = type
        self.__amounts = amounts
        self.__date_time = date_time
        self.__atm_id = atm_id
        self.__transfer_account = transfer_account
    
    def __str__(self):
        return self.__date_time.strftime('%Y-%m-%d %H:%M:%S') + ' - ' + self.__type + " - ATM:" + self.__atm_id + " - " + str(self.__amounts)
    
    @property
    def type(self):
        return self.__type
    
    @property
    def amounts(self):
        return self.__amounts
    
    @property
    def date_time(self):
        return self.__date_time
    
    @property
    def transfer_account(self):
        return self.__transfer_account 
        
class ATM:
    def __init__(self, machine_id, balance = 1000000):
        self.__machine_id = machine_id
        self.__balance = balance
        
    @property
    def machine_id(self):
        return self.__machine_id
    
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, balance):
        if balance > 0:
            self.__balance = balance
            
            
    balance = property(get_balance, set_balance)     
    
    # TODO 2 : เขียน method ที่ทำหน้าที่สอดบัตรเข้าเครื่อง ATM มี parameter 3 ตัว ได้แก่ 1) instance ของธนาคาร
    # TODO     2) instance ของ atm_card 3) entered Pin ที่ user input ให้เครื่อง ATM
    # TODO     return ถ้าบัตร และ Pin ถูกต้องจะได้ instance ของ account คืนมา ถ้าไม่ถูกต้องได้เป็น None
    # TODO     ควรเป็น method ของเครื่อง ATM
    def insert_card(self, bank, card, pin):
        if isinstance(self, ATM) and isinstance(bank, Bank):
            if card.pin == pin:
                for user in bank.user_list:
                    for account in user.account_list:
                        if card == account.card:
                            return account
                              
    # TODO 3 : เขียน method ที่ทำหน้าที่ฝากเงิน โดยรับ parameter 2 ตัว คือ 
    # TODO     1) instance ของ account 2) จำนวนเงิน
    # TODO     การทำงาน ให้เพิ่มจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
    # TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
    # TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0                
    def deposit(self, my_account, amounts):
        if isinstance(my_account, Account):
            if amounts > 0:
                #before = my_account.balance
                self.balance += amounts
                my_account.balance += amounts
                my_account.transaction_list.append(Transaction('D', amounts, datetime.now(), self.machine_id))
                return "Success"
            return "Error"
        else :
            return "Error"
    
    #TODO 4 : เขียน method ที่ทำหน้าที่ถอนเงิน โดยรับ parameter 2 ตัว คือ 
    # TODO     1) instance ของ account 2) จำนวนเงิน
    # TODO     การทำงาน ให้ลดจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
    # TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
    # TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี
    def withdraw(self, my_account, amounts):
        if isinstance(my_account, Account):
            if 0 < amounts <= my_account.balance and amounts <= my_account.max_per_day and amounts <= self.balance:
                #before = my_account.balance
                self.balance -= amounts
                my_account.balance -= amounts
                my_account.max_per_day -= amounts
                print(my_account.max_per_day)
                my_account.transaction_list.append(Transaction('W', amounts, datetime.now(), self.machine_id))
                return "Success"
            return "Error"
        else :
            return "Error"
    
    #TODO 5 : เขียน method ที่ทำหน้าที่โอนเงิน โดยรับ parameter 3 ตัว คือ 
    # TODO     1) instance ของ account ตนเอง 2) instance ของ account ที่โอนไป 3) จำนวนเงิน
    # TODO     การทำงาน ให้ลดจำนวนเงินในบัญชีตนเอง และ เพิ่มเงินในบัญชีคนที่โอนไป และ สร้าง transaction ลงในบัญชี
    # TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
    # TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี
    def transfer(self, my_account, transfer_account, amounts):
        if isinstance(my_account, Account) and isinstance(transfer_account, Account):
            if 0 < amounts <= my_account.balance and amounts <= my_account.max_per_day:
                my_account.balance -= amounts
                my_account.max_per_day -= amounts
                print(my_account.max_per_day)
                transfer_account.balance += amounts
                my_account.transaction_list.append(Transaction('T', amounts, datetime.now(), self.machine_id, transfer_account))
                transfer_account.transaction_list.append(Transaction('T', amounts, datetime.now(), self.machine_id))
                return "Success"
            return "Error"
        else :
            return "Error"                                     
            
##################################################################################

# กำหนดรูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, หมายเลขบัญชี, จำนวนเงิน, หมายเลข ATM ]}
user_info = {'1-1101-12345-53-0':['Harry Potter','1234567890', 20000, '12345'],
             '1-1101-12345-54-0':['Hermione Jean Granger','0987654321', 1000,'12346']}
atm = {'1001':1000000,'1002':200000}

# TODO 1 : จากข้อมูลใน user ให้สร้าง instance โดยมีข้อมูล
# TODO :   key:value โดย key เป็นรหัสบัตรประชาชน และ value เป็นข้อมูลของคนนั้น ประกอบด้วย
# TODO :   [ชื่อ, หมายเลขบัญชี, หมายเลขบัตร ATM, จำนวนเงินในบัญชี]
# TODO :   return เป็น instance ของธนาคาร
# TODO :   และสร้าง instance ของเครื่อง ATM จำนวน 2 เครื่อง

bank = Bank()

user1 = User('1-1101-12345-53-0', 'Harry Potter')
user2 = User('1-1101-12345-54-0', 'Hermione Jean Granger')

harry_card = Card('12345', '1234')
hermione_card = Card('12346', '1234')

harry_account = Account('1234567890', user1, 20000, harry_card)
hermione_account = Account('0987654321', user2, 1000, hermione_card)

atm1 = ATM('1001', 1000000)
atm2 = ATM('1002', 200000)

user1.add_account(harry_account)
user2.add_account(hermione_account)
bank.add_user(user1)
bank.add_user(user2)
bank.add_atm(atm1)
bank.add_atm(atm2)

if datetime.now().time() == time(0, 0, 0):
    for user in bank.user_list:
        for account in user.account_list:
            account.reset_max_per_day()

# Test case #1 : ทดสอบ การ insert บัตร ที่เครื่อง atm เครื่องที่ 1 โดยใช้บัตร atm ของ harry
# และ Pin ที่รับมา เรียกใช้ function หรือ method จากเครื่อง ATM 
# ผลที่คาดหวัง : พิมพ์ หมายเลขบัตร ATM อย่างถูกต้อง และ หมายเลข account ของ harry อย่างถูกต้อง
# Ans : 12345, 1234567890, Success
print("Test case #1 :")
if atm1.insert_card(bank, harry_card, "1234") != None:
    print(atm1.insert_card(bank, harry_card, "1234").card.id, atm1.insert_card(bank, harry_card, "1234").id)
else:
    print(atm1.insert_card(bank, harry_card, "1234"))
print('')


# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# Hermione account before test : 1000
# Hermione account after test : 2000
print("Test case #2 :")
print("Hermione account before test : " + str(hermione_account.balance))
atm2.deposit(hermione_account, 1000)
print("Hermione account after test : " + str(hermione_account.balance))
print('')


# Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
# ผลที่คาดหวัง : แสดง Error
print("Test case #3 :")
print(atm2.deposit(hermione_account, -1))
print('')


# Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# ให้เรียกใช้ method ที่ทำการถอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# Hermione account before test : 2000
# Hermione account after test : 1500
print("Test case #4 :")
print("Hermione account before test : " + str(hermione_account.balance))
atm2.withdraw(hermione_account, 500)
print("Hermione account after test : " + str(hermione_account.balance))
print('')


# Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
# ผลที่คาดหวัง : แสดง Error
print("Test case #5 :")
print(atm2.withdraw(hermione_account, 2000))
print('')


# Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# Harry account before test : 20000
# Harry account after test : 10000
# Hermione account before test : 1500
# Hermione account after test : 11500
print("Test case #6 :")
print("Harry account before test : " + str(harry_account.balance))
print("Hermione account before test : " + str(hermione_account.balance))
atm2.transfer(harry_account, hermione_account, 10000)
print("Harry account after test : " + str(harry_account.balance))
print("Hermione account after test : " + str(hermione_account.balance))
print('')


# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด 
# กำหนดให้เรียกใช้ method __str__() เพื่อใช้คำสั่งพิมพ์ข้อมูลจาก transaction ได้
# ผลที่คาดหวัง
# Hermione transaction : D-ATM:1002-1000-2000
# Hermione transaction : W-ATM:1002-500-1500
# Hermione transaction : T-ATM:1002-10000-11500
print("Test case #7 :")
for transaction in hermione_account.transaction_list:
    print(transaction)