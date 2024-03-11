from datetime import datetime, time, timedelta

date1 = datetime(2024, 1, 27, 10, 0, 0)
date2 = datetime(2024, 1, 28, 12, 30, 0)
date3 = datetime(2024, 1, 29, 13, 30, 0)

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
    
    @property
    def max_per_day(self):
        return self.__max_per_day   
    
    @ property    
    def balance(self):
        return self.__balance
    
    def add_transaction(self, transaction):
        self.__transaction_list.append(transaction)
    
    def check_max_per_day(self, transaction):
        self.__max_per_day = 40000
        target_date = transaction.date_time.date()
        for trans in self.__transaction_list:
            if trans.date_time.date() == target_date:
                if trans.type == 'W' or (trans.type == 'T' and self != trans.target_account):
                    self.__max_per_day -= trans.amounts
        if self.__max_per_day >= transaction.amounts and self != transaction.target_account:
            self.__max_per_day -= transaction.amounts
            return True
        return False                     
                
    def rebalance(self, transaction):
        if isinstance(transaction, Transaction):
            if transaction.type == 'D':
                self.__balance += transaction.amounts
            elif transaction.type == 'W' and transaction.amounts <= self.__balance and self.check_max_per_day(transaction) == True:
                self.__balance -= transaction.amounts
            elif transaction.type == 'T':
                if self != transaction.target_account and transaction.amounts <= self.__balance and self.check_max_per_day(transaction) == True:
                    self.__balance -= transaction.amounts    
                elif self == transaction.target_account:
                    self.__balance += transaction.amounts
                else:
                    return "Error"
            else:
                return "Error"
            transaction.total = self.__balance
            self.add_transaction(transaction)
            return "Success"
        return "Invalid Transaction"             
   
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
    def __init__(self, atm_id, type, amounts, date_time, target_account = None):
        self.__type = type
        self.__amounts = amounts
        self.__date_time = date_time
        self.__atm_id = atm_id
        self.__target_account = target_account
        self.__total = None
    
    def __str__(self):
        return f"{self.__date_time.strftime('%d-%m-%Y %H:%M:%S')} -> {self.__type}-ATM:{self.__atm_id}-{self.__amounts} -> Balance = {self.__total}"
    
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
    def target_account(self):
        return self.__target_account
            
    def get_total(self):
        return self.__total
    
    def set_total(self, balance):
        if balance >= 0:
            self.__total = balance
            
    total = property(get_total, set_total) 
        
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
        if balance >= 0:
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
    def deposit(self, account, amounts):
        if isinstance(account, Account) and amounts > 0:
            if account.rebalance(Transaction(self.__machine_id, 'D', amounts, datetime.now())) == "Success":
                self.__balance += amounts
                return "Success"
            return "Error"
        return "Error"
    
    #TODO 4 : เขียน method ที่ทำหน้าที่ถอนเงิน โดยรับ parameter 2 ตัว คือ 
    # TODO     1) instance ของ account 2) จำนวนเงิน
    # TODO     การทำงาน ให้ลดจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
    # TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
    # TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี
    def withdraw(self, account, amounts):
        if isinstance(account, Account) and 0 < amounts <= self.balance:
            if account.rebalance(Transaction(self.__machine_id, 'W', amounts, datetime.now())) == "Success":
                self.__balance -= amounts
                return "Success"
            return "Error"
        return "Error"
    
    #TODO 5 : เขียน method ที่ทำหน้าที่โอนเงิน โดยรับ parameter 3 ตัว คือ 
    # TODO     1) instance ของ account ตนเอง 2) instance ของ account ที่โอนไป 3) จำนวนเงิน
    # TODO     การทำงาน ให้ลดจำนวนเงินในบัญชีตนเอง และ เพิ่มเงินในบัญชีคนที่โอนไป และ สร้าง transaction ลงในบัญชี
    # TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
    # TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี
    def transfer(self, account, target_account, amounts):
        if isinstance(account, Account) and isinstance(target_account, Account) and amounts > 0:
            if account.rebalance(Transaction(self.machine_id, 'T', amounts, datetime.now(), target_account)) == "Success":
                target_account.rebalance(Transaction(self.machine_id, 'T', amounts, datetime.now(), target_account))
                return "Success"
            return "Error"
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

# print(f"Balance1 = {harry_account.balance}")
# print(f"Max1 = {harry_account.max_per_day}\n")
# print(atm2.deposit(harry_account, 2000))
# print(atm2.withdraw(harry_account, 500))
# print(f"Balance2 = {harry_account.balance}")
# print(f"Max2 = {harry_account.max_per_day}\n")
# print(atm2.transfer(harry_account, hermione_account, 4000))
# print(f"Balance3 = {harry_account.balance}")
# print(f"Max3 = {harry_account.max_per_day}\n")
# print(atm1.withdraw(hermione_account, 100))
# print(f"BalanceHermione = {hermione_account.balance}")
# print(f"MaxHermione = {hermione_account.max_per_day}\n")
# for trans in harry_account.transaction_list:
#     print(trans)
# print('')
# for trans in hermione_account.transaction_list:
#     print(trans)
    
    
# Test case #1 : ทดสอบ การ insert บัตร ที่เครื่อง atm เครื่องที่ 1 โดยใช้บัตร atm ของ harry
# และ Pin ที่รับมา เรียกใช้ function หรือ method จากเครื่อง ATM 
# ผลที่คาดหวัง : พิมพ์ หมายเลขบัตร ATM อย่างถูกต้อง และ หมายเลข account ของ harry อย่างถูกต้อง
# Ans : 12345, 1234567890, Success
print("Test case #1 :")
if atm1.insert_card(bank, harry_card, "1234") != None:
    print(atm1.insert_card(bank, harry_card, "1234").card.id, atm1.insert_card(bank, harry_card, "1234").id, "Success")
else:
    print(atm1.insert_card(bank, harry_card, "1234"))
print('')


# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# Hermione account before test : 1000
# Hermione account after test : 2000
print("Test case #2 :")
print(f"Hermione account before test : {hermione_account.balance}")
atm2.deposit(hermione_account, 1000)
print(f"Hermione account after test : {hermione_account.balance}")
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
print(f"Hermione account before test : {hermione_account.balance}")
atm2.withdraw(hermione_account, 500)
print(f"Hermione account after test : {hermione_account.balance}")
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
print(f"Harry account before test : {harry_account.balance}")
print(f"Hermione account before test : {hermione_account.balance}")
atm2.transfer(harry_account, hermione_account, 10000)
print(f"Harry account after test : {harry_account.balance}")
print(f"Hermione account after test : {hermione_account.balance}")
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
print('')