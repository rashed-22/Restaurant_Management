from abc import ABC, abstractmethod
class User(ABC):
    def __init__(self, name, phone, email, address) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, phone, email, address, money) -> None:
        self.wallet = money
        self.order = None
        super().__init__(name, phone, email, address)

    @property
    def order(self):
        return self.__order
    
    @order.setter
    def order(self, order):
        self.__order = order

    def place_order(self, order):
        self.order = order
        self.bill_due += order.bill
        print(f'{self.name} placed an order with bill {order.bill}')
    
    def eat_food(self, order):
        print(f'{self.name} item food {order.items}')

    def pay_for_order(self, amount):
        #todo: submit the money to the manager
        pass

    def give_tip(self, tips_amount):
        pass

    def write_review(self, stars):
        pass

class Employee(User):
    def __init__(self, name, phone, email, address, salary, s_date, department) -> None:
        super().__init__(name, phone, email, address)
        self.salary = salary
        self.due = salary
        self.s_date = s_date
        self.department = department
    
    def recieve_salary(self):
        self.due = 0

class Chef(Employee):
    def __init__(self, name, phone, email, address, salary, s_date, department, cook_item = []) -> None:
        super().__init__(name, phone, email, address, salary, s_date, department)
        self.cook_item = cook_item

class Server(Employee):
    def __init__(self, name, phone, email, address, salary, s_date, department) -> None:
        super().__init__(name, phone, email, address, salary, s_date, department)
        self.tips_earning = 0
    def take_order(self, order):
        pass

    def transfer_order(self, order):
        pass

    def serve_food(self, order):
        pass

    def recieve_tips(self, amount):
        self.tips_earning += amount

class Manager(Employee):
    def __init__(self, name, phone, email, address, salary, s_date, department) -> None:
        super().__init__(name, phone, email, address, salary, s_date, department)
