def checkPassword(password, passwordConf):
    has_a_number = False
    has_uppercase = False
    # check if both passowrd do not match
    if password != passwordConf:
        return False
    # checking the pasword length

    if len(passwordConf) < 8:
        return False
    # check for a number in the password

    for el in password:
        if el.isnumeric():
            has_a_number = True
    if has_a_number == False:
        return False
    # check for uppercase
    for el in password:
        if el.isupper():
            has_uppercase = True
    if has_uppercase == False:
        return False

    # return True if all is well

    return True


def displayDetails(name, surname, password, passConf):

    print(
        f"\n\nHi {name},\n\nyour full name is : {name +' '+surname}.\nyour password {'*'*len(password) }\n\nBest\nAlliance Team. ")


def register():

    name = input("Please input your name: ")
    surname = input("Please input your surname: ")

    while True:
        password = input("Please input your password: ")
        passConf = input("Please confirm your password: ")
        if checkPassword(password, passConf) == False:
            print(f"\n\nPassword is incorrect!!! Please make sure the followings are correct:\n\n1.\tPassowrd length is atleast 8 or more characters\n2.\tpassword has atleast one numeric\n3.\tpassword has atleast one uppercase\n4.\tpassword and password confirmation should match\n\n")
        else:
            break

    displayDetails(name, surname, password, passConf)
    return
