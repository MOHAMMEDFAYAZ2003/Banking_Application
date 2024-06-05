from customer import Customer
import random

class Register:
    def __init__(self, db):
        self.db = db

    def signup(self):
        username = input("Create Username: ")
        if self.db.query(f"SELECT username FROM customers WHERE username='{username}'"):
            print("Username already exists")
            self.signup()
        else:
            print("Username is available, please proceed")
            password = input("Enter your Password: ")
            name = input("Enter your Name: ")
            age = input("Enter your Age: ")
            city = input("Enter Your City: ")
            account_number = self.generate_account_number()
            customer = Customer(username, password, name, age, city, account_number)
            customer.create_user(self.db)
            print("Signup successful. Your account number is:", account_number)

    def signin(self):
        username = input("Enter Username: ")
        if self.db.query(f"SELECT username FROM customers WHERE username='{username}'"):
            while True:
                password = input(f"Welcome {username.capitalize()}, Enter Password: ")
                if self.db.query(f"SELECT password FROM customers WHERE username='{username}'")[0][0] == password:
                    print("Sign in Successfully")
                    return username
                else:
                    print("Wrong Password, Try Again")
        else:
            print("Username not found")
            return None

    def generate_account_number(self):
        while True:
            account_number = random.randint(10000000, 99999999)
            if not self.db.query(f"SELECT account_number FROM customers WHERE account_number='{account_number}'"):
                return account_number
