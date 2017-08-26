# bruteforce
arr = list(range(1, 101))
sum_of_squares = sum([a*a for a in arr])
square_of_sums = sum(arr)*sum(arr)
diff = square_of_sums - sum_of_squares
print(sum_of_squares, square_of_sums, diff)

# math
n = 100
sumn = int((1+n)*n/2)
sq_sum = sumn*sumn
# f(n) = 1/3*n^3 + 1/2*n^2 + 1/6*n
sum_sq = int(1/3*n*n*n + 1/2*n*n + 1/6*n)

print(sum_sq, sq_sum, sq_sum - sum_sq)