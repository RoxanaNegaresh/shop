import pymysql

class Customers:
    def __init__(self, user_name: str, firstname: str, lastname: str, user_id: int, user_phonenumber: str, totalprice: float, discount: float, debt: float, password: str) -> None:
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
            self.user_name=input("Enter your user name:")
            self.firstname=input("Enter your first name:")
            self.lastname=input("Enter your last name:")
            self.user_id=input("Enter your user ID:")
            self.user_phonenumber=input("Enter your phone number:")
            self.password=input("Enter your password:")
            
            
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
        
class Orders:
    def __init__(self, order_code: int, user_name: str, shop_code: int, good_code: int, order_date: str, delivery_date:str) -> None:
        self.order_code=order_code
        self.user_name=user_name
        self.shop_code=shop_code
        self.good_code=good_code
        self.order_date=order_date
        self.delivery_date=delivery_date
        
class Shops:
    def __init__(self, shop_code: int, shop_name: str, undelivered: int, price: float) -> None:
        self.shop_code=shop_code
        self.shop_name=shop_name
        
        
    def new_shop(self):
        try:
            self.shop_code=input("Enter shop code:")
            self.shop_name=input("Enter shop name:")
            
            
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