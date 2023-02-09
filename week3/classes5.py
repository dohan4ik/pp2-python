"""
 Создайте класс банковского счета, который имеет атрибуты owner, balance и два метода deposit и withdraw. Снятие средств не должно превышать доступный баланс.
Создайте свой класс, сделайте несколько операций пополнения и снятия средств и проверьте, что счет не может быть переполнен.

class Account:
    pass
"""
class Bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def top_up(self, money):
        self.balance += money
        print(f"Ваш кошелек после пополнения {self.balance}")
    def withdraw(self, take_off):
        self.take_off = take_off
        limit = self.balance
        if take_off > limit: 
            print("Вы не можете снять такую сумму")
        else:
            print("Выаолнено")
user = Bank(input("Логин: "), int(input("ваш баланс: ")))
user.top_up(int(input("Введите сумму пополнения: ")))
user.withdraw(int(input("Какую сумму надо снять: ")))