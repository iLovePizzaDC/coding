import sys
import messagePrinter as mP
import accountHandler as aH

def checkForPin(pin, index):
    if pin == aH.getAllUsers()[index].split(",")[2]:
        return True
    else:
        mP.printWrongPIN()
        return False

def updteDB(index, amount, operator):
    editedBlances = aH.getAllBalances()
    newBalance = int(editedBlances[index][:-1])

    if operator == "+":
        newBalance += amount
    elif operator == "-":
        newBalance -= amount

    editedBlances[index] = str(newBalance) + ";"
        
    try:
        with open('python/bankApplication/balanceDB.txt', 'w') as balance:
            for data in editedBlances:
                balance.write(data)
    finally:
        balance.close()

def withdraw(index):
    while True:
        mP.printEnterWithdrawAmount()
        withdraw = input()
        mP.printEnterPinMessage()
        pin = input()

        if checkForPin(pin, index) == True:
            updteDB(index, int(withdraw), "-")
            break

def deposit(index):
    while True:
        mP.printEnterDepositAmount()
        deposit = input()
        mP.printEnterPinMessage()
        pin = input()

        if checkForPin(pin, index) == True:
            updteDB(index, int(deposit), "+")
            break

def logout():
    sys.exit(0)