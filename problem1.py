"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is not frue
"""

#! python3
x = int(input())

if (x % 6) == 0 and (x % 8) != 0:
    x = str(x)
    print(x + " is frue")
else:
    x = str(x)
    print(x + " is not frue")