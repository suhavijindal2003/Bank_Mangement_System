# database management Banking
import mysql.connector as sql

mydb = sql.connect(
    host="localhost",
    user="root",
    password="root",   # <-- change if your MySQL password is different
    database="bank"    # <-- make sure 'bank' database exists
)

# print("✅ Connected to MySQL Database!")

cursor = mydb.cursor()
def db_query(query):
    cursor.execute(query)
    result = cursor.fetchall()
    return result


def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            username VARCHAR(20) NOT NULL,
                password VARCHAR(20) NOT NULL,
                name varchar(20) NOT NULL,
                age INTEGER NOT NULL,
                city VARCHAR(20) NOT NULL,
                balance INTEGER NOT NULL,
                account_number INTEGER NOT NULL,
                status BOOLEAN NOT NULL
        )
    """)
    # print("✅ Table 'customers' created successfully!")
    mydb.commit()


if __name__ == "__main__":
    create_table()
