def validate_encryption_key(key):
    try:
        int(key)
        return True
    except:
        return False


def validate_input(userInput):
    try:
        int(userInput)
        return False
    except:
        return True


def encryption(key, userInput):
    caesar = ""
    key = int(key)
    userInput = list(userInput)
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    loopCounter = 0
    userIndex = 0

    while key > len(alpha) - 1:
        key -= len(alpha) - 1

    while loopCounter < len(userInput):
        userIndex = alpha.index(userInput[loopCounter])

        if userIndex + key > len(alpha) - 1:
            userIndex -= len(alpha) - 1

        caesar += alpha[userIndex + key]

        loopCounter += 1
    
    return caesar

def decryption(key, cryptedText):
    clearText = ""
    key = int(key)
    cryptedText = list(cryptedText)
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    loopCounter = 0
    cryptedTextIndex = 0

    while key > len(alpha) - 1:
        key -= len(alpha) - 1

    while loopCounter < len(cryptedText):
        cryptedTextIndex = alpha.index(cryptedText[loopCounter])

        if cryptedTextIndex + key > len(alpha) - 1:
            cryptedTextIndex -= len(alpha) - 1

        clearText += alpha[cryptedTextIndex - key]

        loopCounter += 1
    
    return clearText


def main():
    error = False
    encryptionInput = input("[En]cryption or [De]cryption: ")

    if "En" in encryptionInput or "en" in encryptionInput:
        userInput = input("Enter alphabetic letters: ")
        key = input("Enter a numeric encryption key: ")

        if validate_encryption_key(key) == False:
            print("Please enter only a numeric key")
            error = True

        if validate_input(userInput) == False:
            print("Please enter only alphabetic letters")
            error = True

        if error == False:
            print('Caesar: %s' % encryption(key, userInput))
        elif error == True:
            main()
    elif "De" in encryptionInput or "de" in encryptionInput:
        cryptedText = input("Enter the crypted text: ")
        key = input("Enter the key: ")

        if validate_encryption_key(key) == False:
            print("Please enter only a numeric key")
            error = True

        if validate_input(cryptedText) == False:
            print("Please enter only alphabetic letters")
            error = True

        if error == False:
            print('DECRYPTED: %s' % decryption(key, cryptedText))
        elif error == True:
            main()


if __name__ == "__main__":
    main()