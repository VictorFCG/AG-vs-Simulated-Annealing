from random import randint

def random_choice(n_itens): #gera uma escolha de itens 
    choice = []
    for i in range(n_itens):
        choice.append(randint(0, 1))
    return choice

def init(n_itens, w_max, v_max):
    weight = []
    value = []

    for i in range(n_itens):
        weight.append(randint(1, w_max))
        value.append(randint(1, v_max))
    c_max = randint(min(weight), sum(weight))

    return weight, value, c_max
