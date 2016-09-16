from random import randint

# rolls chosen number of dices with chosen number of walls,
# then adds them up skipping lowest values


def rm_die(dice, die_num, to_deny):
    roll_list = [randint(1, dice) for x in range(die_num)]
    while to_deny > 0:
        mini = roll_list.index(min(roll_list))
        del(roll_list[mini])
        to_deny -= 1
    return sum(roll_list)


strength = rm_die(6, 4, 1)
print(strength)
