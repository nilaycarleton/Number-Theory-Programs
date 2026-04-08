def lucas_lehmer(p):
    """
    Lucas-Lehmer primality test for Mersenne numbers.
    Args:
        p (int): prime number to test, where Mersenne number is 2^p - 1.
    Returns:
        bool: True if 2^p - 1 is prime (a Mersenne prime), False otherwise.
    """
    if p == 2:
        return True
    m = (1 << p) - 1  # 2^p - 1
    s = 4
    for _ in range(p - 2):
        s = (s * s - 2) % m
    return s == 0

if __name__ == "__main__":
    # Demonstration: test small Mersenne primes
    mersenne_primes = [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127]
    for p in mersenne_primes:
        result = lucas_lehmer(p)
        print(f"2^{p} - 1 is prime: {result}")