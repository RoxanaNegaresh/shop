# importing libraries
from MShop import *

# main program:
while True:
    items = int(input("""
                    Welcome
                    which item do you need?
                    1. panle
                    2. goods
                    3. order    
                    4. shops(only managers)
                    5. loyalty club
                    6. exit
                    """))
    if items == 1:
        try:
            items_1 = int(input("""Which item do you need?
                1. sign up
                2. change your information
                3. your panel
                """))
            if items_1 == 1:
                signup = Customers("user_name", "first name", "last name",
                                   "0011", "09", 10000, 2000, 1000, 3000, "pass")
                signup.sign_up()
            elif items_1 == 2:
                changeinfo = Customers(
                    "user_name", "first name", "last name", "0011", "09", 10000, 2000, 1000, 3000, "pass")
                changeinfo.change_info_user()
            elif items_1 == 3:
                show = Customers("user_name", "first name", "last name",
                                 "0011", "09", 10000, 2000, 1000, 3000, "pass")
                show.show()
            else:
                print("invalid value! (1,2,3)")
        except:
            print("only numbers!")

    if items == 2:
        try:
            items_2 = int(input("""Which item do you need?
                1. Show goods
                2. change good information
                3. add good
                """))
            if items_2 == 1:
                showgood = Goods(100, "good name", "good company",
                                 "2000/01/01", "2002/01/01", 100, 10, 20000)
                showgood.good_show()
            elif items_2 == 2:
                changegood = Goods(
                    100, "good name", "good company", "2000/01/01", "2002/01/01", 100, 10, 20000)
                changegood.change_good_info()
            elif items_2 == 3:
                addgood = Goods(100, "good name", "good company",
                                "2000/01/01", "2002/01/01", 100, 10, 20000)
                addgood.add_good()
            else:
                print("invalid value! (1,2,3)")
        except:
            print("only numbers")
    if items == 3:
        try:
            items_3 = int(input("""Which item do you need?
                    1. Order
                    2. delivery
                    """))
            if items_3 == 1:
                order = Orders(1000, "user name", 10, 100,
                               2, "2024/06/09", "2024/06/10")
                order.order()
            elif items_3 == 2:
                delivery = Orders(1000, "user name", 10, 100,
                                  2, "2024/06/09", "2024/06/10")
                delivery.delivery()
            else:
                print("invalid value! (1,2,3)")
        except:
            print("only numbers")

    if items == 4:
        try:
            items_4 = int(input("""Which item do you need?
                1. new shop
                2. change shop information
                """))
            if items_4 == 1:
                newshop = Shops(10, "name", 2, 900000)
                newshop.new_shop()
            elif items_4 == 2:
                changeshopinfo = Shops(10, "name", 2, 900000)
                changeshopinfo.change_info_shop()
            else:
                print("invalid value! (1,2,3)")
        except:
            print("only numbers")

    if items == 5:
        print("this item is not available right now.")

    if items == 6:
        break
