from math import sqrt

s = 1000


def get_b(a):
    return (s*a - s*s/2) / (a - s)


def get_c(a):
    b = get_b(a)
    return sqrt(a*a + b*b)


# def c(a):
#     return 1000 - a - ((1000*a -500000) / (a - 1000))


def abc():
    for a in range(1, s):
        b = get_b(a)
        c = get_c(a)
        if int(b) == b and int(c) == c:
            print(a, int(b), int(c), int(a*b*c))

        if a >= b:
            break

abc()

# (200, 375, 425, 31875000)

# the overview is very different and is needed to understand for other pythagorean triplets like problem 75
