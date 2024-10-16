from init_knap import init
from random import randint

# cabeçalho, iniciar constantes
n_itens = 15
w_max = 100
v_max = 100


def random_choice():
    choice = []
    for i in range(n_itens):
        choice.append(randint(0, 1))
    return choice


def show_inst(weight, value, c_max):
    print(weight)
    print(value)
    print(min(weight))
    print(sum(weight))
    print(c_max)


def main():
    weight, value, c_max = init(n_itens, w_max, v_max)
    show_inst(weight, value, c_max)


if __name__ == "__main__":
    main()
