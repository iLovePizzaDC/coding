import messagePrinter as mP
import userRequest as uR

def checkSelection(selection):
    if selection == "1" or selection == "2":
        return True
    
    return False

def main():
    while True:
        selection = input(mP.printLoginMessage())
        uR.loginOrRegisterRequest(selection)

        if checkSelection(selection) == True:
            break

if __name__ == "__main__":
    main()