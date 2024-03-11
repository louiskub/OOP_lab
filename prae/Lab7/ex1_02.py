# Class Code
class Bank:
    def __init__(self, name):
        self.__name = name
        self.__user_list = []
        self.__atm_list = []
        self.__seller_list = []
    
    @property
    def name(self):
        return self.__name
       
    def add_user(self, user):
        if isinstance(user, User):
            self.__user_list.append(user)
        
    def add_atm_machine(self, atm):
        if isinstance(atm, AtmMachine):
            self.__atm_list.append(atm)
            
    def add_seller(self, seller):
        if isinstance(seller, Seller):
            self.__seller_list.append(seller)
            
    def search_user_from_id(self, user_id):
        for user in self.__user_list:
            if user.id == user_id:
                return user
    
    def search_atm_machine(self, atm_id):
        for atm in self.__atm_list:
            if atm.machine_id == atm_id:
                return atm
            
    def search_account_from_card(self, card_id):
        for user in self.__user_list:
            for account in user.account_list:
                if isinstance(account, SavingsAccount) and card_id == account.get_card().id:
                    return account
            
    def search_account_from_account_no(self, account_id):
        for user in self.__user_list:
            for account in user.account_list:
                if account.id == account_id:
                    return account
                
    def search_seller(self, seller_name):
        for seller in self.__seller_list:
            if seller.name == seller_name:
                return seller
                    
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
        if isinstance(account, SavingsAccount) or isinstance(account, FixedDepositAccount):
            self.__account_list.append(account)
            
    def search_account(self, account_id):
        for account in self.__account_list:
            if account.id == account_id:
                return account
        
class Account:
    __max_transfer = 100000
    
    def __init__(self, id, user, balance):
        self.__id = id
        self.__user = user
        self.__balance = balance
        self.__transaction_list = []
    
    @property
    def id(self):
        return self.__id
        
    @property
    def user(self):
        return self.__user
    
    @ property    
    def balance(self):
        return self.__balance
    
    @property
    def transaction_list(self):
        return self.__transaction_list  
    
    def add_transaction(self, transaction):
        if isinstance(transaction, Transaction):
            self.__transaction_list.append(transaction)
            
    def __add__(self, amounts):
        if type(amounts) == int or type(amounts) == float and amounts > 0:
            self.__balance += amounts
            return "Success"
        return "Errror"
    
    def __sub__(self, amounts):
        if type(amounts) == int or type(amounts) == float and self.__balance >= amounts > 0:
            self.__balance -= amounts
            return "Success"
        return "Error"
    
    def __rshift__(self, dnt): # dnt[0] = destination_account & dnt[1] = amounts
        return self - dnt[1] == "Success" and dnt[0] + dnt[1] == "Success"    
       
    def deposit(self, amounts):
        if self + amounts == "Success":
            self.add_transaction(Transaction('D', amounts, self.__balance))
            return "Success"
        return "Error"
    
    def withdraw(self, amounts):
        if self - amounts == "Success":
            self.add_transaction(Transaction('W', amounts, self.__balance))
            return "Success"
        return "Error"
    
    def transfer(self, from_where, amounts, target_account):
        if self.__max_transfer >= amounts and self >> [target_account, amounts]:
            self.add_transaction(Transaction('T', amounts, self.__balance, target_account))
            target_account.add_transaction(Transaction('T', amounts, target_account.balance, target_account))  
            return "Success"
        return "Error"                        
                        
class SavingsAccount(Account):
    __interest_rate = 0.5
    __type = "Savings"

    def __init__(self, id, user, balance):
        Account.__init__(self, id, user, balance)
        self.__card = None
    
    def add_card(self, card):
        if isinstance(card, AtmCard) or isinstance(card, DebitCard):
            self.__card = card
    
    def get_card(self):
        return self.__card
    
    def paid(self, amounts, seller_account):
        if self >> [seller_account, amounts]:
            self.add_transaction(Transaction('P', amounts, self.balance, seller_account))
            seller_account.add_transaction(Transaction('P', amounts, seller_account.balance, seller_account))  
            return "Success"
        return "Error"  

class FixedDepositAccount(Account):
    __interest_rate = 2.5
    __type = "Fixed"
   
