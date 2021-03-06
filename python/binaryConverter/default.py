def print_binary(userInput):
    binary = math_operation(userInput)
    
    return binary

def math_operation(userInput):
    binary = ""
    dec = int(userInput)

    while dec > 0:
        binary = str(dec % 2) + binary
        dec = int(dec / 2)

    return binary

def is_int(n):
    try:
        float(n)
    except ValueError:
        return False;
    else:
        return float(n).is_integer()


def main():
    userInput = input("Enter a number: ")
    
    if is_int(userInput) == False:
        print("Please enter a validate number")
        main()
    else:
        print('Binary: %s' % print_binary(userInput))



if __name__ == "__main__":
    main()