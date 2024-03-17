# MVP 
# 1. Ability for user to save a item to database 
# 2. Ability for a user to see all items in a database


# To-do List item 
# Title, Date , Description 
import json
from datetime import datetime   

def user_input():
    """
    Function that takes to-do list in put a returns a dictionary of the item
    
    """
    title = input("Enter a title of item: ")
    description = input("Enter a description ")
    date_created = datetime.today().strftime('%Y-$n-%d')
    due_date = input("Enter in the daye in format Year-Month-Day: ")  #TODO: validate this  input (check if input is properly formatted)
    

    itemdict= {
        "title":title,
        "description":description,
        "date_created":date_created,
        "due_date": due_date


    }
    return itemdict

def save_entry(entry: dict):
    # TODO: try/except block


    """
    Function to write to our database 
    Step 1: Open our database in reading mode and save the entire db to a variable to data
    Step 2: Append the new entry to the data variable 
    Step 3: Save the new data variable and write it back to the DB
    """

    with open("db.json", "r") as file: #when opening a file in python use a mode to open it 
        data = json.load(file) #when you leave the indentation the file closes, also can use file.close()
    data.append(entry) #system to add to database
    
    with open ("db.json", "w") as file: #opening in writing mode so we can addd to the database using python, then we dump our data
        json.dump(data, file)


"""
Challenge, what happen when our database has 5000 todo items
"""

if __name__ == "__name__":
    main()
esfedd