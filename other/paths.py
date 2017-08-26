# https://www.careercup.com/question?id=5736911233613824
# Starting from num = 0, add 2^i (where i can be any non-negative integer) to num until num == N. Print all paths of how num turns from 0 to N.
# For example if N = 4,
# Paths printed are [0,1,2,3,4], [0,1,2,4], [0,1,3,4], [0,2,4], [0,2,3,4], [0,4].
# [0,2,4] is made from 0 + 2^1 + 2^1. [0,1,3,4] from 0 + 2^0 + 2^1 + 2^0


# def sum_paths(N):
#     def aux(path, sum, j):
#         if sum == N:
#             res.append(path)
#         if sum < N:
#             for i in range(j, int.bit_length(N)):
#                 aux(path + [sum + (1 << i)], sum + (1 << i), i)
#     res = []
#     aux([0], 0, 0)
#     return res
#
# print(sum_paths(4))

# [[0, 1, 2, 3, 4], [0, 1, 2, 4], [0, 2, 4], [0, 4]]
# missing [0, 1, 3, 4] and [0, 2, 3, 4]


def sum_paths(N):
    def aux(path, sum):
        if sum == N:
            res.append(path)
        if sum < N:
            for i in range(int.bit_length(N)):
                aux(path + [sum + (1 << i)], sum + (1 << i))
    res = []
    aux([0], 0)
    return res

if __name__ == "__main__":
    print(sum_paths(4))

# [[0, 1, 2, 3, 4], [0, 1, 2, 4], [0, 1, 3, 4], [0, 2, 3, 4], [0, 2, 4], [0, 4]]