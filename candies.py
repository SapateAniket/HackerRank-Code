n = input()
a = [input() for _ in xrange(n)]
candies = [1] * n

for i in xrange(1, n):
    if a[i] > a[i-1]:
        candies[i] = candies[i-1] + 

for i in xrange(n-2, -1, -1):
    if a[i] > a[i+1]:
        candies[i] = max(candies[i], candies[i+1] + 1)

print sum(candies)