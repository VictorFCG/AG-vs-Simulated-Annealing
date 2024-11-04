import starter_generator as sg
import genetic_alg as ga
from random import randint
import json

# cabeçalho, iniciar constantes
n_itens = 30  # Quantidade de itens do problema
w_max = 50  # peso máximo de um item
v_max = 50  # valor máximo de um item
# algoritmo genético
n_pop = 100  # tamanho da população
gen_limmit = 100  # limite de iterações/gerações
m_ratio = 0.01  # taxa de mutação
# tempera

def loop_ag(v_size, weight, value, c_max):
    list_at = []
    list_last = []
    list_at_i = []
    list_improv = []
    for i in range(v_size):
        all_time, all_time_i, lastgen_best, improv = ga.ga_search(n_itens, n_pop, gen_limmit, weight, value, c_max, m_ratio)
        list_at.append(all_time)
        list_last.append(lastgen_best)
        list_at_i.append(all_time_i)
        list_improv.append(improv)
        print(i)
    dados = {
    "list_at": list_at,
    "list_last": list_last,
    "list_at_i": list_at_i,
    "list_improv": list_improv
    }
    with open('mut_100perc.json', 'w') as f:
        json.dump(dados, f, indent=4)

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
    #loop_ag(100, weight, value, c_max)

if __name__ == "__main__":
    main()
