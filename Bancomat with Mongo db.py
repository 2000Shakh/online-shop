from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://Shakhzod:19912000@cluster0.rj0wh.mongodb.net/Bank?retryWrites=true')
db = cluster["Bank"]
collection1 = db["Users"]
collection2 = db["Users2"]


class Bancomat:

    # def __init__(self):
    #     self.bank_card1 = None

    def __init__(self) -> object:
        """

        :rtype: object
        """
        self.bank_kard = None

    def registration(self) -> object:
        name = input("name:")
        surname = input("surname:")
        bank_card = int(input("bank_card:"))
        pin_cod = int(input("pin_cod:"))
        balance = int(input("balance:"))

        a = [
            {
                "name": name,
                "surname": surname,
                "bank_card": bank_card,
                "pin_cod": pin_cod,
                "balance": balance
            }
        ]

        if collection1.count_documents({"bank_card": bank_card}) != 0:
            return
        collection1.insert_one(a)

    def login(self, ):
        log_cart = input("Ввидите номер свой карточке: ")
        pin_cart = int(input("Ввидите пин код"))
        var = collection1.find_one({"bank_card": self.bank_kard})["balance"]

    def balancec(self):
        xxx = collection1.find_one({"bank_card": self.bank_kard})["balance"]
        print(xxx)

    def deposit_money(self):
        summ = float(input("Введите сумму для депозита:"))
        row = collection1.find_one({"bank_card": self.bank_kard})
        print(row['name'], row['surname'])

        t1 = [{
            "name": collection1.find_one({"bank_card": self.bank_kard})["name"],
            "surname": collection1.find_one({"bank_card": self.bank_kard})["surname"],
            "карта": self.bank_kard,
            "Внесенная сумма:": summ,
        }]
        collection2.insert_one(t1)
        balance123 = collection1.find_one({"bank_card": self.bank_kard})["balance"]
        collection1.update_many({'bank_card': self.bank_kard}, {"$set": {"balance": balance123 + summ}})
        print(f"Внесенная сумма:{summ}")

    def cash_withdrawal(self):
        snyatt = float(input("Введите сумму вывода:"))
        print("При снятие и отправка денег есть комиссия в размере 1% суммы транзакции.")
        if collection1.find_one({"bank_card": self.bank_kard})["balance"] >= snyatt * 1.01:
            t2 = [{
                "name": collection1.find_one({"bank_card": self.bank_kard})["name"],
                "surname": collection1.find_one({"bank_card": self.bank_kard})["surname"],
                "карта": self.bank_kard,
                "вы сняли:": snyatt,
            }]
            collection2.insert_many(t2)
            balance123 = collection1.find_one({"bank_card": self.bank_kard})["balance"]
            collection1.update_one({'bank_card': self.bank_kard}, {"$set": {"balance": balance123 - snyatt * 1.01}})
            print(f"Вы сняли:{snyatt * 1.01}")
        else:
            print("Не хватает денег!!!")

    def Send_money(self):
        carta = int(input("Введите Банковский аккаунт получателя карты:"))
        sent = float(input("Введите сумму отправки:"))
        print("Комиссия 1%")
        if collection1.find_one({"bank_card": self.bank_kard})["balance"] >= sent * 1.01:
            t3 = [{
                "name": collection1.find_one({"bank_card": self.bank_kard})["name"],
                "surname": collection1.find_one({"bank_card": self.bank_kard})["surname"],
                "karta": self.bank_kard,
                "карта получателя": carta,
                "вы отправили :": sent
            }]
            collection2.insert_one(t3)
            balance123 = collection1.find_one({"bank_card": self.bank_kard})["balance"]
            balance124 = collection1.find_one({"bank_card": carta})["balance"]
            if carta == self.bank_kard:
                if sent <= self.bank_kard:
                    collection1.update_many({'bank_card': self.bank_kard},
                                            {"$set": {"balance": balance123 - sent * 1.01}})
                    collection1.update_many({'bank_card': carta}, {"$set": {"balance": balance124 + sent}})
                else:
                    print("У вас недастаточно денег")
            else:
                print("С перва нужна регистратция")

    def delete(self):
        collection1.delete_many({})
        collection2.delete_many({})


newBancomat = Bancomat()

print("Добро пожаловать в банкомат Академии")
print("выберите операцию который вы хотите сделать")

while 1:
    print("""1. регистрация
2. войти в акаунт
3. удалить всё
""")
    choose = int(input(":"))
    if choose == 1:
        newBancomat.registration()
    elif choose == 2:
        bank_kard1 = (input("karta:"))
        password = int(input("pin:"))
        # xato {'Anvar', '10234'}, {'Bekzod', '1234'}
        if collection1.count_documents({"bank_card": bank_kard1}) == 1 and collection1.count_documents(
                {"pin_cod": password}) == 1:
            users = collection1.find({"bank_card": bank_kard1})
            # for user in users:
            #     print(f"{user['name']}, {user['surname']}, {user['bank_card']}")
            while 1:

                print("""1. просмотр баланса
2. внесение денег
3. снятие денег
4. отправка денег
5. Завершить оперaцию""")

                x = int(input("Введите:"))

                if x == 1:
                    newBancomat.balancec()

                elif x == 2:
                    newBancomat.deposit_money()

                elif x == 3:
                    newBancomat.cash_withdrawal()

                elif x == 4:
                    newBancomat.Send_money()

                elif x == 5:
                    print("Спасибо за выбор банкомат Академии")
                    break

                else:
                    continue

        else:
            continue
    elif choose == 3:
        newBancomat.delete()
