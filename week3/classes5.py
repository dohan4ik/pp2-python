class Bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def top_up(self, money):
        self.balance += money
        print(f"Ваш кошелек после пополнения {self.balance}")
    def withdraw(self, take_off):
        self.take_off = take_off
        limit = 300000
        if take_off > limit: 
            print("Вы не можете снять такую сумму")
        else:
            print("Done")
user = Bank(input("Логин: "), int(input("ваш баланс: ")))
user.top_up(int(input("Введите сумму пополнения: ")))
user.withdraw(int(input("Какую сумму надо снять: ")))