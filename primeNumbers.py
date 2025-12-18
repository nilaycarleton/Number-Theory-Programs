'''
COMP 1005/1405 Section D - Assignment 2
    Project Details:
        Name: Nilay Sorathia
        Student #: 101345637
        Date Created: [September 10th, 2024]
'''

import random

# Generates a number between 1 and 30. Also, print it out.
num = random.randint(1,30)
print(f"The generated number: {num}")

def findDivisor(num):
    divisors = []
    for x in range(1, num + 1):
        if (num % x  == 0):
            divisors.append(x)
    return divisors

divisor = findDivisor(num) # Stores the lists of divisors.

if (num < 2): # If the random number is less than 2, then it's not a prime number.
    print(f"{num} is not a prime number.")
elif (len(divisor) == 2): # If the list of divisors has only 2 numbers, then it's a prime number.
    print(f"{num} is a prime number.")
else: # If the number of divisors is more than 2, then it's not a prime number.
    print(f"{num} is not a prime number.")