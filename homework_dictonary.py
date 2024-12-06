users = {"mary":"12345", "naomi":"njsjuswe718", "maksik":"qwerty", "qwerty":"1q2w3e4r"}

def addUser(login, password):
    if login in users:
        print("A user with this login already exists")
    else:
        users[login] = password
        print(f"User '{login}' added")

def deleteUser(login):
    if login not in users:
        print("User with this login did not find")
    else:
        del users[login]
        print("User deleted.")

def changePassword(login, newPassword):
    if login not in users:
        print("User with this login did not find")
    elif users[login] == newPassword:
        print("New password must not be as previous password")
    else:
        users[login] = newPassword
        print("Password changed")

def checkPasswords():
    for user in users:
        if len(str(user[login]))<6 or str(user[login]).isalpha():
            print(user + " has unsecured password")

def getPassword(login):
    if login not in users:
        print("User with this login did not find")
    else:
        print(f"Password for user '{login}': {users[login]}")

a=True
while a:
    print("1-add new user\n2-delete user\n3-change password\n4-check password\n5-get password\n6-save to file\n0-exit")
    num=int(input("Enter num of information: "))
    if num==1:
        newLogin=input("Enter new login: ")
        newPassword=input("Enter new password: ")
        addUser(newLogin, newPassword)
    elif num==2:
        loginForDelete=input("Enter login: ")
        deleteUser(loginForDelete)
    elif num==3:
        login=input("Enter login: ")
        newPassword=input("Enter new password: ")
        changePassword(login, newPassword)
    elif num==4:
        checkPasswords()
    elif num==5:
        login=input("Enter login: ")
        getPassword(login)
    elif num==6:
        with open("Users_homework2.txt", "a") as f:
            for login, password in users.items():
                f.write(f"{login} - {str(password)}\n")
    elif num==0:
        a=False
    else:
        print("Error")