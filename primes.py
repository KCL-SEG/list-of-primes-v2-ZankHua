"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 0:
        raise ValueError("number_of_primes must be a positive integer")
    
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def primes(number_of_primes):
    """Return a list of prime numbers of length number_of_primes."""
    
    list_of_primes = []
    num = 2  # Starting from the first prime number
    while len(list_of_primes) < number_of_primes:
        if is_prime(num):
            list_of_primes.append(num)
        num += 1
    return list_of_primes





