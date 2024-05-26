import pymysql

class Customers:
    def __init__(self, user_name: str, firstname: str, lastname: str, user_id: str, user_phonenumber: str, totalprice: float, discount: float, debt: float, password: str) -> None:
        self.user_name=user_name
        self.firstname=firstname
        self.lastname=lastname
        self.user_id=user_id
        self.user_phonenumber=user_phonenumber
        self.totalprice=totalprice
        self.discount=discount
        self.debt=debt
        self.password=password
        
    
        
    def sign_up(self):
        try:
            self.user_name=input("Enter your user name: ")
            self.firstname=input("Enter your first name: ")
            self.lastname=input("Enter your last name: ")
            self.user_id=input("Enter your user ID: ")
            self.user_phonenumber=input("Enter your phone number: ")
            self.password=input("Enter your password: ")
            
            
            connect=pymysql.connect(host='localhost', port=3306, user='root', password='', db='shop')
            cursor=connect.cursor()
            cursor.execute(f"""INSERT INTO customers (user_name, firstname, lastname, user_id, user_phonenumber, password)
                    VALUES 
                    ('{self.user_name}', '{self.firstname}', '{self.lastname}', '{self.user_id}', '{self.user_phonenumber}', '{self.password}');""")
            print("welcome!")
        except:
            print("duplicate User name! try again.")
        
        else:
            connect.commit()
            cursor.close()
            connect.close()
         
        
        
    
    
    def change_info_user(self): 
        items = int(input("""Which Item do you need? 
            1. change your user name 
            2. change your first name 
            3. change your last name 
            4. change your user ID 
            5. change your phonenumber 
            6. change your password
""")) 
     
        username = input("enter your user name: ") 
        password = input("enter your password: ") 
        
        connect = pymysql.connect(host='localhost', port=3306, user='root', password='', db='shop') 
        cursor = connect.cursor() 
        cursor.execute(f"SELECT * FROM customers WHERE user_name='{username}' AND password='{password}'") 
        result = list(cursor.fetchall()) 
        connect.commit() 
     
        if result: 
            if items == 1: 
                new_username = input("Enter your new user name: ") 
                self.user_name = new_username 
                cursor.execute(f"UPDATE customers SET user_name = '{self.user_name}' WHERE user_name = '{username}' AND password='{password}'") 
                connect.commit() 
                print("user name changed successfully!") 
            elif items == 2: 
                new_firstname = input("Enter your new first name: ") 
                self.firstname = new_firstname 
                cursor.execute(f"UPDATE customers SET firstname = '{self.firstname}' WHERE user_name = '{username}' AND password='{password}'") 
                connect.commit() 
                print("first name changed successfully!") 
            elif items == 3: 
                new_lastname = input("Enter your new last name: ") 
                self.lastname = new_lastname 
                cursor.execute(f"UPDATE customers SET lastname = '{self.lastname}' WHERE user_name = '{username}' AND password='{password}'") 
                connect.commit() 
                print("last name changed successfully!") 
            elif items == 4: 
                new_user_id = input("Enter your new user ID: ") 
                self.user_id = new_user_id 
                cursor.execute(f"UPDATE customers SET user_id = '{self.user_id}' WHERE user_name = '{username}' AND password='{password}'") 
                connect.commit() 
                print("user ID changed successfully!") 
            elif items == 5: 
                new_phonenumber = input("Enter your new phone number: ") 
                self.user_phonenumber = new_phonenumber 
                cursor.execute(f"UPDATE customers SET phonenumber = '{self.user_phonenumber}' WHERE user_name = '{username}' AND password='{password}'") 
                connect.commit() 
                print("user phone number changed successfully!") 
            elif items == 6: 
                old_password = input("enter your old password: ") 
                if old_password == self.password: 
                    new_password = input("Enter your new password: ") 
                    self.password = new_password 
                    cursor.execute(f"UPDATE customers SET password = '{self.password}' WHERE user_name = '{username}' AND password='{password}'") 
                    connect.commit() 
                    print("password changed successfully!") 
                else: 
                    print("Wrong password!") 
            else: 
                print("invalid value! (1,2,3,4,5,6)") 
            
            cursor.close() 
            connect.close() 
        else: 
            print("Wrong password or username! try again.")
                
                
                

            
        
        
        
        
        
            
        
        
        
        
        
