from bank import Bank2
from bank import Bank3
class Bank3(Bank2):

    name = property(Bank2.get_name, Bank2.set_name)
    age = property(Bank2.get_age, Bank2.set_age)
    money = property(Bank2.get_money, Bank2.set_money)
    key = property(Bank2.get_key, Bank2.set_key)
