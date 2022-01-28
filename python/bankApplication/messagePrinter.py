def printLoginMessage():
    print("1 | Register")
    print("2 | Login\n")

def printRegisteredHelloMessage(time, name):
    print('\nGood %s' % time, name)

def printRegisteredBalance(balance):
    print('\nCurrent balance: %s EUR\n' % balance)

def printAssignAliasMessage():
    print("Please assign an alias: ")

def printAssignPinMessage():
    print("Please assign a pin: ")

def printEnterAliasMessage():
    print("Please enter your alias: ")

def printEnterPinMessage():
    print("Please enter your pin: ")

def printEnterValidationNumberMessage():
    print("Please enter your validation number: ")

def printSuccessfullyRegistered(newAlias, newPin, index):
    print("Successfully registered (Alias: %s | PIN: %s | Validation Number: %s)" % (newAlias, newPin, index))

def printNoUserFoundToLogin():
    print("Wrong alias, pin or validation number. No user found with these criteria")

def printWrongPIN():
    print("Wrong PIN")

def printOnlyNumeric():
    print("Please enter only numbers")

def printWrongInput():
    print("Please check your input and try again")

def printSelectionMenu():
    print("1 | Withdraw money")
    print("2 | Deposit money")
    print("3 | Logout\n")

def printEnterWithdrawAmount():
    print("Please enter the amount you'd like to withdraw: ")

def printEnterDepositAmount():
    print("Please enter the amount you'd like to deposit: ")