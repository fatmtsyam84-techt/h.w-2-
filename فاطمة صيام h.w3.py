name ="fatma"
pass_word= 5879
user = input("enter the username")
if user == name:
    password = int(input("enter the password"))
    if password == pass_word:
        role =input("please write if you are admin , moderator or user")
        if role == "admin":
            print("Welcome Admin")
        elif role== "moderator":
            print("Welcome Moderator")
        elif role== "user":
            print("Welcome User")
        else:
            print("Unknown role")
    else:
        print("Wrong password")
else:
    print("Wrong password")


