###1
class Cookie:
    def __init__(self):
        self.c = {}

    def set(self, name, value):
        self.c[name] = value

    def get(self, name):
        return self.c.get(name)

    def deli(self, name):
        if name in self.c:
            del self.c[name]


cookie = Cookie()
cookie.set("cookie", "123")
print(cookie.get("cookie"))
cookie.deli("cookie")

###2
class House:
    def __init__(self, address, vladelec, price, max_gost, phone, status=""):
        if price < 0:
            print("Стоимость не может быть отрицательной")
        self.address = address
        self.vladelec = vladelec
        self.price = price
        self.max_gost = max_gost
        self.phone = phone
        self.status = status


class Vladelec:
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address
        self.houses = []

    def add_house(self, house):
        self.houses.append(house)


vlad = Vladelec("Иван Иванов", "8900900900", "ул. Пушкина, 10")
house = House("ул. Лермонтова, 5", vlad, 50000, 3, "88005353535")
vlad.add_house(house)

###3
class Schot:
    def __init__(self, valut, balance=0.0):
        self.valut = valut
        self.balance = balance

class User:
    def __init__(self, name, transfer_limit):
        self.name = name
        self.transfer_limit = transfer_limit
        self.schots = []
        self.transfer_history = []

    def add_account(self, valut):
        self.schots.append(Schot(valut))

    def transfer(self, from_schot_index, to_user, to_schot_index, summ, date):
        if summ > self.transfer_limit:
            print("Превышен лимит перевода")
            return

        if from_schot_index >= len(self.schots) or to_schot_index >= len(to_user.schots):
            print("Ошибка: указан неверный индекс счета")
            return

        from_schot = self.schots[from_schot_index]
        to_schot = to_user.schots[to_schot_index]

        if from_schot.valut != to_schot.valut:
            print("Не совпадают валюты счетов")
            return

        if from_schot.balance < summ:
            print("Недостаточно средств")
            return

        from_schot.balance -= summ
        to_schot.balance += summ

        self.transfer_history.append({
            "date": date,
            "summ": summ,
            "currency": from_schot.valut,
            "from": self.name,
            "to": to_user.name
        })

    def show_balance(self):
        print(f"Балансы пользователя {self.name}:")
        for i, schot in enumerate(self.schots, 1):
            print("Счет", i, ":", schot.balance, schot.valut)

Petya = User('Petya', 500)
Vasya = User('Vasya', 500)
Petya.add_account('rub')
Vasya.add_account('rub')
Petya.schots[0].balance = 1000
Vasya.schots[0].balance = 500
Petya.show_balance()
Vasya.show_balance()
Petya.transfer(0, Vasya, 0, 250, '30.04.2025')
Petya.show_balance()
Vasya.show_balance()

###4
class BlogPost:
    def __init__(self, user_name, text, number_of_likes=0):
        self.user_name = user_name
        self.text = text
        self.number_of_likes = number_of_likes

post1 = BlogPost("user1", "Первый пост")
post2 = BlogPost("user2", "Второй пост")
post1.number_of_likes = 10
print(post1.number_of_likes)
print(post2.number_of_likes)

###5
class BankAccount:
    def __init__(self, client_id, first_name, last_name, balance=0.0):
        self._client_id = client_id
        self._client_first_name = first_name
        self._client_last_name = last_name
        self.balance = balance

    def add(self, summ):
        if summ > 0:
            self.balance += summ
            print(account.balance)

    def withdraw(self, summ):
        if 0 < summ <= self.balance:
            self.balance -= summ
            print(account.balance)


account = BankAccount("123", "Иван", "Иванов")
account.add(1000)
account.withdraw(500)

###6
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.known_people = []

    def know(self, person):
        if person not in self.known_people:
            self.known_people.append(person)

    def is_known(self, person):
        return person in self.known_people

vova = Person("Вова", 30)
valera = Person("Валера", 25)
vova.know(valera)
print(vova.is_known(valera))

###7
class Animal:
    def __init__(self, name, is_hish=False, is_yad=False):
        self.name = name
        self.is_hish = is_hish
        self.is_yad = is_yad

class Human:
    def is_dangerous(animal):
        return animal.is_hish or animal.is_yad

lion = Animal("Лев", is_hish=True)
spider = Animal("Паук", is_yad=True)
dog = Animal("Собака")

print(Human.is_dangerous(lion))
print(Human.is_dangerous(spider))
print(Human.is_dangerous(dog))