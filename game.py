from random import randint

def Game():
    chance= 5
    Correct_Number= randint(1,100)
    

    while chance > 0:
      Guess= int(input("Guess a number between 1 and 100! "))

      
      if Guess > Correct_Number :
        chance -= 1
        print ("Too high")
      elif Guess < Correct_Number:
        chance -= 1
        print ("Too Low")
      elif chance > 0 and Guess == Correct_Number:
        print("You are a winner")
        break   

    if chance == 0: print(f"You have lost the correct number is {Correct_Number}")
    # ternary operator -> short-hand if statement
        
# Game()
race = "american"
my_gender = "male"

color = "black" if race == "african" else "white"

# print(color)

# print(True) if my_gender == "male" else print(False)

def factorial(n : int):
 if n < 0 : return "Factorial is not defined for non negative numbers"
 if n == 0 or n == 1 : return 1

 while n > 1:
  return n * factorial(n-1)

Your_number= input("What is integer do you want the factorial of? ")

print(factorial (int(Your_number)))