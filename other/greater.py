def calculate(arr):
    result = []
    for i, num in enumerate(arr):
        greater = larger(num, arr[i+1:])
        result.append(greater if greater is not None else -1)

    print(' '.join(map(str, result)))


def larger(than, inArray):
    for n in inArray:
        if n > than:
            return n

if __name__ == "__main__":
    calculate([1, 3, 2, 4])
