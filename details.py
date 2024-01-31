from tabulate import tabulate
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    username="root",
    password="Sudhakar@95",
    database="learning"
)
def insert(name,city,grade):
    pass
def update(name,city,grade):
    pass
def select():
    pass
def delete(id):
    pass

while true:
    print("1.insert")
    print("2.upadte")
    print("3.select")
    print("4.delete")

