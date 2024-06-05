class Customer:
    def __init__(self, username, password, name, age, city, account_number):
        self.username = username
        self.password = password
        self.name = name
        self.age = age
        self.city = city
        self.account_number = account_number

    def create_user(self, db):
        db.query(f"INSERT INTO customers (username, password, name, age, city, balance, account_number, status) VALUES "
                 f"('{self.username}', '{self.password}', '{self.name}', {self.age}, '{self.city}', 0, {self.account_number}, 1)")
        db.query(f"CREATE TABLE IF NOT EXISTS {self.username}_transaction "
                 f"(timedate VARCHAR(30), account_number INTEGER, remarks VARCHAR(30), amount INTEGER)")
        db.commit()
