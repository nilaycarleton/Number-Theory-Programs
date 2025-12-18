# Part 1 - Question 1

side1 = int(input("Please enter the length of side 1: ").strip())
side2 = int(input("Please enter the length of side 2: ").strip())
side3 = int(input("Please enter the length of side 3: ").strip())

if ((side1 + side2 > side3) and (side2 + side3 > side1) and (side3 + side1 > side2)):
    print("These side lengths can form a trinangle.")
else:
    print("These side lenghts can't form a triangle.")