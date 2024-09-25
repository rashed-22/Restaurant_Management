from menu import Pizza, Burger, Menu, Drinks
from restaurant import Restaurant
from user import Customer, Chef, Server, Manager
from order import Order
def main():
    menu = Menu()
    pizza_1 = Pizza('meat', 1500, 'large', ['meat', 'olive', 'capsicum'])
    menu.add_menu_item('pizza', pizza_1)
    pizza_2 = Pizza('alur vorta', 200, 'medium', ['tomato', 'olive', 'shutki'])
    menu.add_menu_item('pizza', pizza_2)
    pizza_3 = Pizza('vegetables', 500, 'large', ['tomato', 'olive', 'capsicum'])
    menu.add_menu_item('pizza', pizza_3)

    #add burger to the menu
    burger_1 = Burger('naga burger', 1500, 'chicken', ['bread', 'chili', 'shos'])
    menu.add_menu_item('burger', burger_1)
    burger_2 = Burger('burger king', 400, 'beef', ['bread', 'chili', 'shos'])
    menu.add_menu_item('burger', burger_2)

    #add drinks to the menu
    coke = Drinks('Coke', 60, True)
    menu.add_menu_item('drinks', coke)
    coffee = Drinks('cold coffe', 600, False)
    menu.add_menu_item('drinks', coffee)

    #show menu
    menu.show_menu()

    resturant = Restaurant('Sahi baba hotel', 2000, menu)

    #add employee
    manager = Manager('shada chan', 849430, 'kalachan@khan.com', 'kalapur', 1500, '01 janu 2020', 'manager')
    resturant.add_employee('manager', manager)
    chef = Chef('Rustom babu', 439489, 'rusto@chef.com', 'rustikha', 1000, '02 March 2021', 'chef', ['kacchi', 'morog polao', 'tehari'])
    resturant.add_employee('chef', chef)
    server = Server('chotu pola', 585, 'kdfo@.khan.com', 'cholarpur', 233, '33 jun 2022', 'waiter')
    resturant.add_employee('server', server)

    #show employees
    resturant.show_employees()

    #customer 1 placing an order
    customer_1 = Customer('janina', 549, 'king@khan.com', 'dholaipar', 20000)
    order_1 = Order(customer_1, [pizza_3, coffee])
    customer_1.pay_for_order(order_1)
    resturant.add_order(order_1)

    #customer 1 one paying for order_1
    resturant.recieve_payment(order_1, 5000, customer_1)
    print('revenue and balance after first customer: ',resturant.revenue, resturant.balance)



    #customer 2 placing an order
    customer_2 = Customer('hablu', 665, 'king@khan.com', 'dholaipar', 20000)
    order_2 = Order(customer_2, [pizza_1, coffee, burger_2, burger_1])
    customer_2.pay_for_order(order_2)
    resturant.add_order(order_2)

    #customer 2 one paying for order_1
    resturant.recieve_payment(order_2, 5000, customer_2)
    print('revenue and balance after second customer: ', resturant.revenue, resturant.balance)

    #pay rent
    resturant.pay_expense(resturant.rent, 'Rent')
    print('after rent', resturant.revenue, resturant.balance, resturant.expense)

    resturant.pay_salary(chef)
    print('after salary', resturant.revenue, resturant.balance, resturant.expense)

#call the main function
if __name__ == '__main__':
    main()