# single fibonacci number
def fibb(n):
    actual = 0
    if n == 0 or n == 1:
        actual += 1
    else:
        actual = fibb(n - 1) + fibb(n - 2)
    return actual


# list of fibonacci numbers under n value
def fibb_list(n):
    i, j = 1, 1
    while i < n:
        yield i
        i, j = j, i+j


fibbs = list(fibb_list(4000000))


fibb_sum = 0
for m in fibbs:
    if m % 2 == 0:
        fibb_sum += m

print(fibb_sum)
# fibb_sum should be 4613732