class Goods:
    def __init__(self, good_code: int, good_name:str, good_company: str,  good_production_date: str, good_expiration_date: str, good_Purchases: int,  good_inventory: int, good_price: float) -> None:
        self.good_code=good_code
        self.good_name=good_name
        self.good_company=good_company
        self.good_production_date=good_production_date
        self.good_expiration_date=good_expiration_date
        self.good_Purchases=good_Purchases
        self.good_inventory=good_inventory
        self.good_price=good_price
        
        
        
    def add_good(self):
        
        username = input("enter your user name: ") 
        password = input("enter your password: ") 
        
        connect = pymysql.connect(host='localhost', port=3306, user='root', password='', db='shop') 
        cursor = connect.cursor() 
        cursor.execute(f"SELECT * FROM customers WHERE user_name='{username}' AND password='{password}' AND status=1") 
        result = list(cursor.fetchall()) 
        connect.commit()
        
    
        if result:
            
            try:
                self.good_code=int(input("Enter the good code: "))
                self.good_name=input("Enter the good name: ")
                self.good_company=input("Enter the good company: ")
                self.good_production_date=input("Enter the good production date: ")
                self.good_expiration_date=input("Enter the good expiration date: ")
                self.good_Purchases=int(input("Enter the good Purchases: "))
                self.good_inventory=int(input("Enter the good inventory: "))
                self.good_price=float(input("Enter the good price: "))
                
                
                
                cursor=connect.cursor()
                cursor.execute(f"""INSERT INTO goods (good_code, good_name, good_company, good_production_date, good_expiration_date, good_Purchases, good_inventory, good_price)
                        VALUES 
                        ('{self.good_code}', '{self.good_name}', '{self.good_company}', '{self.good_production_date}', '{self.good_expiration_date}', '{self.good_Purchases}', '{self.good_inventory}', '{self.good_price}');""")
                print("Good added!")
            except:
                print("duplicate Good code! try again.")
            
            else:
                connect.commit()
                    
        else:
            print("Access Denied!")
            
        cursor.close()
        connect.close()
        
         
        
    def change_good_info(self): 
        
        username = input("enter your user name: ") 
        password = input("enter your password: ")
        
        connect = pymysql.connect(host='localhost', port=3306, user='root', password='', db='shop')
        cursor = connect.cursor() 
        
        cursor.execute(f"SELECT * FROM customers WHERE user_name='{username}' AND password='{password}' AND status=1") 
        result_user = list(cursor.fetchall()) 
        connect.commit()
        if result_user:
            items = int(input("""Which Item do you need? 
                1. change the good code 
                2. change the good name
                3. change the good company 
                4. change the good production date
                5. change the good expiration date 
                6. change the good Purchases
                7. change the good inventory
                8. change the good price
    """)) 
        
            goodcode = input("enter the good code: ")
            
            
            
            
            
            cursor.execute(f"SELECT * FROM goods WHERE good_code='{goodcode}'") 
            result = list(cursor.fetchall()) 
            connect.commit() 
            
            
        
            if result: 
                if items == 1: 
                    new_goodcode = input("Enter new good code: ") 
                    self.good_code = new_goodcode 
                    cursor.execute(f"UPDATE goods SET good_code = '{self.good_code}' WHERE good_code = '{goodcode}'") 
                    connect.commit() 
                    print("good code changed successfully!") 
                elif items == 2: 
                    new_goodname = input("Enter new good name: ") 
                    self.good_name= new_goodname 
                    cursor.execute(f"UPDATE goods SET good_name = '{self.good_name}' WHERE good_code = '{goodcode}'") 
                    connect.commit() 
                    print("good name changed successfully!") 
                elif items == 3: 
                    new_goodcompany = input("Enter new good company: ") 
                    self.good_company= new_goodcompany 
                    cursor.execute(f"UPDATE goods SET good_company = '{self.good_company}' WHERE good_code = '{goodcode}'") 
                    connect.commit() 
                    print("good company changed successfully!") 
                elif items == 4: 
                    new_good_production_date = input("Enter good production date: ") 
                    self.good_production_date= new_good_production_date 
                    cursor.execute(f"UPDATE goods SET good_production_date = '{self.good_production_date}' WHERE good_code = '{goodcode}'") 
                    connect.commit() 
                    print("good production date changed successfully!") 
                elif items == 5: 
                    new_good_expiration_date = input("Enter new good expiration date: ") 
                    self.good_expiration_date= new_good_expiration_date 
                    cursor.execute(f"UPDATE goods SET good_expiration_date = '{self.good_expiration_date}' WHERE good_code = '{goodcode}'") 
                    connect.commit() 
                    print("good expiration date changed successfully!") 
                elif items == 6: 
                    new_goodPurchases = input("Enter new good Purchases: ") 
                    self.good_Purchases= new_goodPurchases 
                    cursor.execute(f"UPDATE goods SET good_Purchases = '{self.good_Purchases}' WHERE good_code = '{goodcode}'") 
                    connect.commit() 
                    print("good Purchases changed successfully!") 
                elif items == 7: 
                    new_goodinventory = input("Enter new good inventory: ") 
                    self.good_inventory= new_goodinventory 
                    cursor.execute(f"UPDATE goods SET good_inventory = '{self.good_inventory}' WHERE good_code = '{goodcode}'") 
                    connect.commit() 
                    print("good inventory changed successfully!")
                elif items == 8: 
                    new_goodprice= input("Enter new good price: ") 
                    self.good_price= new_goodprice 
                    cursor.execute(f"UPDATE goods SET good_price = '{self.good_price}' WHERE good_code = '{goodcode}'") 
                    connect.commit() 
                    print("good price changed successfully!")
                else: 
                    print("invalid value! (1,2,3,4,5,6,7,8)") 
                
                cursor.close() 
                connect.close() 
            else: 
                print("Wrong good code! try again.")
        else:
            print("Access Denied!")
            
        
        
        
