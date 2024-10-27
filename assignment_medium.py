"""
Medium Level Challenge
*Challenge:* *Tuple Unpacking and Conditional Operations*

*Problem:*  
Write a program that takes a tuple with three integers, numbers = (a, b, c). Your program should:
1. Unpack the tuple into three separate variables.
2. Create a list with these three integers in ascending order and print it.
3. If the sum of the three numbers is greater than 20, print "High". Otherwise, print "Low".

*Example:*
- Input:  
  numbers = (8, 3, 10)
- Output:
  
  [3, 8, 10]
  High
  

- Input:  
  numbers = (2, 5, 7)
- Output:
  
  [2, 5, 7]
  Low
  
"""

numbers = tuple(input("Enter three integers seperated by ',' ").strip().split(','))

# explanation of the code above
# 1. we have an input that says 'Enter three integers seperated by ',' -> e.x 1,2,3
# 2. As we have already learnt that whatever comes into a input function would be a string
# 3. which means we would have something like "1,2,3" -> in string format
# 4. we used the string "strip" method which removes all white space in our string e.x "1, 3, 5" -> "1,3,5"
# 5. we used the string "split" method which splits the string and gives us a list in return
# 5con'td "1,4,5,5" -> .split(',') gives ['1', '4', '5', '5'] the string is splitted by the ','
# 6. We converted the returned string into a tuple using the tuple constructor

num1, num2, num3 = numbers

# numbers list -> the int() constructor converts the numbers to integer as it is was a string intially
# the sort() method sorts the numbers in ascending number

num_list = [int(num1), int(num2) ,int(num3)]
num_list.sort()

num_sum = num_list[0] + num_list[1] + num_list[2]

if num_sum > 20:
    print("High")
else:
    print("Low")