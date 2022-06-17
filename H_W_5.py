'''1. Make a code that will take the input of two strings.
If the two inputs are the same,
your program will print “SAME”.
 If Not, It should show “NOT Same” and check which one is greater and print that.'''

Input_1 = input ("statment_1: ")
Input_2 = input ("statment_2: ")
if Input_1 == Input_2:
    print("same")

else:
    print("not same")
    if Input_1 > Input_2:
        print("Input_1 is grater")
    else:
        print("Input_2 is grater")

''' Question 2
# Make a calculator, which will work as the following algorithm:
# a. Input 1st Number
# b. Input what you want to do with numbers (+, -, *, or /)
# c. Input 2nd Number
# d. Do calculation
# e. Show Result'''

num_A = float(input("please enter a number:"))
Operator = input ("please enter an operater: ")
num_B = float(input ("please enter a number:"))


if Operator == '+':
    addition = num_A + num_B
    print(num_A, '+', num_B, '=', addition)

elif Operator == '-':
    subtraction = num_A - num_B
    if num_A > num_B:
       print(num_A, '-', num_B, '=', subtraction)
    elif num_A < num_B:
       print(num_A, '-', num_B, '=', subtraction)

elif Operator == '*':
    multiplication = num_A * num_B
    print(num_A, '*', num_B, '=', multiplication)

elif Operator == '/':

    if num_B == 0:
        print('\'ZeroDivisionError\' occurred! Numbers cannot be divided by 0.')
    else:
        division = num_A / num_B
        print(num_A, '*', num_B, '=', division)

else:
    print('Please provide a valid operator (+, -, *, or /) and run the program again.')


# 3 Average rainfall (without using formula)
print("Average rainfall (without using formula)")

Rainfall = [22, 3.4, 1, 8, 19, 21]

sum_elements = Rainfall[0] + Rainfall[1] + Rainfall[2]  + Rainfall[3] + Rainfall[4] + Rainfall[5] #(22 + 3.4 + 1 + 8 + 19 + 21)
num_elements = 6
average_rainfall = sum_elements / num_elements

print('Average rainfall: ', average_rainfall)







#Q4
'''A school has the following rules for the grading system:
  a. Below 25 - F
  b. 25 to 45 - E
  c. 45 to 50 - D
  d. 50 to 60 - C
  e. 60 to 80 - B
  f. Above 80 – A
Ask the user to enter marks and print the corresponding grade.'''

Marks = float(input('marks:'))
if Marks < 25:
    print('Garde F')
elif Marks >= 25 and Marks <= 45:
    print ('Garde E')
elif Marks >= 45 and Marks <= 50:
    print ('Garde D')
elif Marks >= 51 and Marks <= 60:
    print ('Garde C')
elif Marks >= 61 and Marks <= 80:
    print ('Garde B')
elif Marks >= 80 and Marks <= 100:
    print ('Garde A')
else:
    print('error')





