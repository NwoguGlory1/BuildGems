# Create a function that displays the following operations to be performed by a user.
#  add user, first name, last name, age, marital status. 
# the user can edit. You should check that user if the user exists and if not, display the user, the error, user entry value not found. 
# But if it's found, it's able to edit the details. 
# delete user. You should check if the user exists and if not, display that the user entry value is not found.
# And if found, to delete the user from the user store,
# to display all users on the user store. So that's the function I supposed to create.
#  Then another question, create a function that receives the following inputs from a user, the first name, last name, age, marital status, 
# and then save the inputs for each user in your desired data structure and prints all the entries collected.  
# Do not give me the answers to the questions just yet but you can  guide me with each attempt I make, 
# giving me only pointers.

import json
users = []

#Add user by asking for first name, last name, age, marital status
def add_user():
    user_entry = {
        "first_Name": input("Enter your first name: "),
        "last_Name": input("Enter your last name: " ),
        "age": int(input("Enter your age: ")),
        "marital_Status": input("Enter your marital status: ")
    }
    return user_entry

# display users
def display_all_users(users):
    if not users:
        print("user entry empty")
    else:
        for user in users:
            print(user)
        

def update_user():
    name = input("Enter the first name of the user you wish to update:")
    for user in users:
        if user["first_Name"] == name:
          user["first_Name"]  = input("Enter the new first name: ")
          user["last_Name"]  = input("Enter the new last name: ")
          user["age"]   = int(input("Enter the new age: "))
          user["marital_Status"]   = input("Enter the new marital status: ")
          print("User details updated!")
          return
    print("user entry value not found")


def delete_user(users):
    name = input("Enter the first name of the user you wish to delete")
    for user in users:
        if user["first_Name"] == name:
            users.remove(user)
            print("User is deleted!")
            return
        print("user entry value is not found!")


while True: 
    print("\n1. Add User?")
    print("2. Display User?")
    print("3. Edit User?")
    print("4. Delete User?")
    print("5. Do nothing")

    choice = input("Enter a number to choose: ")
    if choice == "1":
        user = add_user()
        users.append(user)
    elif choice == "2":
        display_all_users(users)
    elif choice == "3":
        update_user()
    elif choice == "4":
        delete_user(users)
    elif choice == "5":
        break


#return sends value it returns to the place its function is called
# return does not magically create variables outside the function
# you will receive the values returned into a variable you will create


# while True:
#     user = add_user()
#     users.append(user)
#     Question = input("Register another user? yes or no: ").lower()
#     if Question != 'yes':
#         break

# def save_user():
#     user_data = add_user()
#     update_user()
# first, convert collected python data to a string JSON 
# JSON cannot convert functions, so assign the returned value to a variable before using json.dumps on that variable 
#     json_string = json.dumps(user_data) 
#     print(type(json_string)) #the class str. Serialized!

# # then save the string to a file
#     with open("data.json", "w") as f:
#         x = f.write(json_string)
    # print(type(x))  #the class int cause write returns no of characters written


# to read it from the file 
# with open ("data.json", "r") as f:
#     string_from_file = f.read()
#     # print(type(string_from_file)) #the class str 

# # convert string to python object (list)
# my_saved_data = json.loads(string_from_file)
# print(type(my_saved_data)) #class list
