def login(username, password):
    if username == "admin" and password == "1234":
        print("Login successful")
    else:
        print("Invalid username or password")


if __name__ == "__main__":
    login("admin", "1234")