class BankAccount:

    def __init__(self, name: str, account_number: str, balance = 0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def egyenleg_kiiratas(self):
        print(self.balance)
    def befizetes(self, amount:int):
        self.balance += amount
    def withdrawal(self, amount: int):
        if self.balance >=amount:
            self.balance -= amount
            print("Sikeres pénzfelvétel")
        else:
            print("Sikertelen pénzfelvétel")

account1 = BankAccount("Béla", "00000000", 1000000)
account2 = BankAccount("János", "11111111")
account1.egyenleg_kiiratas()
account2.egyenleg_kiiratas()
account1.withdrawal(50000)
account2.withdrawal(500000)
account1.egyenleg_kiiratas()
account2.egyenleg_kiiratas()
account1.befizetes(200000)
account2.befizetes(200000)
account1.egyenleg_kiiratas()
account2.egyenleg_kiiratas()