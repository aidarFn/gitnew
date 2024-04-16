class Bank:
    def __init__(self, name, age, money, key):
        self._name = name
        self._age = age
        self.__money = money
        self.__key = key

    def set_name(self, name):
        pass

    def get_name(self):
        pass

class Bank2(Bank):
    def set_name(self, name):
        self._name = name
    def get_name(self):
        return self._name
    def set_age(self, age):
        self._age = age
    def get_age(self):
        return self._age
    def set_money(self, money):
        self.__money = money
    def get_money(self):
        return self.__money
    def set_key(self, key):
        self.__key = key
    def get_key(self):
        return self.__key

class Bank3(Bank2):

    name = property(get_name, set_name)
    age = property(get_age, set_age)
    money = property(get_money, set_money)
    key = property(get_key, set_key)

