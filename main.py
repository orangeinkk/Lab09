
def encode():
    encoded = ''
    password = input("Please enter your password to encode: ")
    for digit in password:
        if int(digit) < 7:
            encoded += str(int(digit) + 3)
        else:
            encoded += str(int(digit) - 7)
    return encoded


if __name__ == "__main__":
    while True:
        print("""Menu
-------------
1. Encode
2. Decode
3. Quit
""")
        choice = int(input("Please enter an option: "))
        if choice == 1:
            password = encode()
            print("Your password has been encoded and stored!\n")
        elif choice == 2:
            decode()
        elif choice == 3:
            break
