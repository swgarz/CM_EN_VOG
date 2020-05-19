# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:49:18 2020

@author: Elena y Daniel
"""
import mlrose
import numpy as np
import itertools


def aptitud(ls_basicas):
    suma = 0
    for i in range(len(ls_basicas)-1):
        if ls_basicas[i][0] == ls_basicas[i+1][0] or ls_basicas[i][1] == ls_basicas[i+1][1]:
            suma += 1
    return suma


def aptitud2(poA, poB):
    if poA[0] == poB[0] or poA[1] == poB[1]:
        return 2
    else:
        return 1

#orden = list(com)

def encuentra_circuito2(orden, ls_basicas):

    #n_bas = [i for i in range(len(ls_basicas))]
    #orden = orden + [len(ls_basicas)-1]
        
    orden_aux = [i for i in range(len(orden))]
    # [0, 1, 2, 5]
    # [0, 1, 2, 3] 
    dist_list = []
    for i in orden_aux:
        for j in orden_aux:
            if i != j:
                costo = aptitud2(ls_basicas[orden[i]], ls_basicas[orden[j]])
                #print(ls_basicas[orden[i]], ls_basicas[orden[j]], costo)
                dist_list.append((i, j, costo))
    
# =============================================================================
#     comb = itertools.combinations(orden, 2)
#     print(i)
#     dist_list = []
#     for i in comb:
#         print(i)
#         costo = aptitud2(ls_basicas[i[0]], ls_basicas[i[1]])
#         dist_list.append((i[0], i[1], costo))
# =============================================================================
        #print(ls_basicas[i[0]], ls_basicas[i[1]], costo)
    
    # Initialize fitness function object using dist_list
    fitness_dists = mlrose.TravellingSales(distances = dist_list)
    problem_fit = mlrose.TSPOpt(length = len(orden), fitness_fn = fitness_dists, maximize=True)
    best_state, best_fitness = mlrose.genetic_alg(problem_fit, random_state = 2)
    
    
    resul = []
    for i in best_state:
        resul.append(orden[i])
    

    ini = resul.index(len(ls_basicas)-1)
    resul = resul[ini:] + resul[0:ini]
    result = resul + [resul[0]]
    sum_total = 0
    for i in range(len(result)-1):
        #print(i, ls_basicas[result[i]], ls_basicas[result[i+1]])
        costo = aptitud2(ls_basicas[result[i]], ls_basicas[result[i+1]])
        if costo == 1:
            #print('Entro')
            best_fitness += .5
            return resul, best_fitness/2
            break
# =============================================================================
        #print(ls_basicas[result[i]], ls_basicas[result[i+1]], sum_total)
    #max_attempts = 1000
    
    #print(best_state)
    #print(best_fitness)
    
# =============================================================================
#     for i in best_state:
#         print(ls_basicas[i])
# =============================================================================
    return resul, best_fitness/2

  
def encuentra_circuito(ls_basicas):

    n_bas = [i for i in range(len(ls_basicas))]
    comb = itertools.combinations(n_bas, 2)
    
    dist_list = []
    for i in comb:
        costo = aptitud2(ls_basicas[i[0]], ls_basicas[i[1]])
        dist_list.append((i[0], i[1], costo))
        #print(ls_basicas[i[0]], ls_basicas[i[1]], costo)
    
    # Initialize fitness function object using dist_list
    fitness_dists = mlrose.TravellingSales(distances = dist_list)
    problem_fit = mlrose.TSPOpt(length = len(ls_basicas), fitness_fn = fitness_dists, maximize=True)
    best_state, best_fitness = mlrose.genetic_alg(problem_fit, random_state = 2)
    #print(best_state)
    #print(best_fitness)
    
# =============================================================================
#     for i in best_state:
#         print(ls_basicas[i])
# =============================================================================
    return list(best_state), best_fitness/2
