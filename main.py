import starter_generator as sg
import genetic_alg as ga
from random import randint

# cabeçalho, iniciar constantes
n_itens = 15  # Quantidade de itens do problema
w_max = 100  # peso máximo de um item
v_max = 100  # valor máximo de um item
# algoritmo genético
n_pop = 100  # tamanho da população
gen_limmit = 100  # limite de iterações/gerações
m_ratio = 0.01  # taxa de mutação
# tempera


def show_inst(weight, value, c_max):  # dados sobre uma instância do problema
    print("Lista de pesos:\n", weight)
    print("Lista de valores:\n", value)
    print("Menor peso:", min(weight))
    print("Soma dos pesos:", sum(weight))
    print("Capacidade da mochila:", c_max)


def main():
    weight, value, c_max = sg.init(
        n_itens, w_max, v_max
    )  # inicia itens aleatórios e uma capacidade para a mochila
    show_inst(weight, value, c_max)
    ga.ga_search(n_itens, n_pop, gen_limmit, weight, value, c_max, m_ratio)


if __name__ == "__main__":
    main()
