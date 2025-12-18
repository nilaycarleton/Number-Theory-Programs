'''
COMP 1005/1405 Section D - Assignment 2
    Project Details:
        Name: Nilay Sorathia
        Student #: 101345637
        Date Created: [September 10th, 2024]
'''

num = int(input("Please enter a number to find all of it's divisors: ").strip())

def findDivisor(num): # Setting the parameters as the input number.
    divisors = [] 
    for x in range(1, num + 1):
        if (num % x  == 0): # Check if the number in the provided range gives a remainder of 0 by being divided by the input number. 
            divisors.append(x) # If true, then add the divisor to the end of the list.
    return divisors # Once the for loop is terminated, the list is returned to the function.

print(f"The divisors of {num}: {findDivisor(num)}")