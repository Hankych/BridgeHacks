def login():
    user = input("Input a username")
    password = input("Input a password")
    
    for account in open("accounts.txt", "r").readlines():
        login = account.split
    if user == login[0] and password ==login[1]:
        print("You are now logged in.")
        return True
    else:
        print("Incorrect. Please try again.")
        return False

def registerUser():
    user = input("Input a username: ")
    password = input("Input a password: ")
    confirmPassword = input("Confirm password: ")
    email = input("Input email: ")
    fName = input("Input First Name: ")
    lName = input("Input Last Name: ")
    age = input("Input Age: ")
    
    if password == confirmPassword:
        file = open("accounts.txt", "a")
        file.write(user)
        file.write(" ")
        file.write(password)
        file.write(" ")
        file.write(email)
        file.write(" ")
        file.write(fName)
        file.write(" ")
        file.write(lName)
        file.write(" ")
        file.write(age)
        file.write("\n")
        file.close()
        if login():
            print("You are now logged in...")
        else:
            print("You aren't logged in!")

registerUser()