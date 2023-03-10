# list => array
friend1 = "Sharukh Khan"
friend2 = "Hrittik Roshan"
friend3 = "Amir Khan"

#             0                1               2
friends = ["Sharukh Khan","Hrittik Roshan","Amir Khan"] # list or array
# print(friends)
# print(friends[1]) # accessing data


# x = ["Sharukh Khan",2,True,9.8,"Monalisa Maity"] # can contain different data type


# looping =============================
# for x in friends:
#     print(x)


# sorting =========================================
# name = ["monalisa","Debranjan","Debosmita","Didipriya","alokdut","bapi"]
# name = ["monalisa","alokdut","bapi"]
# name.sort() # asc
# name.sort(reverse = True) # desc
# print(name)


# add data ==============================================
# print(name)
# name.append("Bong Guy")
# name.append("DJ Bapan")
# name.insert(2,"Wonder Munna")
# print(name)


# update data ======================================
# students = ["monalisa","Debranjan","Debosmita","Didipriya","alokdut","bapi"]
# print(students)
# students[5] = "Soumitra"
# print(students)


# remove data =========================================
# print(students)
# # students.remove("bapi")
# # students.pop()
# students.pop(2)
# print(students)

# join lists ==============================
students = ["monalisa","Debranjan","Debosmita","Didipriya","alokdut","bapi"]
friends = ["Sharukh Khan","Hrittik Roshan","Amir Khan"]

# y = students + friends
# print(y)

# students.extend(friends)
# print(students)

for x in friends:
    students.append(x)

print(students)