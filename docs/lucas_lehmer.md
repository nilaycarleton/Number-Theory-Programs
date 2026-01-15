# Lucas-Lehmer Test for Mersenne Primes

## History
The Lucas–Lehmer test (LLT) is a primality test for Mersenne numbers. The test was originally developed by Édouard Lucas in 1878 and subsequently improved by Derrick Henry Lehmer in the 1930s.

## Mathematical Derivation
The test is based on the Lucas-Lehmer sequence, defined recursively as:

s_0 = 4,
s_n = (s_{n-1}^2 - 2) mod (2^p - 1).

Then, 2^p - 1 is prime if and only if s_{p-2} = 0.

## Algorithm
1. Compute M = 2^p - 1.
2. Set s = 4.
3. Repeat p-2 times: s = (s^2 - 2) mod M.
4. If s == 0, then M is prime.

## Significance
This test is the most efficient known method for testing the primality of Mersenne numbers and is used by the Great Internet Mersenne Prime Search (GIMPS) to discover record-breaking primes.

## References
- Lucas, É. (1878). Théorie des fonctions numériques simplement périodiques.
- Lehmer, D. H. (1935). On Lucas's Test for the Primality of Mersenne's Numbers.