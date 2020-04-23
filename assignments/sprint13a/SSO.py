print("Hello! please sign in: ")

while True:
    
    user = input("Username: ")
    passw = input("Password: ")

    if user == "test" and passw == "pass":
        print("Success!")
        break
    else:
        print("Oops, incorrect username or password!")
