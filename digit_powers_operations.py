
# takes number to power of itself and then adds it digits
# aka
# num^num = 100x10y1z then returns x + y + z


def d_adder(num):
    p_num = num ** num
    digits = list(str(p_num))
    summ = 0
    x = 0
    while x in range(len(str(p_num))):
        summ += int(digits[x])
        x += 1
    return summ


print(d_adder(11))
