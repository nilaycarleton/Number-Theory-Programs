# Part 1 - Question 2

num = int(input("Please enter a number to find all of it's divisors: ").strip())

divisors = []
for x in range(1, num + 1):
    if (num % x  == 0):
        divisors.append(x)
print(divisors)