def print_hex(userInput):
    hex = math_operation(userInput)

    return hex

def math_operation(userInput):
    hex = ""
    hexPos = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    dec = int(userInput)
    loopTimes = 8

    while dec > 0 or loopTimes > 0:
        mod = (dec % 16) * 16
        hex = str(mod) + hex
        dec = int(dec / 2)
        loopTimes -= 1

    return hex

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
        print('HEX: %s' % print_hex(userInput))



if __name__ == "__main__":
    main()