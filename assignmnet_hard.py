"""
Hard Level Challenge
*Challenge:* *List and Tuple Manipulation with Boolean Check*

*Problem:*  
Write a program that takes a tuple with five integers, numbers = (n1, n2, n3, n4, n5). Your program should:
1. Unpack the tuple into five variables.
2. Create a list containing only the odd numbers from the tuple.
3. If the list of odd numbers has three or more elements, print "More Odds". Otherwise, print "Fewer Odds".

*Example:*
- Input:  
  numbers = (1, 4, 7, 2, 9)
- Output:
  
  [1, 7, 9]
  More Odds
  

- Input:  
  numbers = (2, 8, 6, 4, 10)
- Output:
  
  []
  Fewer Odds
"""


numbers = tuple(input("Enter five integers seperated by ',' ").strip().split(','))

# explanation of the code above
# 1. we have an input that says 'Enter three integers seperated by ',' -> e.x 1,2,3
# 2. As we have already learnt that whatever comes into a input function would be a string
# 3. which means we would have something like "1,2,3" -> in string format
# 4. we used the string "strip" method which removes all white space in our string e.x "1, 3, 5" -> "1,3,5"
# 5. we used the string "split" method which splits the string and gives us a list in return
# 5con'td "1,4,5,5" -> .split(',') gives ['1', '4', '5', '5'] the string is splitted by the ','
# 6. We converted the returned string into a tuple using the tuple constructor

num1, num2, num3, num4, num5 = numbers

# numbers list -> the int() constructor converts the numbers to integer as it is was a string intially
# int(num1) % 2 -> the % modulo operation returns the remainder of the division if we have 0 it means the number is even
num_list = [int(num1) % 2, int(num2) % 2, int(num3) % 2, int(num4) % 2, int(num5) % 2]

# we simply count the number of even numbers in the list
even_count = num_list.count(0)

# we create a conditionsl statement to check if we have more odds or less even
# we are using 2 here because we are working with 5 integers so we can only decide which is more or less only if it's greater than 2
if even_count <= 2:
    print("More odds")
else:
    print("Fewer odds")

# Note: our solution doesn't have to look exactly the same
# in programing we have more than 1 thousand ways to do the samething but just take note of the comments and understand
# Also most of these would have been achieved easily with 'loops' which we would talk about in the next session