class Card:
    def __init__(self, id, account, pin):
        self.__id = id
        self.__account = account
        self.__pin = pin
    
    @property
    def id(self):
        return self.__id
    
    @property
    def account(self):
        return self.__account
    
    @property
    def pin(self):
        return self.__pin

class AtmCard(Card):
    __fee = 150

class DebitCard(Card):
    __fee = 300                     

class Transaction:
    def __init__(self, type, amounts, total, target_account = None):
        self.__type = type
        self.__amounts = amounts
        self.__total = total
        self.__target_account = target_account
    
    def __str__(self):
        return f"{self.__type} - {self.__amounts} -> Total = {self.__total}"
    
    @property
    def type(self):
        return self.__type
    
    @property
    def from_where(self):
        return self.__from_where
    
    @property
    def amounts(self):
        return self.__amounts
    
    @property
    def total(self):
        return self.__total
    
    @property
    def target_account(self):
        return self.__target_account

class Seller:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__edc_list = []
        
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def edc_list(self):
        return self.__edc_list
    
    def add_edc(self, edc):
        if isinstance(edc, EdcMachine):
            self.__edc_list.append(edc)
            
    def search_edc_from_no(self, edc_id):
        for edc in self.__edc_list:
            if edc.id == edc_id:
                return edc
            
    def paid(self, customer_account, amounts, seller_account):
        return customer_account.paid(amounts, seller_account)
        
class EdcMachine:
    def __init__(self, id, seller):
        self.__id = id
        self.__seller = seller
        
    @property
    def id(self):
        return self.__id
    
    @property
    def seller(self):
        return self.__seller
    
    def add_seller(self, seller):
        if isinstance(seller, Seller):
            self.__seller = seller
            
    def paid(self, card, amounts, seller_account):
        if isinstance(card, DebitCard):
            return card.account.paid(amounts, seller_account)
        return "Error"

class AtmMachine:
    __withdraw_limit = 20000
    
    def __init__(self, machine_id, balance = 1000000):
        self.__machine_id = machine_id
        self.__balance = balance
        
    @property
    def machine_id(self):
        return self.__machine_id
    
    def insert_card(self, atm_card, pin):
        if atm_card.pin == pin:
            return "Success"
        return None

    def deposit(self, account, amounts):
        if amounts >= 100 and amounts % 100 == 0 and account.deposit(amounts) == "Success":
            self.__balance += amounts
        return "Error"

    def withdraw(self, account, amounts):
        if self.__withdraw_limit >= amounts >= 100 and amounts % 100 == 0 and account.withdraw(amounts) == "Success":
            self.__balance -= amounts
            return "Success"
        return "Error"

    def transfer(self, account, amounts, target_account):
        return account.transfer(amounts, target_account)                                                
    
##################################################################################

# กำหนด รูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, ประเภทบัญชี, หมายเลขบัญชี, จำนวนเงินในบัญชี, ประเภทบัตร, หมายเลขบัตร ]}
user ={'1-1101-12345-12-0':['Harry Potter','Savings','1234567890',20000,'ATM','12345'],
       '1-1101-12345-13-0':['Hermione Jean Granger','Saving','0987654321',1000,'Debit','12346'],
       '1-1101-12345-13-0':['Hermione Jean Granger','Fix Deposit','0987654322',1000,'',''],
       '9-0000-00000-01-0':['KFC','Savings','0000000321',0,'',''],
       '9-0000-00000-02-0':['Tops','Savings','0000000322',0,'','']}

atm ={'1001':1000000,'1002':200000}

seller_dic = {'210':"KFC", '220':"Tops"}

EDC = {'2101':"KFC", '2201':"Tops"}

# TODO 1 : สร้าง Instance ของธนาคาร และ สร้าง Instance ของ User, Account, บัตร
# TODO   : จากข้อมูลใน user รูปแบบการนำข้อมูลไปใช้สามารถใช้ได้โดยอิสระ
# TODO   : โดย Account แบ่งเป็น 2 subclass คือ Savings และ FixedDeposit
# TODO   : โดย บัตร แบ่งเป็น 2 subclass คือ ATM และ Debit

