
def encode():
    encoded = ''
    password = input("Please enter your password to encode: ")
    for digit in password:
        if int(digit) < 7:
            encoded += str(int(digit) + 3)
        else:
            encoded += str(int(digit) - 7)
    return encoded


def decode(key):
    decoded_key = ''
    for i in key:
        if int(i) - 3 >= 0:
            decoded_key += f'{int(i)-3}'
        else:
            decoded_key += f'{int(i)+7}'

    return decoded_key


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
            print(f'The encoded password is {password}, and the original password is {decode(password)}')
        elif choice == 3:
            break
