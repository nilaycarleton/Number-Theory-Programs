'''
COMP 1005/1405 Section D - Assignment 2
    Project Details:
        Name: Nilay Sorathia
        Student #: 101345637
        Date Created: [September 10th, 2024]
'''

def numValid():
    while True: # The loop continuously loops until the user has entered 2 valid numbers.
        num1 = input("Please enter the 1st number between 100 and 999: ").strip()
        num2 = input("Please enter the 2nd number between 100 and 999: ").strip()
        
        if (len(num1) == 3 and len(num2) == 3 and num1 < num2): # Checks if each number has only 3 digits and 1st number is less than the 2nd number. All of these conditons must be met. 
            num1 = int(num1) # Converts each number into an integer.
            num2 = int(num2)
            return num1, num2  
        else: 
            print("\nPlease re-enter numbers between 100 and 999.") 

def numNarc(num):
    hunds = num // 100 # Gets the 1st digit of the number by dividing it by 100 and rounding it down to the nearest whole number.
    tens = (num // 10) % 10 # Gets the 2nd digit of the number by dividing it by 10 and rounding it down to the nearest whole number then dividing it by 10 again and getting the remainder of that division. 
    ones = num % 10 # Gets the 3rd digit of the number by dividing it by 10 and getting the remainder of the division.
    return num == (hunds ** 3 + tens**3 + ones ** 3) # Compares the original number and the calculated narcissistic number to check if the number is narcissistic. 

def narcRange(num1, num2): 
    narcissisticNumbers = []
    for num in range(num1, num2 + 1): 
        if numNarc(num): # Uses the function to check if any number in the range is a narcissistic number.
            narcissisticNumbers.append(num) # If a number is a narcissistic number, then add the number to the end of the list. 
    return narcissisticNumbers 

def main():
    flag = True
    while flag: # The loop will at least run once because the flag is set to true.
        num1, num2 = numValid() # Runs the functions which run the prompts and checks for validity.
        narcNumbers = narcRange(num1, num2) # If the numbers are valid, then this functions to identify narcissistic numbers in the following range.

        if (len(narcNumbers) > 0): # Check if the list has any narcissistic numbers. 
            print(f"Narcissistic numbers between {num1} and {num2} are: {narcNumbers}") # If the list does have narcissistic numbers, then it would print the list and the numbers for narcissistic numbers found. 
            print(f"Total Narcissistic numbers found: {len(narcNumbers)}")
        else:
            print(f"No Narcissistic numbers found between {num1} and {num2}.") 
        
        choice = ((input("Do you want to check another range? Enter yes to continue or enter no to quit.: ").strip())).lower() # Removes the leading and trailing spaces from the start and the end and lowers all characters. 
        
        if (choice == "no"):
            flag = False # If the user picks no, then the flag will become false, which will terminate the loop.

main() # Runs the main function to initiate the program. 
