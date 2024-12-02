
def client_search(name, data):
    # This function takes in a string and assigns all of this client's info to a dictionary.
    
    client = {}  # The main profile to compare all of the values to
    client_index = None  # To store the row index
    
    for index, row in enumerate(data):  # Use enumerate to get both the index and the row
        if row["  What’s your name or nickname?  (First name or preferred name only)"] == name:
            client = row  # Assign the row
            client_index = index  # Store the index
            break
    
    if client:
        return client, client_index  # Return both the client and the index
    else:
        print("Client not found")
        return None, None