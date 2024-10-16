from random import randint


def init(N, w_max, v_max):
    weight = []
    value = []

    for i in range(N):
        weight.append(randint(1, w_max))
        value.append(randint(1, v_max))
    c_max = randint(min(weight), sum(weight))

    return weight, value, c_max
