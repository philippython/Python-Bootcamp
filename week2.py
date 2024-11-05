# loop -> doing something repeatedly 
# for loop -> used when we want to loop a no of times or
# when we have an existing sequence and we want to perform an operation on each item of that sequence

# while loop
# a while loop would keep running aas far as a condition is met

# week_three_list = [1, 24, 20, 34, 17 ,10]

# even_count = 0


# # first for loop ever
# for num in week_three_list:
#     print("loop is running...")
#     if num < 0:
#         print("bamlak is greater 20")
#         even_count += 1
#     else:
#         pass


# print(even_count)


# for i in range(0,5):
#     print(i)
#     print("I love Python")

# salary = 1000

# while salary > 0:
#     salary -= 100
#     print("You paid your bill of $100")
# print("You're not permitted to live here")

# declaring a function or creating function -> parameters, arguments
# def first_function():
    # function body
    # pass

# # call the function
# first_function()

# def calcAge(role, year, name):
#     age = 2024 - year
#     print(f'{name} is {age} yrs old, he is a {role}')

# calcAge("QA Engineer", 1972, "Mr Abiodun")

#  types of function arguments -> default argument,positional argument, keyword argument

# functions with outputs
def spaceCounter(string):
    # tell us how many spaces we have in the string
    # "john  "
    stringLenghtWithSpaces = len(string)
    stringLengthWithoutSpaces = len(string.replace(" ", ""))
    spaces = stringLenghtWithSpaces - stringLengthWithoutSpaces
    if spaces > 0:
        return "We have spaces within the string"
    elif spaces == 0:
        return "We have no space"

    # what is the return statement -> basically using the "return keyword to return a value or terminate execution of a function"



# spaces -> spaceCounter("Py conference Paris")
# name = "john"
# print(name)

# spacesReturned = spaceCounter("86tt6uygi;ikukygilhj")
# print(spacesReturned)

# type hinting "hint"
def addition_multiplication(a: int, b: int):
    addition = a + b
    multiplication = a * b
    return addition, multiplication

addition_multiplication(9, 4)

sum, multiply = addition_multiplication(9, 4)
print(sum)
print(multiply)

#  recursion -> is a concept whereby a function calls itself

#  4! -> 4*3*2*1

# def factorial_recursive(n: int):
#     if n < 0:
#         return "Factorial is not defined for negative numbers."
#     if n == 0 or n == 1:
#         return 1
#         # 4 * factorial_recursive(3) * 3 * factorial_recursive(2) * 2 * factorial_recursive(1) * 1
#     return n * factorial_recursive(n - 1)

# number = 5
# print("Factorial (using recursion):", factorial_recursive(number))

# python dictionary
# boy -> a boy is a male child
# key -> value

# new_dict = {
#     "3992152019": "$200",
#     "9229975019": "$2100",
#     "bamlak" : 750,
#     "name" : "james",
#     111 : "768",
#     1 : [90,0]
#     # ["1", "2"]: 900
# }

# grabbing or acccessing a dictionary value
# print(new_dict["name"])


# new_dict["name"] = "python dev"

# print(new_dict.get(101))
# new_dict.update({"aman": 2300})

# print(new_dict.items())

# new_dict.pop(101, "philip")

# new_dict.popitem()
# new_dict.popitem()
# print(new_dict)
# creating a dictionary
country_capitals = {
  "Germany": "Berlin",
  "Canada": {"Ontario": "Ottawa"},
  "England": "London"
}

ottawa = country_capitals.get("Canada").update({"Saskatchewan": "Saskatoon"})
# printing the dictionary
print(country_capitals)

# # looping over a dictionary [("Germany", "Berlin")]
# for capital in country_capitals.values():
#     print(capital)

d1 = {1: "john", 2 : "jubril"}
d2 = {3: "abiodun", 4: "jubril"}
d3 = d1 | d2
print(d3)