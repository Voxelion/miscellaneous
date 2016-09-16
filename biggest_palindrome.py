from time import time

list999 = [x for x in range(999, 100, -1)]


def is_palindrome(i):
    num = list(str(i))
    length = int(len(str(i)))
    if length == 0 or length == 1:
        return True
    elif length > 1:
        for z in range(length):
            if num[z] == num[length - z - 1]:
                pass
            else:
                return False
        return True


def tbig_mult(nums):
    actual = 0
    frst = 0
    sec = 0
    for x in nums:
        print(x)
        for y in nums:
            if is_palindrome(x * y) == True and x * y > actual:
                actual = x * y
                frst = x
                sec = y
    return actual, frst, sec


start = time()
biggest_palindrome, first, second = tbig_mult(list999)
end = time()

print(biggest_palindrome, first, second, end - start)
