from datetime import datetime

class Bank:
    def __init__(self, username, db):
        self.username = username
        self.db = db
        self.account_number = self.get_account_number()

    def get_account_number(self):
        return self.db.query(f"SELECT account_number FROM customers WHERE username='{self.username}'")[0][0]

    def balance_enquiry(self):
        balance = self.db.query(f"SELECT balance FROM customers WHERE username='{self.username}'")[0][0]
        print(f"{self.username}'s Balance is {balance}")

    def deposit(self):
        amount = self.get_amount("deposit")
        if amount:
            balance = self.db.query(f"SELECT balance FROM customers WHERE username='{self.username}'")[0][0] + amount
            self.db.query(f"UPDATE customers SET balance={balance} WHERE username='{self.username}'")
            self.db.commit()
            self.log_transaction('deposit', amount)
            self.balance_enquiry()

    def withdraw(self):
        amount = self.get_amount("withdraw")
        if amount:
            balance = self.db.query(f"SELECT balance FROM customers WHERE username='{self.username}'")[0][0]
            if amount > balance:
                print("Insufficient Balance")
            else:
                balance -= amount
                self.db.query(f"UPDATE customers SET balance={balance} WHERE username='{self.username}'")
                self.db.commit()
                self.log_transaction('withdraw', amount)
                self.balance_enquiry()

    def fund_transfer(self):
        receiver = int(input("Enter Receiver Account Number: "))
        amount = self.get_amount("transfer")
        if amount:
            sender_balance = self.db.query(f"SELECT balance FROM customers WHERE username='{self.username}'")[0][0]
            if amount > sender_balance:
                print("Insufficient Balance")
            else:
                receiver_balance = self.db.query(f"SELECT balance FROM customers WHERE account_number={receiver}")[0][0]
                self.db.query(f"UPDATE customers SET balance={sender_balance - amount} WHERE username='{self.username}'")
                self.db.query(f"UPDATE customers SET balance={receiver_balance + amount} WHERE account_number={receiver}")
                self.db.commit()
                self.log_transaction('transfer', amount, receiver)
                self.balance_enquiry()
                print(f"Amount Transfered Successfully '{receiver}'")

    def get_amount(self, action):
        try:
            amount = int(input(f"Enter Amount to {action}: "))
            if amount <= 0:
                print("Amount should be positive")
                return None
            return amount
        except ValueError:
            print("Invalid Amount, Try Again")
            return None

    def log_transaction(self, action, amount, receiver=None):
        if action == 'deposit':
            remarks = 'Amount Deposited'
        elif action == 'withdraw':
            remarks = 'Amount Withdrawn'
        elif action == 'transfer':
            remarks = f'Fund Transfer to {receiver}'
        self.db.query(f"INSERT INTO {self.username}_transaction (timedate, account_number, remarks, amount) VALUES "
                      f"('{datetime.now()}', {self.account_number}, '{remarks}', {amount})")
