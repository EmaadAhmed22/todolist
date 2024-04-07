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
    date_created = datetime.today().strftime("%Y-$n-%d")
    due_date = input(
        "Enter in the daye in format Year-Month-Day: "
    )  # TODO: validate this  input (check if input is properly formatted)

    taskdict = {
        "title": title,
        "description": description,
        "date_created": date_created,
        "due_date": due_date,
    }
    print(taskdict)
    return taskdict


# what we doing now
# we have db.json
# step 1 - take all of db.json and put it into a variable called dats
# notice data is a list of each task in db
# data = [{...}], [{...}], [{...}] each element in list is a taskdict
# step 2 we add our new task dict to the end of data
# we be loading and stuff
# this is what not to do


def save_entry(entry: dict):
    # TODO: try/except block

    """
    Function to write to our database
    Step 1: Open our database in reading mode and save the entire db to a variable to data
    Step 2: Append the new entry to the data variable
    Step 3: Save the new data variable and write it back to the DB
    """
    try:
        with open(
            "db.json", "r"
        ) as rfile:  # when opening a file in python use a mode to open it
            data = json.load(
                rfile
            )  # when you leave the indentation the file closes, also can use file.close()#system to add to database
    except json.decoder.JSONDecodeError:
        data = []

    data.append(entry)
    with open(
        "db.json", "w"
    ) as wfile:  # opening in writing mode so we can addd to the database using python, then we dump our data
        json.dump(data, wfile)


def list_entries():
    """
    Function that lists all the added tasks
    """
    try:
        with open(
            "db.json", "r"
        ) as rfile:  # when opening a file in python use a mode to open it
            data = json.load(
                rfile
            )  # when you leave the indentation the file closes, also can use file.close()#system to add to database
    except json.decoder.JSONDecodeError:
        data = []

    if len(data) != 0:
        for task in data:
            print(task)
    else:
        print("No tasks have been saved! Add a task")
    return data


def main():
    start = True
    while start:
        print(" Welcome to my Todo List ")
        print(" Select an option ")
        print(" 1 --> Add an entry ")
        print(" 2 --> List all my entries ")
        print(" 3 --> End application ")
        user_choice = input("Choices ")
        try:
            user_choice_num = int(user_choice)
        except ValueError:
            print(f"{user_choice} This is not a integer. Try again ")
            continue
        if user_choice_num not in [1, 2, 3]:
            print(" Choose either 1,2,3 to use this app!")
            continue
        if user_choice_num == 1:
            user_entry = user_input()  # equal to what is returned)
            save_entry(user_entry)
        elif user_choice_num == 2:
            list_entries()
        else:
            start == False


# testing functions

if __name__ == "__main__":
    main()


# line 87 makes it so main is only run
