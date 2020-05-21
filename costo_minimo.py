# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:49:18 2020

@author: Elena y Daniel
"""

import pandas as pd
import numpy as np
import math
import encuentra_circuitos as f_g
import itertools
 

def isextremo(matriz, ren, col):
    up, x_up, y_up = arriba(ren, col, matriz)
    down, x_down, y_down = abajo(ren, col, matriz)
    right, x_right, y_right = derecha(ren, col, matriz)
    left, x_left, y_left = izquierda(ren, col, matriz)

    if down and right:
        return True
    elif left and down:
        return True
    elif up and right:
        return True
    elif up and left:
        return True
    else:
        return False
    
    
def arriba(x, y, matriz):
    bandera = False
    ren = x - 1
    while ren >= 0:
        if not math.isnan(matriz[ren][y]):
            #print(matriz[ren][y])
            bandera = True
            return True, ren, y
        ren -= 1
    
# =============================================================================
#     for ren in range(0, x):
#         if matriz[ren][y] !=0:
#             bandera = True
#             return True, ren, y
# =============================================================================
    return bandera , -1, -1
    

def abajo(x, y, matriz):
    bandera = False
    n_ren = matriz.shape[0]
    for ren in range(x+1, n_ren):
        if not math.isnan(matriz[ren][y]):
            #print(matriz[ren][y])
            bandera = True
            return bandera, ren, y
    return bandera , -1, -1


def derecha(x, y, matriz):
    bandera = False
    n_col = matriz.shape[1]
    for col in range(y+1, n_col):
        if not math.isnan(matriz[x][col]):
            bandera = True
            return True, x, col
    return bandera , -1, -1


def izquierda(x, y, matriz):
    bandera = False
    col = y - 1
    while col>=0:
        if not math.isnan(matriz[x][col]):
            bandera = True
            
            return True, x, col
        col -= 1
        
# =============================================================================
#     for col in range(0, y):
#         if matriz[x][col] != 0:
#             bandera = True
#             return True, x, col
# =============================================================================
    return bandera , -1, -1


if __name__ == '__main__':

   
    costo_min = pd.read_csv('vogel.csv') #importar Datos
    costo_min.dropna(inplace=True) #elimina valores nulos
    costo_min = costo_min.set_index('fuentes') #establece el indice de los datos
    costo_min_sol = costo_min.copy() #crea un nuevo objeto compuesto
    for i in range(costo_min.shape[0]-1): #devuelve la dimension de las tuplas
        for j in range(len(costo_min.columns)-1): #devuelve la dimension de las columnas
            costo_min_sol.iloc[i, j] = 0 # selecciona i,j

    bandera = True
    fun_obj = 0
    while bandera:
        minimos = costo_min.iloc[:-1, :-1].idxmin(axis=1) # Encuentra el indice del costo minimo por columna
        if minimos.shape[0] == 0: #Si no hay minimos proceso terminado
            bandera = False
            print('Proceso terminado')
            break
            

        minimo = costo_min.loc[costo_min.index[0], minimos[0]] # Obtiene el minimo del primer renglon
        count = 0
        renglon = 0
        columna = minimos[0] # Obtiene la columna del minimo del primer renglon
        for i in  range(1, costo_min.shape[0]-1):# Recorrera todas las columnas con costos a partir del renglon 1
            #print(i)
            aux = costo_min.loc[costo_min.index[i], minimos[i]] # Obtiene el minimo del renglon
            if aux < minimo: #Compara el minimo de todos los renglones contra el minimo del renglon 0
                #Se guarda el renglon y columna del valor minimo
                renglon = i
                columna = minimos[i]
                minimo = aux
        # hasta aqui se ha encontrado el mínimo de la matriz
        
        #Obtiene la demanda y oferta del costo minimo
        oferta = costo_min.iloc[renglon, -1]
        demanda = costo_min.loc[costo_min.index[-1], columna]
        # Se hace asigna la maxima cantidad  dependiendo las restricciones de la oferta y demanda
        if demanda != 0 and oferta != 0:
            if oferta > demanda:
                #print('Ofer > demanda')
                #print(str(costo_min.loc[costo_min.index[renglon], columna]),' * ', str(demanda))
                fun_obj += (costo_min.loc[costo_min.index[renglon], columna] * demanda) # multiplica la oferta por el costo
                costo_min_sol.loc[costo_min.index[renglon], columna] = demanda #se cumple la demanda del costo minimo
                costo_min.loc[costo_min.index[-1], columna] = 0 # deja en cero los demas espacios de la columna
                costo_min.iloc[renglon, -1] = costo_min.iloc[renglon, -1] - demanda # Se le quita la oferta a la demanda
                costo_min.drop(columna, inplace=True, axis=1) #Se elimina la columna
            else:
                #print('Ofer < demanda')
                fun_obj += (costo_min.loc[costo_min.index[renglon], columna] * oferta) # multiplica la demanda por el costo
                costo_min_sol.loc[costo_min.index[renglon], columna] = oferta # se da la oferta al costo
                costo_min.iloc[renglon, -1] = 0 # deja los demas espacios del renglon en blanco
                costo_min.loc[costo_min.index[-1], columna] = costo_min.loc[costo_min.index[-1], columna] - oferta # Se le quita la demanda a la oferta
                costo_min.drop(costo_min.index[renglon], inplace=True, axis=0) #Se elimina el renglon
            if minimos.shape[0] == 0:
                bandera = False
                break
                print('Proceso terminado')
        else:
            # Si la oferta o la demanda son 0  se elimina de la tabla
            if demanda == 0:
                costo_min.drop(columna, inplace=True, axis=1)
            else:
                costo_min.drop(costo_min.index[renglon], inplace=True, axis=0)

    print('******************************')
    print('Funcion Objetivo: ', fun_obj)
    print(costo_min_sol)
    
    costo_min = pd.read_csv('vogel.csv') #lee el archivo
    costo_min = costo_min.set_index('fuentes') # No cambiar de nombre
    
    n_col = costo_min_sol.shape[1] - 1
    n_ren = costo_min.shape[0] - 1
    optimiza_met = True
    primera_ite = 0
    print('\nProceso optimizacion solucion inicial\n')
    while optimiza_met:
        if primera_ite == 0:
            matriz = costo_min_sol.iloc[:-1,:-1].to_numpy()
            matriz = matriz.astype('float')
            matriz[matriz == 0] = 'nan' 
            matriz_no_bas = matriz.copy()
            matriz_circuito = matriz.copy()
            matriz_costo = costo_min.iloc[:-1,:-1].to_numpy()
        else:
            matriz = matriz_circuito.copy()
            matriz_no_bas = matriz.copy()
            matriz_circuito = matriz.copy()
        primera_ite += 1
        
        ls_u = [np.nan for i in range(n_ren)]
        ls_v = [np.nan for i in range(n_col)]
        
        ren = 1
        col = 1
        bandera = 0
        ls_u[0] = 0
        
        ls_basicas = []
        for ren in range(n_ren):
            for col in range(n_col):
                if not math.isnan(matriz[ren][col]):
                    ls_basicas.append((ren, col))
                    if not math.isnan(ls_u[ren]) and math.isnan(ls_v[col]):
                        ls_v[col] = matriz_costo[ren][col] - ls_u[ren]                    
                    elif math.isnan(ls_u[ren]) and not math.isnan(ls_v[col]):
                        ls_u[ren] = matriz_costo[ren][col] - ls_v[col]
    
        #print('Valida u')
        for ren in range(len(ls_u)):
            if math.isnan(ls_u[ren]):
                for col in range(n_col):
                    if not math.isnan(matriz[ren][col]):
                        ls_v[col] = matriz_costo[ren][col] - ls_u[ren]   
    
        #print('Valida v')
        for col in range(len(ls_v)):
            if math.isnan(ls_v[col]):
                for ren in range(n_ren):
                    if not math.isnan(matriz[ren][col]):
                        ls_v[col] = matriz_costo[ren][col] - ls_u[ren]      
    
                
                     
        #for c, i in enumerate(ls_u):
            #print('u'+str(c), ':', i)
        #for c, i in enumerate(ls_v):
            #print('v'+str(c), ':', i)
        
        r_entrada = 0
        c_entrada = 0
        entrada = -1000
        #print('No basicoa')
    
        demanda = [] 
        oferta = []       
        for ren in range(n_ren):
            for col in range(n_col):
                if math.isnan(matriz_no_bas[ren][col]):
                   #oferta.append(esquina_noro.iloc[ren, -1])
                   #demanda.append(esquina_noro.iloc[-1, col])
                   matriz_no_bas[ren][col] = ls_u[ren] + ls_v[col] - matriz_costo[ren][col]
                   if matriz_no_bas[ren][col] > entrada:
                       entrada = matriz_no_bas[ren][col]
                       r_entrada = ren
                       c_entrada = col   
                else:
                    matriz_no_bas[ren][col] = 0
        if entrada < 0:
            optimiza_met = False
            break
        #oferta.append(esquina_noro.iloc[r_entrada, -1])
        #demanda.append(esquina_noro.iloc[-1, c_entrada])
        #theta = min(oferta + demanda)
        #print('Valor entrada: ', entrada)
        #print('Valor theta: ', theta)
        #print('Crear circuito')
    
            
        circuito = False
        ban_cir = 0
        ls_circuito = []
    
        r_e = r_entrada
        c_e = c_entrada
    
        #matriz_circuito = matriz.copy()
        #print(r_entrada, c_entrada)
        #print(r_e, c_e)
        ls_aux = ls_basicas
        ls_basicas.append((r_entrada, c_entrada))
        
        ls_basicas_clone = ls_basicas.copy()
      
        #----------------- Concepto de prueba--------------------#
        n = 4
        matriz_circuito2 = matriz.copy()
        matriz_circuito2[r_entrada][c_entrada] = 1
        ban_cir_t = False
        for c, n in enumerate(range(4, len(ls_basicas)+1)):
            #print(n)
            comb = itertools.combinations([c for c, i in enumerate(ls_basicas)], n)
            for com in comb:
                #print(com)
                criterio = len(list(com)) if len(list(com)) % 2 == 0 else len(list(com)) - 1 
                if len(ls_basicas)-1 in list(com):
                    ord_circuito, costo_cir = f_g.encuentra_circuito2(list(com), ls_basicas)
                    num_extremos = 0
                    for i in ord_circuito:
                        #print(i, ls_basicas[i])
                        if isextremo(matriz_circuito2, ls_basicas[i][0], ls_basicas[i][1]):
                           num_extremos += 1 
                    
                    if costo_cir == criterio and num_extremos>=4:
                        #print('La chida')
                        camino = list(com)
                        ban_cir_t = True
                        break
            if ban_cir_t:
                break
        ini = ord_circuito.index(len(ls_basicas)-1)
        camino = ord_circuito[ini:] + ord_circuito[0:ini]

        l_theta = []
        l_theta_p = []

        #print('Valor theta: ', theta)
        #Definir el valor de theta el chido
        signos = 1
        ban_alt = False
        for c, i in enumerate(camino):
            #print(ls_basicas[i])
            ren = ls_basicas[i][0]
            col = ls_basicas[i][1]
            if c == 0:
                matriz_circuito[ren][col] = 100000
            else:
                if signos % 2 != 0:
                    if isextremo(matriz_circuito2, ren, col):
                        #print(matriz_circuito[ren][col])
                        #print("resta m[{}][{}]".format(ren, col))
                        if matriz_circuito[ren][col] == 0:
                            ban_alt = True
                        l_theta.append(matriz_circuito[ren][col])
                        signos += 1
                else:
                    if isextremo(matriz_circuito2, ren, col):
                        l_theta_p.append(matriz_circuito[ren][col])
                        signos += 1
        theta = min(l_theta)
        
        #if ban_alt:
            #theta = min(l_theta_p)
        
        
        
        
        #matriz_circuito = matriz.copy()
        #m_aux = 
        matriz_circuito2 = matriz.copy()
        matriz_circuito2[r_entrada][c_entrada] = theta
        signos = 1
        for c, i in enumerate(camino):
            #print(ls_basicas[i])
            ren = ls_basicas[i][0]
            col = ls_basicas[i][1]
            if c == 0:
                matriz_circuito[ren][col] = theta
            else:
                if signos % 2 != 0:
                    if isextremo(matriz_circuito2, ren, col):
                        matriz_circuito[ren][col] -= theta
                        #print("resta m[{}][{}]".format(ren, col))
                        signos += 1
                else:
                    if isextremo(matriz_circuito2, ren, col):
                        #print("suma m[{}][{}]".format(ren, col))
                        matriz_circuito[ren][col] += theta
                        signos += 1
        ban_for = False
        for ren in range(n_ren):
            for col in range(n_col):
                if matriz_circuito[ren][col] == 0:
                    matriz_circuito[ren][col] = 'nan'
                    ban_for = True
                    break
            if ban_for:
                break
    
    fun_obj2 = 0
    for ren in range(n_ren):
        for col in range(n_col):
            if not math.isnan(matriz[ren][col]):
                fun_obj2 += (matriz[ren][col] * matriz_costo[ren][col])
    print('Funcion Objetivo:: ', fun_obj2)
    print(pd.DataFrame(matriz))