scb = Bank('SCB')
scb.add_user(User('1-1101-12345-12-0','Harry Potter'))
scb.add_user(User('1-1101-12345-13-0','Hermione Jean Granger'))
scb.add_user(User('9-0000-00000-01-0','KFC'))
scb.add_user(User('9-0000-00000-02-0','Tops'))
harry = scb.search_user_from_id('1-1101-12345-12-0')
harry.add_account(SavingsAccount('1234567890', harry, 20000))
harry_account = harry.search_account('1234567890')
harry_account.add_card(AtmCard('12345', harry_account, '1234'))
hermione = scb.search_user_from_id('1-1101-12345-12-0')
hermione.add_account(SavingsAccount('0987654321',hermione,2000))
hermione_account1 = hermione.search_account('0987654321')
hermione_account1.add_card(DebitCard('12346',hermione_account1,'1234'))
hermione.add_account(FixedDepositAccount('0987654322',hermione,1000))
hermione_account2 = hermione.search_account('0987654322')
kfc = scb.search_user_from_id('9-0000-00000-01-0')
kfc.add_account(SavingsAccount('0000000321', kfc, 0))
tops = scb.search_user_from_id('9-0000-00000-02-0')
tops.add_account(SavingsAccount('0000000322', tops, 0))

# TODO 2 : สร้าง Instance ของเครื่อง ATM

scb.add_atm_machine(AtmMachine('1001',1000000)) 
scb.add_atm_machine(AtmMachine('1002',200000))

# TODO 3 : สร้าง Instance ของ Seller และใส่เครื่อง EDC ใน Seller 

temp1 = Seller('210','KFC')
temp1.add_edc(EdcMachine('2101',temp1)) 
scb.add_seller(temp1) 
temp2 = Seller('220',"Tops")
temp2.add_edc(EdcMachine('2201',temp2))
scb.add_seller(temp2)

# TODO 4 : สร้าง method ฝาก โดยใช้ __add__ ถอน โดยใช้ __sub__ และ โอนโดยใช้ __rshift__
# TODO   : ทดสอบการ ฝาก ถอน โอน โดยใช้ + - >> กับบัญชีแต่ละประเภท

# TODO 5 : สร้าง method insert_card, deposit, withdraw และ transfer ที่ตู้ atm และเรียกผ่าน account อีกที
# TODO   : ทดสอบโอนเงินระหว่างบัญชีแต่ละประเภท

# TODO 6 : สร้าง method paid ที่เครื่อง EDC และเรียกผ่าน account อีกที

# TODO 7 : สร้าง method __iter__ ใน account สำหรับส่งคืน transaction เพื่อให้ใช้กับ for ได้ 

# Test case #1 : ทดสอบ การฝาก จากเครื่อง ATM โดยใช้บัตร ATM ของ harry
# ต้องมีการ insert_card ก่อน ค้นหาเครื่อง atm เครื่องที่ 1 และบัตร atm ของ harry
# และเรียกใช้ function หรือ method deposit จากเครื่อง ATM และเรียกใช้ + จาก account
# ผลที่คาดหวัง :
# Test Case #1
# Harry's ATM No :  12345
# Harry's Account No :  1234567890
# Success
# Harry account before deposit :  20000
# Deposit 1000
# Harry account after deposit :  21000

atm_machine = scb.search_atm_machine('1001')
harry_account = scb.search_account_from_card('12345')
atm_card = harry_account.get_card()
print("Test Case #1")
print("Harry's ATM No : ",atm_card.id)
print("Harry's Account No : ",harry_account.id)
print(atm_machine.insert_card(atm_card, "1234"))
print("Harry account before deposit : ",harry_account.balance)
print("Deposit 1000")
atm_machine.deposit(harry_account,1000)
print("Harry account after deposit : ",harry_account.balance)
print("")

# Test case #2 : ทดสอบ การถอน จากเครื่อง ATM โดยใช้บัตร ATM ของ hermione
# ต้องมีการ insert_card ก่อน ค้นหาเครื่อง atm เครื่องที่ 2 และบัตร atm ของ hermione
# และเรียกใช้ function หรือ method withdraw จากเครื่อง ATM และเรียกใช้ - จาก account
# ผลที่คาดหวัง :
# Test Case #2
# Hermione's ATM No :  12346
# Hermione's Account No :  0987654321
# Success
# Hermione account before withdraw :  2000
# withdraw 1000
# Hermione account after withdraw :  1000

