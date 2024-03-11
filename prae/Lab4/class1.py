class BankAccount:
    accounts_created = 0
    def __init__(self, number, client, balance):
        self.number = number
        self.client = client
        self.balance = balance
        BankAccount.accounts_created += 1
        
my_account = BankAccount("5621", "Gino Navone", 33424.4)
print(my_account.client)