import string
import random
class BankAccount:
    def __init__(self, login, password, balance):
        self.login = login
        self._balance = balance
        self.__password = password

    def get_balance(self):
        return self._balance

    def __random_pass(self):
        print(self.__password)
        chart = string.ascii_letters + string.digits
        password = ''.join(random.choice(chart) for i in range(5))
        return password

    def reset_pass(self, old_pass):
        if old_pass == self.__password:
            self.__password = self.__random_pass()
        else:
            return "не верный старый пароль пароль"

ardager = BankAccount("ardager", "Def2638", 1000)
# print(ardager._BankAccount__password)
# print(ardager.reset_pass("Def2638"))
# print(ardager._BankAccount__password)

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    @abstractmethod
    def move(self):
        pass
    def action(self):
        pass

class Dog(Animal):

    def make_sound(self):
        print('Gaf Gaf')

    def move(self):
        pass

gufi = Dog()

# gufi.

class OTPSender(ABC):
    @abstractmethod
    def send_otp(self, phone):
        pass

class KG(OTPSender):
    def send_otp(self, phone):
        data = f'''
            <Phone>{phone}</Phone>
            <Text>Ваш временный код: 1234</Text>
        '''

        return data
class RU(OTPSender):
    def send_otp(self, phone):
        data = {
            "phone": phone,
            "text": "Ваш временный код: 1234"
        }

        return data