class Orders:
    def __init__(self, order_code: int, user_name: str, shop_code: int, good_code: int, good_number: int, order_date: str, delivery_date:str) -> None:
        self.order_code=order_code
        self.user_name=user_name
        self.shop_code=shop_code
        self.good_code=good_code
        self.good_number=good_number
        self.order_date=order_date
        self.delivery_date=delivery_date
        
class Shops:
    def __init__(self, shop_code: int, shop_name: str, undelivered: int, price: float) -> None:
        self.shop_code=shop_code
        self.shop_name=shop_name
        
        
    def new_shop(self):
        try:
            self.shop_code=int(input("Enter shop code: "))
            self.shop_name=input("Enter shop name: ")
            
            
            connect=pymysql.connect(host='localhost', port=3306, user='root', password='', db='shop')
            cursor=connect.cursor()
            cursor.execute(f"""INSERT INTO shops (shop_code, shop_name)
                    VALUES 
                    ('{self.shop_code}', '{self.shop_name}');""")
            print("Shop Added!")
        except:
            print("duplicate Shop code! try again.")
        
        else:
            connect.commit()
            cursor.close()
            connect.close()
            
    def change_info_shop(self): 
        items = int(input("""Which Item do you need? 
            1. change your shop code 
            2. change your shop name 
            
""")) 
     
        shopcode = input("enter shop code: ") 
         
        
        connect = pymysql.connect(host='localhost', port=3306, user='root', password='', db='shop') 
        cursor = connect.cursor() 
        cursor.execute(f"SELECT * FROM shops WHERE shop_code='{shopcode}'") 
        result = list(cursor.fetchall()) 
        connect.commit() 
     
        if result: 
            if items == 1: 
                new_shopcode = input("Enter your new shop code: ") 
                self.shop_code = new_shopcode
                cursor.execute(f"UPDATE shops SET shop_code = '{self.shop_code}' WHERE shop_code = '{shopcode}'") 
                connect.commit() 
                print("shop code changed successfully!") 
            elif items == 2: 
                new_shopname = input("Enter your new shop name: ") 
                self.shop_name = new_shopname 
                cursor.execute(f"UPDATE shops SET shop_name = '{self.shop_name}' WHERE shop_code = '{shopcode}'") 
                connect.commit() 
                print("shop name changed successfully!")  
            else: 
                print("invalid value! (1,2)") 
            
            cursor.close() 
            connect.close() 
        else: 
            print("Wrong Shop code! try again.")