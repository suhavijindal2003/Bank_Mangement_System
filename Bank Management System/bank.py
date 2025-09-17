#bank services
from database import *
import datetime
class Bank:
    
    def __init__(self,username,account_number):
        self.__username=username
        self.__account_number=account_number
       
    #  createing a transaction table for each user
    def create_transaction_table(self):
        db_query(f"CREATE TABLE IF NOT EXISTS {self.__username}_Bank_transaction "
                 f"( timedate VARCHAR(30),"
                 f"account_number INTEGER,"
                 f"remarks VARCHAR(30),"
                 f"amount INTEGER )")
        
    # balanceenquiry
    def balanceEnquiry(self,amount):
        temp =db_query(f"SELECT balance FROM customers WHERE username='{self.__username}';")
        balance=temp[0][0]
    # deposit money
    def deposit(self,amount):
        temp =db_query(f"SELECT balance FROM customers WHERE username='{self.__username}';")
        balance=temp[0][0]
        balance+=amount
        db_query(f"UPDATE customers SET balance={balance} WHERE username='{self.__username}';")
        self.balanceEnquiry()
        db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                 f"'{datetime.datetime.now()}',"
                 f"'{self.__account_number}',"
                 f"'Amount Deposit',"
                 f"'{amount}'"
                 f")")
        print(f"{self.__username} Amount is Sucessfully Depositted into Your Account {self.__account_number}")