from math import sqrt


def fast_is_prime(n):
    if n == 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    if n < 8: return True
    if n % 3 == 0: return False

    # n is a prime if there is no divisor smaller than sqrt(n)
    limit = int(sqrt(n)) + 1

    # any prime higher than 3 can be written as f = 6*k +/- 1
    f = 5

    while f < limit:
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f += 6

    return True


def sum_primes_below(n):
    """
    >>> sum_primes_below(3)
    2
    >>> sum_primes_below(4)
    5
    >>> sum_primes_below(5)
    5
    >>> sum_primes_below(6)
    10
    >>> sum_primes_below(7)
    10
    >>> sum_primes_below(8)
    17
    >>> sum_primes_below(9)
    17
    >>> sum_primes_below(10)
    17
    >>> sum_primes_below(11)
    17
    >>> sum_primes_below(12)
    28
    """
    result = 2
    candidate = 3

    while candidate < n:
        if fast_is_prime(candidate):
            result += candidate
        candidate += 2

    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(sum_primes_below(2_000_000))

    # someone else's sieve of Eratosthenes
    marked = [0] * 2000000
    value = 3
    s = 2
    while value < 2000000:
        if marked[value] == 0:
            s += value
            i = value
            while i < 2000000:
                marked[i] = 1
                i += value
        value += 2
    print(s)

# 142913828922
