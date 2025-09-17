#User registration Signin SignUp
import random
# from database import *
from bank import Bank
from customer import *
def SignUp():
    username = input("Enter your username: ")
    temp=db_query(f"SELECT username FROM customers WHERE username='{username}';")
    # print(temp)
    if temp:
        print("Username already exists. Please choose a different username.")
        SignUp()
        
    else:
        print("Username available.")
        password = input("Enter your password: ")
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        city = input("Enter your city: ")
        while True:
            account_number = int(random.randint(10000000, 99999999))
            temp=db_query(f"SELECT account_number FROM customers WHERE account_number='{account_number}';")
            if temp:
                continue
            else:
                print(account_number)
                break
    cusobj=Customer(username,password,name,age,city,account_number)
    cusobj.createuser()
    print("User registered successfully!")
    bankobj=Bank(username,account_number)
    bankobj.create_transaction_table()
    print("Account created successfully!")
    
def SignIn():
    username = input("Enter Username: ")
    temp = db_query(f"SELECT username FROM customers where username = '{username}';")
    if temp:
        while True:
            password = input(f"Welcome {username.capitalize()} Enter Password: ")
            temp = db_query(f"SELECT password FROM customers where username = '{username}';")
            # print(temp[0][0])
            if temp[0][0] == password:
                print("Sign IN Succesfully")
                return username
            else:
                print("Wrong Password Try Again")
                continue
    else:
        print("Enter Correct Username")
        SignIn()