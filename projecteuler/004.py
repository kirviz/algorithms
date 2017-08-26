from math import ceil, floor


def is_polyndrome(num):
    """
    >>> is_polyndrome(121)
    True
    >>> is_polyndrome(123)
    False
    >>> is_polyndrome(2442)
    True
    >>> is_polyndrome(2424)
    False
    """
    digits = str(num)
    return digits == digits[::-1]
    # unnecesary complicated solution
    count = len(digits)
    left = digits[:floor(count/2)]
    right = digits[ceil(count/2):]
    return left == right[::-1]



def reverse_int(num):
    """
    >>> reverse_int(123)
    321
    >>> reverse_int(685030)
    30586
    """
    result = 0
    while num > 0:
        result = result * 10 + num % 10
        num //= 10
    return result


def is_polyndrome_int(num):
    """
    >>> is_polyndrome_int(1210)
    False
    """
    return num == reverse_int(num)


def max_polyndrome():
    result = 0
    for a in range(100, 1000):
        for b in range(a, 1000):
            c = a * b
            if c > result and is_polyndrome_int(c):
                result = c
    return result


def max_polyndrome2():
    """
    >>> max_polyndrome2()
    906609
    """

    result = 0
    for a in range(999, 99, -1):
        for b in range(999, a-1, -1):
            c = a * b
            if c > result and is_polyndrome_int(c):
                result = c
                break
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # print(max_polyndrome2())