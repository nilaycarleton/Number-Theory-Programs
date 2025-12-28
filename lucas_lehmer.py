"""
Lucas–Lehmer test for Mersenne primes.

This module provides a function to determine whether a number of the form
M_p = 2^p - 1 (a Mersenne number) is prime. The Lucas–Lehmer test is a
deterministic primality test for Mersenne numbers, famously used to discover
the largest known primes.

Author: A French mathematician and theologian
"""

def lucas_lehmer(p: int) -> bool:
    """
    Determine whether 2^p - 1 is a Mersenne prime using the Lucas–Lehmer test.

    Parameters
    ----------
    p : int
        Exponent; the Mersenne number to test is M_p = 2^p - 1.

    Returns
    -------
    bool
        True if M_p is prime, False otherwise.

    Notes
    -----
    The test is defined for integer p > 1. For p = 2, M_2 = 3, which is prime.
    If p is composite, M_p is also composite (except for p = 2), but the test
    will correctly return False.

    The algorithm follows the classic Lucas–Lehmer iteration:
        s_0 = 4
        s_{i+1} = (s_i^2 - 2) mod M_p
    After p-2 iterations, M_p is prime iff s_{p-2} == 0.

    Examples
    --------
    >>> lucas_lehmer(3)
    True   # M_3 = 7 is prime
    >>> lucas_lehmer(4)
    False  # M_4 = 15 is composite
    >>> lucas_lehmer(13)
    True   # M_13 = 8191 is prime
    """
    if p < 2:
        return False
    if p == 2:
        return True  # M_2 = 3 is prime
    m = (1 << p) - 1  # 2**p - 1 computed efficiently
    s = 4
    for _ in range(p - 2):
        s = (s * s - 2) % m
    return s == 0


def is_mersenne_prime(p: int) -> bool:
    """
    Alias for lucas_lehmer(p). Added for clarity.
    """
    return lucas_lehmer(p)


if __name__ == "__main__":
    # Demonstrate the function with known Mersenne primes.
    mersenne_exponents = [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127]
    print("Testing known Mersenne primes (up to p = 127):")
    for p in mersenne_exponents:
        if lucas_lehmer(p):
            print(f"M_{p} = 2^{p} - 1 is prime")
        else:
            print(f"M_{p} = 2^{p} - 1 is composite (should not happen)")
    # A few composite exponents
    composite_exponents = [4, 6, 8, 9, 10, 11]
    print("\nTesting some composite exponents:")
    for p in composite_exponents:
        if not lucas_lehmer(p):
            print(f"M_{p} = 2^{p} - 1 is composite (as expected)")
        else:
            print(f"M_{p} = 2^{p} - 1 is prime (unexpected!)")