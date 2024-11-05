# yeild statement and generator function
# def generator(num: int):

#     # 0, 1, 2, 3, 4, 5
#     for i in range(0, num+1):
#         yield i

# gen = generator(5)

# for generated_value in gen:
#     print(generated_value)

# first class function -> is a function that can be treated as a variable and can be passed into another function
def greet(name: str):
    print(f"Hey {name}")


greeter = greet

greeter("Bamlak")

# higher order function is a function that accepts other functions as parameter
# def greet_multiple(num: int, func):
#     for i in range(1, num+1):
#         func("Aman")


# variable_gm = greet_multiple
# variable_gm(4, greet)

# scope -> global scope, enclosing scope , local scope

name = "Bamlak"


def test():
    # enclosing scope
    name = "john"
    y = 10
    def inner_test():
        # # local scope
        # global x
        # x = 30

        # nonlocal name
        # name = "test"

        # z = 5
        print("Inner test was called")
    return inner_test

returned_function = test()
returned_function()













