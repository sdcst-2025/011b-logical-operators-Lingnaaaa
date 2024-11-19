#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 

You can use max() to help you find the largest number
You can use min() to help you find the smallest number
How can we find the middle number though?
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
x = input ('Enter a number:')
y = input ('Enter a number:')
z = input ('Enter a number:')
x = int(x)
y = int(y)
z = int(z)

if z>y>x and x**2+y**2==z**2:
    print (f'{x},{y},{z} form a Pythagorean Triple')
if z>x>y and x**2+y**2==z**2:
    print (f'{y},{x},{z} form a Pythagorean Triple')
if x>y>z and z**2+y**2==x**2:
    print (f'{z},{y},{x} form a Pythagorean Triple')
if x>z>y and z**2+y**2==x**2:
    print (f'{y},{z},{x} form a Pythagorean Triple')
if y>x>z and x**2+z**2==y**2:
    print (f'{z},{x},{y} form a Pythagorean Triple')
if y>z>x and x**2+z**2==y**2:
    print (f'{x},{z},{y} form a Pythagorean Triple')

if z>y>x and x**2+y**2!=z**2:
    print(f'{x},{y},{z} do not form Pythagorean triple')
if z>x>y and x**2+y**2!=z**2:
    print (f'{y},{x},{z} do not form a Pythagorean Triple')
if x>y>z and z**2+y**2!=x**2:
    print (f'{z},{y},{x} do not form a Pythagorean Triple')
if x>z>y and z**2+y**2!=x**2:
    print (f'{y},{z},{x} do not form a Pythagorean Triple')
if y>x>z and x**2+z**2!=y**2:
    print (f'{z},{x},{y} do not form a Pythagorean Triple')
if y>z>x and x**2+z**2!=y**2:
    print (f'{x},{z},{y} do not form a Pythagorean Triple')