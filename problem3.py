#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""
x = int(input())
y = int(input())
z = int(input())

if x > y and x > z:
    longest = x
    if y > z: 
        middle = y
        shortest = z
        if longest ** 2 == middle ** 2 + shortest ** 2:
            longest = str(longest)
            middle = str(middle)
            shortest = str(shortest)
            print(shortest + "," + middle + "," + longest + " form a Pythagorean triple")
        else:
            longest = str(longest)
            middle = str(middle)
            shortest = str(shortest)
            print(shortest + "," + middle + "," + longest + " do not form a Pythagorean triple")
    elif z > y: 
        middle = z
        shortest = y
        if longest ** 2 == middle ** 2 + shortest ** 2:
            longest = str(longest)
            middle = str(middle)
            shortest = str(shortest)
            print(shortest + "," + middle + "," +longest + " form a Pythagorean triple" )
        else:
            longest = str(longest)
            middle = str(middle)
            shortest = str(shortest)
            print(shortest + "," + middle + "," + longest + " do not form a Pythagorean triple")
elif y > x and y > z:
    longest = y
    if x > z: 
        middle = x
        shortest = z
        if longest ** 2 == middle ** 2 + shortest ** 2:
            longest = str(longest)
            middle = str(middle)
            shortest = str(shortest)
            print(shortest + "," + middle + "," + longest + " form a Pythagorean triple" )
        else:
            longest = str(longest)
            middle = str(middle)
            shortest = str(shortest)
            print(shortest + "," + middle + "," + longest + " do not form a Pythagorean triple")
    elif z > x: 
        middle = z
        shortest = x
        if longest ** 2 == middle ** 2 + shortest ** 2:
            longest = str(longest)
            middle = str(middle)
            shortest = str(shortest)
            print(shortest + "," + middle + "," + longest + " form a Pythagorean triple" )
        else:
            longest = str(longest)
            middle = str(middle)
            shortest = str(shortest)
            print(shortest + "," + middle + "," + longest + " do not form a Pythagorean triple")
elif z > x and z > y:
    longest = z
    if y > x: 
        middle = y
        shortest = x
        if longest ** 2 == middle ** 2 + shortest ** 2:
            longest = str(longest)
            middle = str(middle)
            shortest = str(shortest)
            print(shortest + "," + middle + "," +longest + " form a Pythagorean triple" )
        else:
            longest = str(longest)
            middle = str(middle)
            shortest = str(shortest)
            print(shortest + "," + middle + "," + longest + " do not form a Pythagorean triple")
    elif x > y: 
        middle = x
        shortest = y 
        if longest ** 2 == middle ** 2 + shortest ** 2:
            longest = str(longest)
            middle = str(middle)
            shortest = str(shortest)
            print(shortest + "," + middle + "," +longest + " form a Pythagorean triple" )
        else:
            longest = str(longest)
            middle = str(middle)
            shortest = str(shortest)
            print(shortest + "," + middle + "," +longest + " do not form a Pythagorean triple")


