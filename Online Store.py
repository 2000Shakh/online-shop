import datetime
import datetime

from bson import ObjectId
from pymongo import MongoClient

class Store:
    def __init__(self):
        from pymongo import MongoClient
        cluster = MongoClient( "mongodb+srv://Shakhzod:19912000@cluster0.rj0wh.mongodb.net/Magazine?retryWrites=true&w=majority")
        db = cluster["Cluster"]
        self.admen = db["Admen"]
        self.chek = db["Chek"]
        self.clients = db["Clients"]
        self.products= db["Products"]

    def insert(self):
        users = [
            {"name": "Shakhzod",
             "surname": "Eshtemirov",
             "login": "Shakhzod2000",
             "password": "4555",
             "balance": 0

                }
        ]
        self.admen.insert_many(users)


    def registration(self):
        name = input("Ввидите ваш имя:")
        surname = input("Ввидите вашу фамилию:")
        login = input("Ввидите ваш логин:")
        password = int(input("Ввидите ваш пароль:"))
        balance = int(input("Ввидите ваш баланс"))

        my_users = [
            {"name": name,
             "surname": surname,
             "login": login,
             "password": password,
             "balance": balance
             }
        ]
        self.clients.insert_many(my_users)



if __name__ == "__main__":
    db =Store()
    db.registration()
