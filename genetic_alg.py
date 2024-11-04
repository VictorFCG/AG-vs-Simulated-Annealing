import starter_generator as sg
from random import randint
from random import random


def print_pop(population, n_pop):
    for i in range(n_pop):
        print(population[i])
    print("\n")


def repr(p1, p2, n_itens, m_ratio):
    son = []
    mid = int(n_itens / 2)
    # crossover
    for i in range(mid):
        son.append(p1[i])
    for i in range(mid, n_itens):
        son.append(p2[i])

    # mutação
    if (random() < m_ratio):
        position = randint(0, (n_itens - 1))
        if son[position] == 1:
            son[position] = 0
        else:
            son[position] = 1

    return son


def pick_parent(population, sum_eval, n_pop, n_itens):
    aux_rand = randint(0, sum_eval)
    aux_sum = 0
    for i in range(n_pop):
        aux_sum += population[i][n_itens + 2]  # posição do coeficiente
        if aux_rand <= aux_sum:
            return population.pop(i)
    return population.pop()


def new_gen(population, n_pop, sum_eval, n_itens, m_ratio):
    borutos = []
    for i in range(n_pop):
        p1 = pick_parent(
            population, sum_eval, n_pop, n_itens
        )  # remove temporariamente indivíduo
        p2 = pick_parent(population, (sum_eval - p1[n_itens + 2]), (n_pop - 1), n_itens)
        population.append(p1)  # readicionando os indivíduos na população
        population.append(p2)

        borutos.append(repr(p1, p2, n_itens, m_ratio))

    return borutos


def pick_best(population, n_itens):
    best_eval = population[0][n_itens + 2]
    best = population[0]
    for i in population:
        if i[n_itens + 2] > best_eval:
            best_eval = i[n_itens + 2]
            best = i
    return best


def evaluate(c_max, population, n_itens):
    w_position = n_itens
    v_position = n_itens + 1
    sum_eval = 0
    for i in population:
        eval = i[v_position]
        if (i[w_position] - c_max) > 0:
            #se muito pesado penalizar
            eval = int(eval * 0.1)
        sum_eval += eval
        i.append(eval)
    return sum_eval


def set_value(population, value, n_itens):
    for i in population:
        v = 0
        for j in range(n_itens):
            v += i[j] * value[j]
        i.append(v)


def set_weight(population, weight, n_itens):
    for i in population:
        w = 0
        for j in range(n_itens):
            w += i[j] * weight[j]
        i.append(w)


def init_pop(n_itens, n_pop):
    population = []

    for i in range(n_pop):
        choice = sg.random_choice(n_itens)
        population.append(choice)
    return population


def ga_search(n_itens, n_pop, gen_limmit, weight, value, c_max, m_ratio):
    population = init_pop(n_itens, n_pop)
    set_weight(population, weight, n_itens)
    set_value(population, value, n_itens)
    sum_eval = evaluate(c_max, population, n_itens)
    gen_best = pick_best(population, n_itens)
    all_time_i = 0 #geração do melhor da história
    all_time = gen_best #melhor conhecido durante ahistória
    improv = 0 #numero de melhorias

    for i in range(gen_limmit):

        population = new_gen(population, n_pop, sum_eval, n_itens, m_ratio)
        set_weight(population, weight, n_itens)
        set_value(population, value, n_itens)
        sum_eval = evaluate(c_max, population, n_itens)
        gen_best = pick_best(population, n_itens)
        if gen_best[n_itens + 2] > all_time[n_itens + 2]:
            all_time_i = i + 1
            all_time = gen_best
            improv += 1
    lastgen_best = pick_best(population, n_itens)
    return all_time[n_itens + 2], all_time_i, lastgen_best[n_itens + 2], improv

    # print_pop(population, n_pop)
    # print("Melhor: ")
    # print(current_best)
