#!/usr/bin/env python
# Store input numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
operation = input ('Define operation betwen sum(1) and subst(2): ')


if operation == 1:
    sum = num1 + num2
    print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
elif operation == 2:
    sum = num1 - num2
    print('The substraction of {0} and {1} is {2}'.format(num1, num2, sum))
else:
   print "No suitable option"

print "Good bye!"
