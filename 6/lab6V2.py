# Class Code
from datetime import datetime

class User :
  def __init__(self, ident_id, name) :
    self.__ident_id = ident_id
    self.__name = name
    self.__account_list = []

  @property
  def name(self):
    return self.__name

  def add_account(self, account) :
    self.__account_list.append(account)


class Account :
  __max_deposit = 40000
  def __init__(self, user, account_id, balance = 0, card = None) :
    self.__user = user
    self.__account_id = account_id
    self.__balance = balance
    self.__transaction_list = []
    self.__card = card

  @property
  def account_id(self) :
    return self.__account_id
  @property
  def balance(self):
    return self.__balance
  @balance.setter
  def balance(self,balance) :
    self.__balance = balance
  @property
  def card(self):
    return self.__card
  @property
  def transaction_list(self) :
    return self.__transaction_list
  @property
  def max_deposit(self):
    return self.__max_deposit

  def add_card(self, card) :
    self.__card = card
  def add_transaction(self, transaction) :
    self.__transaction_list.append(transaction)

  def check_deposit_per_day(self, date) :
    total = 0 # total withdraw or tranfer in this date
    for transaction in self.transaction_list :
      if transaction.date.year == date.year and transaction.date.month == date.month and transaction.date.day == date.day\
      and (transaction.type == 'W' or (transaction.type == 'T' and transaction.target != self)):
        total += transaction.amount
    return total


  #self, type, amount, date, atm_id, target_account = None
  def cal_balance(self,transaction) :
    if isinstance(transaction, Transaction) :
      transaction.balance_before = self.balance
      if transaction.type == 'D' :
        self.balance += transaction.amount
        
      elif transaction.type == 'W' :
        total = self.check_deposit_per_day( transaction.date) # total withdraw or tranfer in this date
        if total + transaction.amount <= self.max_deposit \
        and self.balance >= transaction.amount :
          self.balance -= transaction.amount
        else :
          return 'error'
          
      elif transaction.type == 'T' :
        if transaction.target_account == self :
          self.balance += transaction.amount
        else :
          total = self.check_deposit_per_day( transaction.date) # total withdraw or tranfer in this date
          if total + transaction.amount <= self.max_deposit and self.balance >= transaction.amount :
            target_transaction = Transaction(transaction.type, transaction.amount, transaction.date, transaction.atm_id, transaction.target_account)
            transaction.target_account.cal_balance(target_transaction)
            
            self.balance -= transaction.amount
          else :
            return 'error'
      else :
        return 'error'
      transaction.balance_after = self.balance
      self.add_transaction(transaction)
      return 'success' 


class AtmCard :
  def __init__(self, card_id, pin_id) :
    self.__card_id = card_id
    self.__pin_id = pin_id

  @property
  def card_id(self) :
    return self.__card_id
  @property
  def pin_id(self) :
    return self.__pin_id


class Transaction :
  def __init__ (self, type, amount, date, atm_id, target_account=None):
    self.__type = type
    self.__amount = amount
    self.__date = date
    self.__atm_id = atm_id
    self.__target_account = target_account
    self.__balance_before = None
    self.__balance_after = None
  @property
  def type(self) :
    return self.__type
  @property
  def amount(self) :
    return self.__amount
  @property
  def date(self) :
    return self.__date
  @property
  def atm_id(self) :
    return self.__atm_id
  @property
  def target_account(self) :
    return self.__target_account
  @property
  def balance_before(self) :
    return self.__balance_before
  @property
  def balance_after(self) :
    return self.__balance_after
  @balance_before.setter
  def balance_before(self, balance_before) :
    self.__balance_before = balance_before
  @balance_after.setter
  def balance_after(self, balance_after) :
    self.__balance_after = balance_after

  def __str__ (self) :
    return f"time : {self.date.strftime('%d-%m-%Y %H:%M:%S')} \n \
    {self.type} - ATM:{self.atm_id} - Amount:{self.amount} - Before:{self.balance_before} - After:{self.balance_after}"


class Atm :
  def __init__(self , atm_id , total_cash = 1000000) :
    self.__total_cash = total_cash
    self.__atm_id = atm_id

  @property
  def atm_id(self):
    return self.__atm_id
  @property
  def total_cash(self):
    return self.__total_cash
  @total_cash.setter
  def total_cash(self,total_cash) :
    self.__total_cash = total_cash

  def insert_card(self, bank, card, entered_pin) :
    if isinstance(bank, Bank) and card.pin_id == entered_pin :
      for account in bank.account_list :
        if account.card == card :
          return account
    return None

  def deposit(self, account, amount) :
    if amount > 0 and isinstance(account, Account):
      if account.cal_balance( Transaction('D', amount, datetime.now(), self.atm_id)) == 'success':
        self.total_cash += amount
        return 'success'
    return 'error'

  def withdraw(self, account, amount) :
    if self.total_cash >= amount > 0 and isinstance(account, Account) :
      if account.cal_balance( Transaction('W', amount, datetime.now(), self.atm_id)) == 'success' :
        self.total_cash -= amount
        return 'success'
    return 'error'

  def transfer(self, account, target_account, amount) :
    if amount > 0 and isinstance(account, Account) and isinstance(target_account, Account) :
      if account.cal_balance( Transaction('T', amount, datetime.now(), self.atm_id, target_account)) == 'success' :
        return 'success'
    return 'error'

