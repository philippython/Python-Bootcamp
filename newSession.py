# import statement
from random import randint, shuffle, randrange
from math import sqrt, sin, cos
from bamlak import name

# print(bootcamp_fee)
# print(bamlak_tuition)

# third-party packages
# builtin pacakages

# list -> ordered , mutable, you can access items of a list using the index
# starting first index is always 0

listOfNames = ["Jamal", "bamlak", "Mr abiodun"]

# negative indexing
thirdName = listOfNames[-2]

# updating items/item of a list
# listOfNames[-2] = "Mr Ogunyemi"

# del listOfNames[0]

# print(thirdName)
# print(listOfNames)
# print(f"{listOfNames[0]}, {listOfNames[1]} and {listOfNames[2]} are on the call")

# randomNumber = randint(2, 4)
# print(randomNumber)

# print(sqrt(25))

newList = ["Damilola", "Joy", "favor", "jamal", "bamlak"]

# append is used to add new "item" to a list

# listOfNames.append(newList)

listOfNames.extend(newList)

# listOfNames.clear()

# print(listOfNames.count("Aman"))

# print(listOfNames.index("Joy"))

listOfNames.insert(0, "mary")

listOfNames.remove("favor")
listOfNames.reverse()

copyofListofNames = listOfNames.copy()

# print(copyofListofNames)

# print(listOfNames[3])

# len() -> is used to check the length of a sequence
# string -> seq of character
# list -> seq of objects  ->


lenghtOfNewList = len(newList)
newName = "jamal"

# print(len(newName))
# print(lenghtOfNewList)

# accesssing items of a nested list
nested_list = ["jamal", "bamlak", ["odulaja", "biset", [20, 23]]]
bamlak_age = nested_list[2][2][1]
print(bamlak_age)

bamlakSurname = "brset"
# string methods
# __dir__ method -> helps you get all the methods available -> magic methtod, dunder method

# print(newName.__dir__())
# print(bamlakSurname.replace("r", "i"))
# print(bamlakSurname.count("t"))

vip = ["Damilola", "Joy", "favor", "jamal", "bamlak", "philip"]

# membership operators -> not in and in

# attendee = input("Enter your name? ")

# if attendee not in vip:
#     print("Welcome to the VVIP Section!")
# else:
#     print("Welcome to VIP Section")

# countryName = "Peru"

# python tuple -> python list, ordered,
# python list is mutable -> IT CAN BE CHANGED
# python tuple is immutable -> IT CANNOT BE CHANGED

colors = ("red", "green", "blue", nested_list)
colors = colors + ("orange", "pink")

names = "biset", "aman", "luke", "thoeed"
# print(type(names))
# blue = colors[2]
# print(blue)
# print(colors)

# unpacking a tuple
# _, _, _, _, _, pink = colors
# print(pink)

# method 1
# biset, aman, luke, thoeed = names
# print(thoeed)


# method 2
biset = names[0]
aman = names[1]
luke = names[2]
thoeed = names[3]

# myAge = colors[3][2][2][0]
# print(myAge)

# set is mutable & unordered

newSet = {"joke", "tears", "laugh", "joy"}
set = {"joke", "joy"}
# print(dir(newSet))
# union, intersection , difference


print(newSet.issuperset(set))










