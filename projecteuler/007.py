from math import sqrt


_primes = [2, 3]


def prime(n):
    if n < 0:
        return 1

    while len(_primes) <= n:
        p = _primes[-1]
        p += 2
        while not is_prime(p):
            p += 2
        _primes.append(p)

    return _primes[n]


def is_prime(num):
    for divisor in _primes:
        if num % divisor == 0:
            return False
    return True


# print(prime(10000)) # 104743


def fast_is_prime(n):
    """
    >>> fast_is_prime(1)
    False
    >>> fast_is_prime(2)
    True
    >>> fast_is_prime(3)
    True
    >>> fast_is_prime(4)
    False
    >>> fast_is_prime(5)
    True
    >>> fast_is_prime(6)
    False
    >>> fast_is_prime(7)
    True
    >>> fast_is_prime(8)
    False
    >>> fast_is_prime(9)
    False
    >>> fast_is_prime(10)
    False
    >>> fast_is_prime(11)
    True
    >>> fast_is_prime(12)
    False
    >>> fast_is_prime(13)
    True
    >>> fast_is_prime(17)
    True
    >>> fast_is_prime(19)
    True
    """
    if n == 1:return False
    if n == 2: return True
    if n % 2 == 0: return False
    if n < 8: return True
    if n % 3 == 0: return False

    # n is a prime if there is no divisor smaller than sqrt(n)
    limit = int(sqrt(n))

    # any prime higher than 3 can be written as f = 6*k +/- 1
    f = 5

    while f < limit:
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f += 6

    return True


def fast_prime(n):
    """
    >>> fast_prime(1)
    2
    >>> fast_prime(2)
    3
    >>> fast_prime(3)
    5
    >>> fast_prime(4)
    7
    >>> fast_prime(5)
    11
    >>> fast_prime(6)
    13
    >>> fast_prime(7)
    17
    """
    if n == 1: return 2
    count = 1
    candidate = 1

    while count < n:
        candidate += 2
        if fast_is_prime(candidate):
            count += 1

    return candidate

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print(fast_prime(10001))