class Bank :
  __atm_card_fee = 150
  def __init__(self):
    self.__user_list = []
    self.__account_list = []
    self.__atm_list = []

  @property
  def account_list(self):
    return self.__account_list

  def add_user(self, user) :
    self.__user_list.append(user)
  def add_account(self, account) :
    self.__account_list.append(account)
  def add_atm(self, atm) :
    self.__atm_list.append(atm)



###############################################################################


# กำหนดรูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, หมายเลขบัญชี, หมายเลข ATM, จำนวนเงิน ]}
# *** Dictionary นี้ ใช้สำหรับสร้าง user และ atm instance เท่านั้น
# TODO 1 : จากข้อมูลใน user ให้สร้าง instance จากข้อมูล Dictionary
# TODO :   key:value โดย key เป็นรหัสบัตรประชาชน และ value เป็นข้อมูลของคนนั้น ประกอบด้วย
# TODO :   [ชื่อ, หมายเลขบัญชี, หมายเลขบัตร ATM, จำนวนเงินในบัญชี]
# TODO :   return เป็น instance ของธนาคาร
# TODO :   และสร้าง instance ของเครื่อง ATM จำนวน 2 เครื่อง

bank = Bank()

user1 = User('1-1101-12345-60-0', 'Harry Potter')
user2 = User('1-1101-12345-61-0', 'Hermione Jean Granger')

harry_card = AtmCard('12345', '1234')
hermione_card = AtmCard('12346', '1234')

harry_account = Account(user1, '1234567890', 20000, harry_card)
hermione_account = Account(user2, '0987654321', 1000, hermione_card)

atm1 = Atm('1001', 1000000)
atm2 = Atm('1002', 2000000)

bank.add_user(user1)
bank.add_user(user2)
bank.add_account(harry_account)
bank.add_account(hermione_account)
bank.add_atm(atm1)
bank.add_atm(atm2)


# # Test case #1 : ทดสอบ การ insert บัตร ที่เครื่อง atm เครื่องที่ 1 โดยใช้บัตร atm ของ harry
# # และ Pin ที่รับมา เรียกใช้ function หรือ method จากเครื่อง ATM 
# # ผลที่คาดหวัง : พิมพ์ หมายเลขบัตร ATM อย่างถูกต้อง และ หมายเลข account ของ harry อย่างถูกต้อง
# # Ans : 12345, 1234567890, Success
print("Test case #1 :")
if atm1.insert_card(bank, harry_card, "1234") != None:
    print(atm1.insert_card(bank, harry_card, "1234").card.card_id, atm1.insert_card(bank, harry_card, "1234").account_id, "Success")
else:
    print(atm1.insert_card(bank, harry_card, "1234"))
print('')


# # Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# # ให้เรียกใช้ method ที่ทำการฝากเงิน
# # ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# # Hermione account before test : 1000
# # Hermione account after test : 2000
print("Test case #2 :")
print(f"Hermione account before test : {hermione_account.balance}")
atm2.deposit(hermione_account, 1000)
print(f"Hermione account after test : {hermione_account.balance}")
print('')


# # Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
# # ผลที่คาดหวัง : แสดง Error
print("Test case #3 :")
print(atm2.deposit(hermione_account, -1))
print('')


# # Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# # ให้เรียกใช้ method ที่ทำการถอนเงิน
# # ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# # Hermione account before test : 2000
# # Hermione account after test : 1500
print("Test case #4 :")
print(f"Hermione account before test : {hermione_account.balance}")
atm2.withdraw(hermione_account, 500)
print(f"Hermione account after test : {hermione_account.balance}")
print('')


# # Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
# # ผลที่คาดหวัง : แสดง Error
print("Test case #5 :")
print(atm2.withdraw(hermione_account, 2000))
print('')


# # Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# # ให้เรียกใช้ method ที่ทำการโอนเงิน
# # ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# # Harry account before test : 20000
# # Harry account after test : 10000
# # Hermione account before test : 1500
# # Hermione account after test : 11500
print("Test case #6 :")
print(f"Harry account before test : {harry_account.balance}")
print(f"Hermione account before test : {hermione_account.balance}")
atm2.transfer(harry_account, hermione_account, 10000)
print(f"Harry account after test : {harry_account.balance}")
print(f"Hermione account after test : {hermione_account.balance}")
print('')


# # Test case #7 : แสดง transaction ของ Hermione ทั้งหมด 
# # กำหนดให้เรียกใช้ method __str__() เพื่อใช้คำสั่งพิมพ์ข้อมูลจาก transaction ได้
# # ผลที่คาดหวัง
# # Hermione transaction : D-ATM:1002-1000-2000
# # Hermione transaction : W-ATM:1002-500-1500
# # Hermione transaction : T-ATM:1002-10000-11500
print("Test case #7 :")
for transaction in hermione_account.transaction_list:
    print(transaction)
print('')