def register(username, email, password):
   
    user = {
        "username": username,
        "email": email,
        "password": password
    }

    print("Registration successful!")
    return user


# Example usage
new_user = register(
    "Sanjana",
    "sanjana@example.com",
    "password123"
)

print(new_user)