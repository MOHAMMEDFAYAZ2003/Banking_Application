from register import Register
from bank import Bank
from database import Database

class BankingSystem:
    def __init__(self):
        self.db = Database()
        self.register = Register(self.db)
        self.bank = None

    def run(self):
        print("Welcome to SBI Banking Project")
        while True:
            try:
                choice = int(input("1. SignUp\n2. SignIn\n"))
                if choice == 1:
                    self.register.signup()
                elif choice == 2:
                    user = self.register.signin()
                    if user:
                        self.bank = Bank(user, self.db)
                        self.main_menu()
                    else:
                        print("Sign in failed")
                else:
                    print("Please Enter Valid Input From Options")
            except ValueError:
                print("Invalid Input Try Again with Numbers")

    def main_menu(self):
        while True:
            print(f"Welcome {self.bank.username.capitalize()}! Choose Your Banking Service")
            try:
                choice = int(input("1. Balance Enquiry\n2. Cash Deposit\n3. Cash Withdrawal\n4. Fund Transfer\n5. Exit\n"))
                if choice == 1:
                    self.bank.balance_enquiry()
                elif choice == 2:
                    self.bank.deposit()
                elif choice == 3:
                    self.bank.withdraw()
                elif choice == 4:
                    self.bank.fund_transfer()
                elif choice == 5:
                    break
                else:
                    print("Please Enter Valid Input From Options")
            except ValueError:
                print("Invalid Input Try Again with Numbers")

if __name__ == "__main__":
    system = BankingSystem()
    system.run()
