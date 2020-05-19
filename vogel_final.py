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
import sys



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
    
    ruta = r'C:\Users\raulr\Desktop/' # ruta del archivo
    vogel = pd.read_csv('vogel.csv')
    vogel.dropna(inplace=True)
    vogel = vogel.set_index('fuentes')
    
                
    ls_col = []    
    for col in list(vogel.columns)[:-1]:
        #print([col])
        val_x_ren = vogel[col][:-1].sort_values(ascending=True)
        val_x_ren = list(val_x_ren[0:2])       
        ls_col.append(abs(val_x_ren[0] - val_x_ren[1]))
    ls_col.append(0)
    row_df = pd.DataFrame([ls_col], columns=vogel.columns)
    vogel = pd.concat([vogel, row_df], ignore_index=True)   

    ls_ren = []
    indice_fila = 0
    for indice_fila in range(vogel.shape[0]-2):
        #print(indice_fila)
        val_x_ren = vogel.iloc[indice_fila][:-1].sort_values(ascending=True)
        val_x_ren = list(val_x_ren[0:2])       
        ls_ren.append(abs(val_x_ren[0] - val_x_ren[1]))
    ls_ren.append(0)
    ls_ren.append(0)
    vogel['penalizacion'] = ls_ren

    vogel_sol = vogel.copy()
    for i in range(vogel.shape[0]-2):
        for j in range(len(vogel.columns)-2):
                vogel_sol.iloc[i,j] = 0
                
    bandera = True
    fun_obj = 0
    while bandera:
        #Penalizacion columna
        if len(vogel.columns) == 2 or vogel.shape[0] == 2:
            print('Se acabaron las columnas')
            bandera = False
            break
        indice_pen_col = vogel.iloc[:-2, -1].idxmax()
        max_pen_col = vogel.iloc[:-2, -1].max()
        
        #Penalizacion renglon
        indice_pen_ren = vogel.iloc[-1,:-2].idxmax()
        max_pen_ren = vogel.iloc[-1,:-2].max()
        if max_pen_col == 0 and max_pen_ren==0:
            print('Se termino el proceso')    
            for i in list(vogel.columns)[:-2]:            
                vogel_sol[i][list(vogel.index)[0]] = vogel[i][-2:-1].values[0]
            bandera = False
    
        else:        
            if max_pen_col > max_pen_ren:# Si esto occure buscara el valor minimo de la columna de los contrario buscara el minimo del renglon
                print('Buscara por renglon', indice_pen_col)
                #list(vogel.index).index(2)
#               indice_val_min = vogel.iloc[indice_pen_col, :-2].idxmin()
                indice_pen_col_sol = indice_pen_col
                indice_pen_col = list(vogel.index).index(indice_pen_col)
                indice_val_min = vogel.iloc[indice_pen_col, :-2].idxmin()
                oferta = vogel.iloc[indice_pen_col, -2]
                demanda = vogel[indice_val_min][-2:-1].values[0]
                if demanda != 0 and oferta != 0:            
                    if oferta > demanda:
                        print('oferta > demanda')
                        fun_obj += (vogel.iloc[indice_pen_col][indice_val_min] * demanda)
                        vogel_sol.iloc[indice_pen_col_sol][indice_val_min] = demanda
                        vogel[indice_val_min][-2:-1].values[0] = 0
                        vogel.iloc[indice_pen_col,-2] = vogel.iloc[indice_pen_col,-2] - demanda
                        vogel.iloc[indice_pen_col, -1] = 0
                        vogel.drop(indice_val_min, inplace=True, axis=1)
                        if oferta==demanda:
                            vogel.drop(indice_pen_col, inplace=True, axis=0)                    
                    else:
                        print('demanda < oferta')
                        fun_obj += (vogel.iloc[indice_pen_col][indice_val_min] * oferta)
                        vogel_sol.iloc[indice_pen_col_sol][indice_val_min] = oferta
                        vogel.iloc[indice_pen_col,-2] = 0
                        vogel[indice_val_min][-2:-1].values[0] = vogel[indice_val_min][-2:-1].values[0] - oferta
                        vogel.iloc[indice_pen_col,-1] = 0
                        vogel.drop(indice_pen_col_sol, inplace=True, axis=0)
