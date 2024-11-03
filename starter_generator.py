from random import randint


def random_choice(n_itens):  # gera uma escolha de itens/ um estado
    choice = []
    for i in range(n_itens):
        choice.append(randint(0, 1))
    return choice


def init(n_itens, w_max, v_max):
    weight = [
        22,
        31,
        15,
        1,
        34,
        10,
        2,
        3,
        16,
        14,
        20,
        49,
        41,
        36,
        38,
        37,
        50,
        40,
        17,
        19,
        48,
        6,
        5,
        45,
        9,
        23,
        39,
        8,
        46,
        13,
        21,
        7,
        43,
        11,
        18,
        26,
        33,
        25,
        30,
        44,
        47,
        32,
        28,
        4,
        12,
        42,
        35,
        29,
        27,
        24,
    ]
    value = [
        30,
        11,
        34,
        16,
        42,
        14,
        12,
        22,
        47,
        23,
        37,
        21,
        49,
        26,
        35,
        15,
        18,
        29,
        45,
        7,
        28,
        1,
        38,
        40,
        31,
        10,
        6,
        13,
        19,
        17,
        8,
        43,
        2,
        9,
        27,
        25,
        36,
        4,
        39,
        41,
        24,
        48,
        3,
        20,
        5,
        44,
        50,
        32,
        46,
        33,
    ]
    c_max = 600
    """weight = []
    value = []

    for i in range(n_itens):
        weight.append(randint(1, w_max))
        value.append(randint(1, v_max))
    c_max = randint(min(weight), sum(weight))"""

    return weight, value, c_max
