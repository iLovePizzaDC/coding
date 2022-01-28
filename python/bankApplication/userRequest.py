import messagePrinter as mP
import accountHandler as aH
import bankOptions as bO

def loginOrRegisterRequest(selection):
    if selection == "1":
        mP.printAssignAliasMessage()
        newAlias = input()
        mP.printAssignPinMessage()
        newPin = input()

        try:
            with open('python/bankApplication/userDB.txt', 'r') as user:
                userIndex = len(user.read().split(";"))
        finally:
            user.close()

        aH.register(str(userIndex), newAlias, newPin)
    elif selection == "2":
        mP.printEnterAliasMessage()
        alias = input()
        mP.printEnterPinMessage()
        pin = input()
        mP.printEnterValidationNumberMessage()
        index = input()

        aH.login(index, alias, pin)
    else:
        mP.printWrongInput()

def loggedInBankOptions(userIndex, selection):
    if selection == "1":
        bO.withdraw(userIndex)
    elif selection == "2":
        bO.deposit(userIndex)
    elif selection == "3":
        bO.logout()
