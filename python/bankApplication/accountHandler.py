import re
import messagePrinter as mP
import userRequest as uR
import timeHandler as tH

def getAllUsers():
    try:
        with open('python/bankApplication/userDB.txt', 'r') as user:
            allUsers = user.read().split(";")
    finally:
        user.close()

    return allUsers

def getAllBalances():
    try:
        with open('python/bankApplication/balanceDB.txt', 'r') as balance:
            allBalances = balance.read()
    finally:
        balance.close()

    balance =  [e+";" for e in allBalances.split(";") if e]

    return balance

def checkSelection(selection):
    if selection == "1" or selection == "2" or selection == "3":
        return True
    
    return False

def register(index, newAlias, newPin):
    try:
        with open('python/bankApplication/userDB.txt', 'a') as user:
            user.write(index + "," + newAlias + "," + newPin + ";")
    finally:
        user.close()

    try:
        with open('python/bankApplication/balanceDB.txt', 'a') as balance:
            balance.write("0;")
    finally:
        balance.close()

    print(mP.printSuccessfullyRegistered(newAlias, newPin, index))

def login(index, alias, pin):
    allUsers = getAllUsers()
    allBalances = getAllBalances()
    currentUser = index + "," + alias + "," + pin

    if currentUser in allUsers:
        userIndex = allUsers.index(currentUser)
        aliasAndPinHolder = allUsers[userIndex].split(",")
        currentBalance = allBalances[userIndex][:-1]

        while True:
            tH.createTimestamp()
            mP.printRegisteredHelloMessage(tH.createTimestamp(), aliasAndPinHolder[1])
            mP.printRegisteredBalance(currentBalance)
            mP.printSelectionMenu()
            selection = input()

            if checkSelection(selection) == True:
                break

        uR.loggedInBankOptions(userIndex, selection)
    else:
        mP.printNoUserFoundToLogin()