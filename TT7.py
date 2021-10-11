import json

student_list = ['pam','rob','joe','greg','bob','amy','matt']
print(student_list[2:5])  # The following print statement includes elements at index 2 & excludes element at index 5
print(student_list[:-5])  # print elements beginning to 4th
print(student_list[5:])  # print elements 6th to end (index 5)
print(student_list)  # print elements beginning to end
# check if rob is in the student_list
for name in student_list:
    if name == "rob":
        print(True)

p1 = {"name":"John", "age":61, "city":"Eugene"}
p2 = {"name":"Risa", "age":16, "city":"New York"}
p3 = {"name":"Ryan", "age":16, "city":"Los Angeles"}
p4 = {"name":"Shekar", "age":16, "city":"San Francisco"}

list_of_people = [p1, p2, p3, p4]  # a list of dictionaries

# write some code to Print List of people one by one
for person in list_of_people:
    print(person["name"])

# turn list to dictionary of people
dict_people = {'people': list_of_people}
print("List to Dictionary of people")
print(type(dict_people))
print(dict_people)

# write some code to Print People from Dictionary
for people in dict_people["people"]:
    print(people)

# turn dictionary to JSON
print("** Dumps - Python to JSON String**")
json_people = json.dumps(list_of_people)
print("JSON People #1")
print(type(json_people))
print(json_people)

# write some code to pretty print the JSON dict
print("JSON People #2")
print(json.dumps(list_of_people, indent=4))

# write some code to unwind JSON using json.loads and print the people
print("** Loads - JSON to Python Dict**")
json_dict = json.loads(json_people)
print(json_dict)
# to list
json_list = json.dumps(json_people)
print(json_list)
"""
names = [person['name'] for person in json_dict]
print("Names of people to list: " + str(names))
print("Names of people: ")
# pretty print Names of People
"""

