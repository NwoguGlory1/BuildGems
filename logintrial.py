# # Create a function that displays the following operations to be performed by a user.
# #  add user, first name, last name, age, marital status. 
# # the user can edit. You should check that user if the user exists and if not, display the user, the error, user entry value not found. 
# # But if it's found, it's able to edit the details. 
# # delete user. You should check if the user exists and if not, display that the user entry value is not found.
# # And if found, to delete the user from the user store,
# # to display all users on the user store. So that's the function I supposed to create.
# #  Then another question, create a function that receives the following inputs from a user, the first name, last name, age, marital status, 
# # and then save the inputs for each user in your desired data structure and prints all the entries collected.  
# # Do not give me the answers to the questions just yet but you can  guide me with each attempt I make, 
# # giving me only pointers.

# import json
# #empty dictionary
# user_data = []

#  #Add user by asking for first name, last name, age, marital status
# def add_user():
#     user_entry = {
#     user_entry["first_Name"] = input("Enter your first name: ")
#     user_entry["last_Name"]= input("Enter your last name: " )
#     user_entry["age"] = int(input("Enter your age: "))
#     user_entry["marital_Status"] = input("Enter your marital status: ")
#     }
#     return user_entry

# #return sends value it returns to the place its function is called
# # return does not magically create variables outside the function
# # you will receive the values returned into a variable you will create
# user_data = add_user()
# print(user_data)
# print(type(user_data))  # <class 'dict'>

# while True:
#     def update_user():
#         print("Do you want to register another user? Respond with YES or NO")
#         if input == YES:
#             add_user() 
#         else:
#             break
#         return

# def save_user():
#     user_data = add_user()
#     update_user()
# # first, convert collected python data to a string JSON 
# # JSON cannot convert functions, so assign the returned value to a variable before using json.dumps on that variable 
#     json_string = json.dumps(user_data) 
#     print(type(json_string)) #the class str. Serialized!

# # then save the string to a file
#     with open("data.json", "w") as f:
#         x = f.write(json_string)
#     # print(type(x))  #the class int cause write returns no of characters written


# # to read it from the file 
# with open ("data.json", "r") as f:
#     string_from_file = f.read()
#     # print(type(string_from_file)) #the class str 

# # convert string to python object (list)
# my_saved_data = json.loads(string_from_file)
# # print(type(my_saved_data)) #class list

# # def edit_user():
# # if user in 

# # def delete_user():

# # def display-all-users():