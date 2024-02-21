import string
#This line imports the string module,
#which contains various string constants and helpful functions for string manipulation.

import getpass 
#This line imports the getpass module, which provides a portable way to handle password prompts securely.
# It allows users to input passwords without displaying them on the screen.
def check_pwd():
    password = getpass.getpass(prompt="Enter Password: ")
    #This line prompts the user to enter a password securely without echoing the characters on the screen,
    # using the getpass.getpass() function.
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0
#These lines initialize variables to keep track of the password strength (strength),
#any remarks about the password (remarks), and counts for different types of characters 
#in the password (lower_count, upper_count, num_count, wspace_count, special_count)
    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count +=1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count +=1
        else:
            special_count +=1

    if lower_count >= 1:
        strength +=1
    if upper_count >= 1:
        strength +=1
    if num_count >= 1:
        strength +=1
    if wspace_count>=1:
        strength +=1
    if special_count>=1:
        strength +=1

    if strength == 1:
        remarks = "Very Bad Password!!! Change ASAP"
    elif strength == 2:
        remarks = "Not A Good Password!!! Change ASAP"
    elif strength ==3:
        remarks = "It's a weak password, consider changing"
    elif strength == 4:
        remarks = "It's a hard password, but can be better"
    elif strength == 5:
        remarks = "A very strong password"

    print('Your password has: ')
    print(f"{lower_count} lowercase characters")
    print(f"{upper_count} uppercase characters")
    print(f"{num_count} numeric characters")
    print(f"{wspace_count} whitespace characters")
    print(f"{special_count} special characters")

    print(f"Password Strength:{strength}")
    print(f"Hint: {remarks}")

def ask_pwd(another_pwd=False):
    valid = False
    if another_pwd:
        choice=input('Do you want to enter another pwd (y/n): ')
    else:
        choice=input('Do you want to check pwd (y/n): ')

    while not valid:
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            return False
        else:
            print('Invalid, Try Again')

if __name__ == '__main__':
    print('* welcome to Password checker *')
    ask_pw = ask_pwd()
    while ask_pw:
        check_pwd()
        ask_pw = ask_pwd(True)
