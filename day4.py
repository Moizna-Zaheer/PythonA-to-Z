# sets 
rollno = {30013,30010,30021,30007,30001}
newrollno = {30032,30059,30013}

# difference of two sets
difference = rollno.difference(newrollno)
print("Difference = ",difference)

# union of two sets 
rollno = rollno.union(newrollno)
print("Union = ",rollno)

# intersection of two sets 
rollno = rollno.intersection(newrollno)
print("Intersection = ",rollno)

# sets
group1 = {"ayesha","sadia","memona","moizna"}
group2 = {"roha","tahreem","ajwa","moizna"}
group3 = {"arooba","fakhra","moizna"}

# difference of three sets
difference3 = group1.difference(group2,group3)
print("Difference of three sets = ", difference3)

# union of three sets
union3 = group1.union(group2,group3)
print("Union of three sets = ", union3)

# intersection of three sets
intersection3 = group1.intersection(group2,group3)
print("Intersection of three sets = ", intersection3)


# dictionary
dic = {"name":"moizna",
       "semester":7,
       "rollno.":30013,
       "CGPA": 3.11,
       "subject":"computer"}
print(dic)
dic.update({"semester":8})
print(dic)
dic1 = dic.copy()
print(dic1)
dic.clear()
print(dic)