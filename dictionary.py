# print("Hello Champions.")
# dictionary ============== 
# can't contain duplicate value
my_dict = {
    "name":"Monalisa Maity", # key: value
    # "name":"Sourav Gangully", # can't contain duplicate value
    "clg":"HIT", # clg => key -------------- HIT => value
    "age":20,
    "address":"Haldia",
    "likes":["Gym","Shopping","Travelling"],
    "travel":{
        "first":"Digha",
        "second":"Puri",
        "third":"Darjeeling"
    }
}

print(my_dict) # ========== print actual dictionary

# my_dict["education"] = "CSC" # ========= adding data into dictionary
# my_dict["dislike"] = "red" # ========= adding data into dictionary

# my_dict["age"] = 22 # ===== change or update data into dictionary

my_dict.pop("travel")

print()
print(my_dict)
# print(len(my_dict)) # =============== length of the dictionary
# print(my_dict["travel"]) # ========== accessing dictionary data
# print(my_dict['name']) # ========== accessing dictionary data
# print(my_dict["likes"]) # ========== accessing dictionary data