def validate_userInput(text, key):
    try:
        int(text)
        int(key)

        return False
    except:
        return True


def encryption(clearText, key):
    vigenere = ""
    clearText = list(clearText)
    key = list(key)
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    clearTextIndex = []
    keyIndex = []
    vigenereIndex = []
    loopCounterClearText = 0
    loopCounterKey = 0
    loopCounterVigenere = 0
    loopCounterVigenereKey = 0

    while loopCounterClearText < len(clearText):
        clearTextIndex.append(alpha.index(clearText[loopCounterClearText]))

        loopCounterClearText += 1

    while loopCounterKey < len(key):
        keyIndex.append(alpha.index(key[loopCounterKey]))

        loopCounterKey += 1

    while loopCounterVigenere < len(clearTextIndex):
        if loopCounterVigenereKey >= len(keyIndex):
            loopCounterVigenereKey = 0

        vigenereIndex.append((clearTextIndex[loopCounterVigenere] + keyIndex[loopCounterVigenereKey]) % 27)

        loopCounterVigenere += 1
        loopCounterVigenereKey += 1

    for i in vigenereIndex:
        vigenere += alpha[i]

    return vigenere
    

def decryption(cryptedText, key):
    clearText = ""
    cryptedText = list(cryptedText)
    key = list(key)
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    cryptedTextIndex = []
    keyIndex = []
    clearTextIndex = []
    loopCounterCryptedText = 0
    loopCounterKey = 0
    loopCounterClearText = 0
    loopCounterClearTextKey = 0

    while loopCounterCryptedText < len(cryptedText):
        cryptedTextIndex.append(alpha.index(cryptedText[loopCounterCryptedText]))

        loopCounterCryptedText += 1

    while loopCounterKey < len(key):
        keyIndex.append(alpha.index(key[loopCounterKey]))

        loopCounterKey += 1

    while loopCounterClearText < len(cryptedTextIndex):
        if loopCounterClearTextKey >= len(keyIndex):
            loopCounterClearTextKey = 0

        clearTextIndex.append((cryptedTextIndex[loopCounterClearText] - keyIndex[loopCounterClearTextKey]) % 27)

        loopCounterClearText += 1
        loopCounterClearTextKey += 1

    for i in clearTextIndex:
        clearText += alpha[i]

    return clearText


def main():
    error = False
    encryptionInput = input("[En]cryption or [De]cryption: ")

    if "En" in encryptionInput or "en" in encryptionInput:
        clearText = input("Enter alphabetic words/sentences: ")
        key = input("Enter an alphabetic key: ")

        if validate_userInput(clearText, key) == True:
            print('VIGENERE: %s' % encryption(clearText, key))
        elif validate_userInput(clearText, key) == False:
            print("Please enter only an alphabetic text and key")
            main()
    elif "De" in encryptionInput or "de" in encryptionInput:
        cryptedText = input("Enter the crypted text: ")
        key = input("Enter the key: ")

        if validate_userInput(cryptedText, key) == True:
            print('DECRYPTED: %s' % decryption(cryptedText, key))
        elif validate_userInput(cryptedText, key) == False:
            print("Please enter only an alphabetic text and key")
            main()
    else:
        main()


if __name__ == "__main__":
    main()