# =============================================================================
#                         if oferta==demanda:
#                             vogel.drop(indice_pen_col, inplace=True, axis=1)
# =============================================================================
                else:
            # Si la oferta o la demanda son 0  se elimina de la tabla
                    if demanda == 0:
                        vogel.drop(indice_val_min, inplace=True, axis=1)
                    else:
                        vogel.drop(indice_pen_col_sol, inplace=True, axis=0)
                    
            else:
                print('Buscara por columna', indice_pen_ren)
                indice_val_min = vogel[indice_pen_ren].iloc[:-2].idxmin()            
                oferta = vogel.loc[indice_val_min,:][-2] #vogel.iloc[indice_val_min,-2]
                demanda = vogel[indice_pen_ren][-2:-1].values[0]
                if demanda != 0 and oferta != 0: 
                    if oferta > demanda:
                        print('oferta > demanda')
                        fun_obj += (vogel[indice_pen_ren][indice_val_min] * demanda)
                        vogel_sol[indice_pen_ren][indice_val_min] = demanda
                        vogel[indice_pen_ren][-2:-1].values[0] = 0
                        #vogel.iloc[indice_val_min,-2] = vogel.iloc[indice_val_min,-2] - demanda
                        vogel.iloc[indice_val_min,-2] = vogel.iloc[list(vogel.index).index(indice_val_min),-2] - demanda
                        vogel[indice_pen_ren].iloc[-1] = 0
                        vogel.drop(indice_pen_ren, inplace=True, axis=1)
# =============================================================================
#                         if oferta==demanda:
#                             vogel.drop(indice_val_min, inplace=True, axis=0)                     
# =============================================================================
                    else:
                        print('demanda < oferta')
                        fun_obj += (vogel[indice_pen_ren][indice_val_min] * oferta)
                        vogel_sol[indice_pen_ren][indice_val_min] = oferta
                        vogel.iloc[indice_val_min,-2] = 0
                        vogel[indice_pen_ren][-2:-1].values[0] = vogel[indice_pen_ren][-2:-1].values[0] - oferta
                        vogel[indice_pen_ren].iloc[-1] = 0
                        vogel.drop(indice_val_min, inplace=True, axis=0)
                else:
            # Si la oferta o la demanda son 0  se elimina de la tabla
                    if demanda == 0:
                        vogel.drop(indice_pen_ren, inplace=True, axis=1)
                    else:
                        vogel.drop(indice_val_min, inplace=True, axis=0)                        
# =============================================================================
#                         if oferta==demanda:
#                             vogel.drop(indice_val_min, inplace=True, axis=1)
# =============================================================================
    print('******************************') 
    print('Funcion Objetivo: ', fun_obj)
    print(vogel_sol)

    vogel = pd.read_csv('vogel.csv')
    vogel.dropna(inplace=True)
    vogel = vogel.set_index('fuentes')
    
    vogel_sol = vogel_sol[:-1]
    vogel_sol = vogel_sol.iloc[:,:-1]
    
    n_col = vogel_sol.shape[1] - 1
    n_ren = vogel_sol.shape[0] - 1
    optimiza_met = True
    primera_ite = 0
    print('\nProceso optimizacion solucion inicial\n')
    while optimiza_met:
        if primera_ite == 0:
            matriz = vogel_sol.iloc[:-1,:-1].to_numpy()
            matriz = matriz.astype('float')
            matriz[matriz == 0] = 'nan' 
            matriz_no_bas = matriz.copy()
            matriz_circuito = matriz.copy()
            matriz_costo = vogel.iloc[:-1,:-1].to_numpy()
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
