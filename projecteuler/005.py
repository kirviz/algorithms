if __name__ == "__main__":
    print(20*19*9*17*4*7*13*11)

from math import log, floor

def p(n):
    """calculates the n-th prime number
    >>> p(0)
    2
    >>> p(1)
    3
    >>> p(2)
    5
    >>> p(3)
    7
    >>> p(4)
    11
    >>> p(5)
    13
    """
    if n < 0:
        return 1

    def is_prime(num):
        for value in _primes:
            if num % value == 0:
                return False
        return True

    while n >= len(_primes):
        counter = _primes[-1] + 2
        while not is_prime(counter):
            counter += 2
        _primes.append(counter)

    return _primes[n]
_primes = [2, 3]


def a(n, k):
    """calculates maximum power of p(n) needed
    >>> a(0, 20)
    4
    >>> a(1, 20)
    2
    >>> a(2, 20)
    1
    """
    return floor(log(k) / log(p(n)))


def smallest_divisible_up_to(n):
    result = 1
    for i in range(n-1):
        result *= p(i) ** a(i, n)
    return result


def smarter_smallest_divisible_up_to(n):
    result = 1
    i = 0
    need_log = True
    while p(i) < n:
        need_log = need_log and (p(i) * p(i) < n)
        ai = a(i, n) if need_log else 1
        result *= p(i) ** ai
        i += 1
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print(smarter_smallest_divisible_up_to(20))