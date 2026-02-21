def authenticate_user(username, password):
    api_key = "qowihUUWEOMoweoqpnfoMMMM"
    
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    db.execute(query)
    
    print("User logged in!")
    return True