atm_machine = scb.search_atm_machine('1002')
hermione_account = scb.search_account_from_card('12346')
atm_card = hermione_account.get_card()
print("Test Case #2")
print("Hermione's ATM No : ", atm_card.id)
print("Hermione's Account No : ", hermione_account.id)
print(atm_machine.insert_card(atm_card, "1234"))
print("Hermione account before withdraw : ",hermione_account.balance)
print("withdraw 1000")
atm_machine.withdraw(hermione_account,1000)
print("Hermione account after withdraw : ",hermione_account.balance)
print("")


# Test case #3 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ที่เคาน์เตอร์
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง
# Test Case #3
# Harry's Account No :  1234567890
# Hermione's Account No :  0987654321
# Harry account before transfer :  21000
# Hermione account before transfer :  1000
# Harry account after transfer :  11000
# Hermione account after transfer :  11000

harry_account = scb.search_account_from_card('12345')
hermione_account = scb.search_account_from_card('12346')
print("Test Case #3")
print("Harry's Account No : ",harry_account.id)
print("Hermione's Account No : ", hermione_account.id)
print("Harry account before transfer : ",harry_account.balance)
print("Hermione account before transfer : ",hermione_account.balance)
harry_account.transfer("0000", 10000, hermione_account) # take atm_id as parameter
print("Harry account after transfer : ",harry_account.balance)
print("Hermione account after transfer : ",hermione_account.balance)
print("")

# Test case #4 : ทดสอบการชำระเงินจากเครื่องรูดบัตร ให้เรียกใช้ method paid จากเครื่องรูดบัตร
# โดยให้ hermione ชำระเงินไปยัง KFC จำนวน 500 บาท ผ่านบัตรของตัวเอง
# ผลที่คาดหวัง
# Hermione's Debit Card No :  12346
# Hermione's Account No :  0987654321
# Seller :  KFC
# KFC's Account No :  0000000321
# KFC account before paid :  0
# Hermione account before paid :  11000
# KFC account after paid :  500
# Hermione account after paid :  10500

hermione_account = scb.search_account_from_account_no('0987654321')
debit_card = hermione_account.get_card()
kfc_account = scb.search_account_from_account_no('0000000321')
kfc = scb.search_seller('KFC')
edc = kfc.search_edc_from_no('2101')

print("Test Case #4")
print("Hermione's Debit Card No : ", debit_card.id)
print("Hermione's Account No : ",hermione_account.id)
print("Seller : ", kfc.name)
print("KFC's Account No : ", kfc_account.id)
print("KFC account before paid : ",kfc_account.balance)
print("Hermione account before paid : ",hermione_account.balance)
edc.paid(debit_card, 500, kfc_account)
print("KFC account after paid : ",kfc_account.balance)
print("Hermione account after paid : ",hermione_account.balance)
print("")

# Test case #5 : ทดสอบการชำระเงินแบบอิเล็กทรอนิกส์ ให้เรียกใช้ method paid จาก kfc
# โดยให้ Hermione ชำระเงินไปยัง Tops จำนวน 500 บาท
# ผลที่คาดหวัง
# Test Case #5
# Hermione's Account No :  0987654321
# Tops's Account No :  0000000322
# Tops account before paid :  0
# Hermione account before paid :  10500
# Tops account after paid :  500
# Hermione account after paid :  10000

hermione_account = scb.search_account_from_account_no('0987654321')
debit_card = hermione_account.get_card()
tops_account = scb.search_account_from_account_no('0000000322')
tops = scb.search_seller('Tops')
print("Test Case #5")
print("Hermione's Account No : ",hermione_account.id)
print("Tops's Account No : ", tops_account.id)
print("Tops  account before paid : ",tops_account.balance)
print("Hermione account before paid : ",hermione_account.balance)
tops.paid(hermione_account,500,tops_account)
print("Tops account after paid : ",tops_account.balance)
print("Hermione account after paid : ",hermione_account.balance)
print("")

# Test case #6 : แสดง transaction ของ Hermione ทั้งหมด โดยใช้ for loop 
for trans in hermione_account.transaction_list:
    print(trans)