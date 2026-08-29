import json
import numpy as np
from datetime import datetime

class Expence:
    def __init__(self,date,category,amount):
        self.date=date
        self.category=category
        self.amount=amount
    def add_expence(self):
        try:
            with open("Expence.json","r")as f:
                data=json.load(f)
        except(FileNotFoundError,json.JSONDecodeError):
            data={"1" : {"date": self.date, "category": self.category, "amount": self.amount}}
            with open ("Expence.json","w")as f:
                json.dump(data,f,indent=4)
        else:
            data[str(len(data)+1)] = {"date": self.date, "category": self.category, "amount": self.amount}
            with open("Expence.json","w")as f:
                json.dump(data,f,indent=4)

while True:
    i=int(input("enter 1 if you want to add expence and 0 if u want to exit."))
    if i==1:
        now=datetime.now()
        now=now.strftime("%Y-%m-%d")
        category=input("enter category of expence: ")
        amount=input("Enter amount: ")
        E=Expence(now,category,amount)
        E.add_expence()
    elif i==0:
        break
    else:
        print ("invalid Input ")
