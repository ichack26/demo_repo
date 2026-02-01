def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_perfect_square(n):
    """Check if a number is a perfect square."""
    root = int(n**0.5)
    return root * root == n

def find_primes(limit, multiplier, constant):
    result = []
    for p in range(2, limit):
        if is_prime(p):
            value = multiplier * p + constant
            if is_perfect_square(value):
                result.append(p)
    return result

def main():
    """Find all primes under 1000 such that 17p + 625 is a square number."""
    limit = 1000
    multiplier = 17
    constant = 625  
    primes = find_primes(limit, multiplier, constant)
    for p in primes:
        print(f"{p} works")

if __name__ == "__main__":
    main()
