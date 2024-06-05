import mysql.connector as sql

class Database:
    def __init__(self):
        self.mydb = sql.connect(
            host="localhost",
            user="root",
            password="12345",
            database="Bank"
        )
        self.cursor = self.mydb.cursor()
        self.create_customer_table()

    def create_customer_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                username VARCHAR(20) NOT NULL,
                password VARCHAR(20) NOT NULL,
                name VARCHAR(20) NOT NULL,
                age INTEGER NOT NULL,
                city VARCHAR(20) NOT NULL,
                balance INTEGER NOT NULL,
                account_number INTEGER NOT NULL,
                status BOOLEAN NOT NULL
            )
        ''')
        self.mydb.commit()

    def query(self, query_str):
        self.cursor.execute(query_str)
        return self.cursor.fetchall()

    def commit(self):
        self.mydb.commit()
