#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""
x = int(input())
y = int(input())

if x > y:
    big = x
    small = y
    if (big % small) == 0:
        small = str(small)
        big = str(big)
        print(small +" is a factor of " + big)
    else:
        small = str(small)
        big = str(big)
        print(small + " is not a factor of " + big)
elif y > x:
    big = y
    small = x
    if (big % small) == 0:
        small = str(small)
        big = str(big)
        print(small +" is a factor of " + big)
    else:
        small = str(small)
        big = str(big)
        print(small + " is not a factor of " + big)
