# Number Theory Programs

## Overview

This repository contains five programs that demonstrate fundamental programming concepts while exploring interesting mathematical properties:
- Finding all divisors of a number
- Identifying prime numbers
- Discovering narcissistic (Armstrong) numbers
- Triangle inequality theorem validation
- Interactive range-based number analysis

## Programs

### 1. Divisor Finder (`divisor.py`)

Finds all divisors of a given number.

**Concept:** A divisor is a number that divides evenly into another number with no remainder.

**Usage:**
```bash
python divisor.py
```

**Example:**
```
Please enter a number to find all of it's divisors: 12
The divisors of 12: [1, 2, 3, 4, 6, 12]
```

**How it works:**
- Takes a number as input
- Iterates through all numbers from 1 to the input
- Checks if each number divides evenly (remainder = 0)
- Returns a list of all divisors

---

### 2. Simple Divisor Finder (`part1Q2.py`)

A streamlined version of the divisor finder without function encapsulation.

**Usage:**
```bash
python part1Q2.py
```

**Example:**
```
Please enter a number to find all of it's divisors: 20
[1, 2, 4, 5, 10, 20]
```

---

### 3. Prime Number Checker (`primeNumbers.py`)

Randomly generates a number between 1 and 30 and determines if it's prime.

**Concept:** A prime number is a natural number greater than 1 that has exactly two divisors: 1 and itself.

**Usage:**
```bash
python primeNumbers.py
```

**Example Output:**
```
The generated number: 17
17 is a prime number.
```

```
The generated number: 24
24 is not a prime number.
```

**Algorithm:**
1. Generate random number (1-30)
2. Find all divisors using `findDivisor()` function
3. Check conditions:
   - If number < 2: not prime
   - If exactly 2 divisors: prime
   - Otherwise: not prime

---

### 4. Narcissistic Number Finder (`narcissisticNumbers.py`)

Finds all narcissistic (Armstrong) numbers within a user-specified range.

**Concept:** A narcissistic number is a number that equals the sum of its digits each raised to the power of the number of digits. For 3-digit numbers: abc = a³ + b³ + c³

**Examples of Narcissistic Numbers:**
- 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153 ✓
- 370 = 3³ + 7³ + 0³ = 27 + 343 + 0 = 370 ✓
- 371 = 3³ + 7³ + 1³ = 27 + 343 + 1 = 371 ✓
- 407 = 4³ + 0³ + 7³ = 64 + 0 + 343 = 407 ✓

**Usage:**
```bash
python narcissisticNumbers.py
```

**Example Session:**
```
Please enter the 1st number between 100 and 999: 150
Please enter the 2nd number between 100 and 999: 400
Narcissistic numbers between 150 and 400 are: [153, 370, 371]
Total Narcissistic numbers found: 3
Do you want to check another range? Enter yes to continue or enter no to quit.: yes

Please enter the 1st number between 100 and 999: 200
Please enter the 2nd number between 100 and 999: 300
No Narcissistic numbers found between 200 and 300.
Do you want to check another range? Enter yes to continue or enter no to quit.: no
```

**Features:**
- Input validation for 3-digit numbers
- Ensures first number is less than second number
- Interactive loop for multiple range checks
- Detailed output with count of numbers found

**Functions:**
- `numValid()` - Validates user input (3-digit numbers, proper ordering)
- `numNarc(num)` - Checks if a single number is narcissistic
- `narcRange(num1, num2)` - Finds all narcissistic numbers in range
- `main()` - Orchestrates the program flow

---

### 5. Triangle Validator (`part1Q1.py`)

Determines if three given side lengths can form a valid triangle using the triangle inequality theorem.

**Concept:** The triangle inequality theorem states that the sum of any two sides of a triangle must be greater than the third side.

**Mathematical Rule:**
For sides a, b, c to form a triangle:
- a + b > c
- b + c > a
- c + a > b

**Usage:**
```bash
python part1Q1.py
```

**Example - Valid Triangle:**
```
Please enter the length of side 1: 3
Please enter the length of side 2: 4
Please enter the length of side 3: 5
These side lengths can form a triangle.
```

**Example - Invalid Triangle:**
```
Please enter the length of side 1: 1
Please enter the length of side 2: 2
Please enter the length of side 3: 10
These side lengths can't form a triangle.
```

---

## Requirements

- Python 3.x
- No external libraries required (uses only standard library)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/number-theory-programs.git
cd number-theory-programs
```

2. Run any program:
```bash
python divisor.py
python primeNumbers.py
python narcissisticNumbers.py
python part1Q1.py
python part1Q2.py
```

## Mathematical Concepts Covered

### Divisibility
A number `a` is divisible by `b` if `a % b == 0`

### Prime Numbers
- Must be greater than 1
- Has exactly two divisors (1 and itself)
- Examples: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29...

### Narcissistic Numbers (3-digit)
- Also called Armstrong numbers or pluperfect digital invariants
- For 3-digit number xyz: xyz = x³ + y³ + z³
- Only four exist for 3-digit numbers: 153, 370, 371, 407

### Triangle Inequality Theorem
- Fundamental geometric principle
- Prevents impossible triangles (e.g., sides 1, 2, 100)
- Ensures the shortest distance between two points is a straight line

## Code Quality Features

- ✅ Comprehensive input validation
- ✅ Clear function documentation
- ✅ Meaningful variable names
- ✅ Modular design with reusable functions
- ✅ User-friendly error messages
- ✅ Interactive loops for repeated operations
- ✅ Efficient algorithms

## Learning Objectives

This assignment demonstrates:

- **Mathematical algorithms** - Divisor finding, prime detection, digit extraction
- **Input validation** - Range checking, type validation, logical constraints
- **Loop constructs** - For loops, while loops, flag-based control
- **List operations** - Appending, length checking, iteration
- **Function design** - Parameters, return values, single responsibility
- **Conditional logic** - Complex boolean expressions
- **String manipulation** - strip(), lower(), digit extraction
- **Modular programming** - Breaking problems into smaller functions
- **Random number generation** - Using the random module

## Algorithm Complexity

| Program | Time Complexity | Space Complexity |
|---------|----------------|------------------|
| Divisor Finder | O(n) | O(d) where d = number of divisors |
| Prime Checker | O(n) | O(d) |
| Narcissistic Finder | O(n) for range | O(k) where k = count found |
| Triangle Validator | O(1) | O(1) |

## Project Structure

```
.
├── divisor.py                    # Function-based divisor finder
├── part1Q2.py                    # Simple divisor finder
├── primeNumbers.py               # Random prime number checker
├── narcissisticNumbers.py        # Interactive narcissistic number finder
├── part1Q1.py                    # Triangle inequality validator
└── README.md                     # This file
```

## Interesting Facts

**Narcissistic Numbers:**
- There are only 88 narcissistic numbers in base 10
- The largest is 115,132,219,018,763,992,565,095,597,973,971,522,401 (39 digits!)
- For 3-digit numbers, only 4 exist: 153, 370, 371, 407

**Prime Numbers:**
- There are infinitely many prime numbers (proven by Euclid ~300 BCE)
- The largest known prime (as of 2024) has over 24 million digits
- Prime numbers are fundamental to modern cryptography

## Contributing

This is an academic project, but suggestions for improvements are welcome! Feel free to fork and experiment.

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Carleton University Computer Science Department
- COMP 1005/1405 course instructors and TAs
- Python documentation and mathematical resources
