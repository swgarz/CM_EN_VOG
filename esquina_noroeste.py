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

    return bandera , -1, -1

if __name__ == '__main__':

    ruta = 'C://Users//nuria//Desktop//daniel//Opti//programas//vogel.csv' # ruta del archivo
    esquina_noro = pd.read_csv('vogel.csv') #lee el archivo
    esquina_noro = esquina_noro.set_index('fuentes') # No cambiar de nombre
   
    
    #crea una copia del archivo origel para poder las soluciones
    esquina_noro_sol = esquina_noro.copy()
    for i in range(esquina_noro.shape[0]-1):
        for j in range(len(esquina_noro.columns)-1):
                esquina_noro_sol.iloc[i,j] = 0

    # Esta x y nos sirven para asignar los valores a nuestra tabla de soluciones
    x = 0
    y = 0
    fun_obj = 0
    bandera = True
    ofer = -1
    dem = -1
    while True:
        #Si la oferta y la demanda son 0 salir del proceso
        if (ofer==0 and dem == 0) or (esquina_noro.shape[0]<1):
            print('Proceso terminado')
            bandera = False
            break
        
        #obtiene la posicion de la oferta y demanda de nuestro archivo 
        ind_oferta = len(esquina_noro.columns) -1
        ind_demanda = esquina_noro.shape[0] - 1   
        #obtiene la oferta y demanda de nuestro archivo siempre de la esquina noroeste 
        ofer = esquina_noro.iloc[0, ind_oferta]
        dem = esquina_noro.iloc[ind_demanda, 0]

        # Entrara al proceso si la demanda y la oferta son diferentes de 0
        if dem != 0 and ofer != 0:
            # si la demanda es mayor a la oferta entra en caso contrario pasa el else
            # aqui se hace asigna la maxima cantidad  dependiendo las restricciones de la oferta y demanda
            if dem > ofer:
                esquina_noro_sol.iloc[x, y] = ofer 
                fun_obj += (esquina_noro.iloc[0, 0] * ofer) # multiplica la oferta por el costo
                esquina_noro.iloc[0, ind_oferta] = esquina_noro.iloc[0, ind_oferta] - ofer # Se le quita la oferta a la oferta
                esquina_noro.iloc[ind_demanda, 0] = esquina_noro.iloc[ind_demanda, 0] - ofer  # Se le quita la oferta a la demanda
                esquina_noro.drop(esquina_noro.index[0], inplace=True, axis=0)
                x += 1

            else:
                esquina_noro_sol.iloc[x, y] = dem
                fun_obj += (esquina_noro.iloc[0, 0] * dem)
                esquina_noro.iloc[0, ind_oferta] = esquina_noro.iloc[0, ind_oferta] - dem # Se le quita la demanda a la oferta
                esquina_noro.iloc[ind_demanda, 0] = esquina_noro.iloc[ind_demanda, 0] - dem # Se le quita la demanda a la demanda
                esquina_noro.drop(esquina_noro.columns[0], inplace=True, axis=1)
                y += 1
        else:
            # Si la oferta o la demanda son 0  se elimina de la tabla
            if dem > ofer:
                esquina_noro.drop(esquina_noro.index[0], inplace=True, axis=0)
                x += 1
            else:
                esquina_noro.drop(esquina_noro.columns[0], inplace=True, axis=1)
                y += 1
        #Si la oferta y la demanda son 0 salir del proceso                
        if (ofer==0 and dem == 0) or (esquina_noro.shape[0]<1):
            print('Proceso terminado')
            bandera = False
            break

    print('******************************') 
    print('Funcion Objetivo: ', fun_obj)
    print(esquina_noro_sol)
    
    esquina_noro = pd.read_csv('vogel.csv') #lee el archivo
    esquina_noro = esquina_noro.set_index('fuentes') # No cambiar de nombre
    
    n_col = esquina_noro_sol.shape[1] - 1
    n_ren = esquina_noro_sol.shape[0] - 1
    optimiza_met = True
    primera_ite = 0
    print('\nProceso optimizacion solucion inicial\n')
    while optimiza_met:
        if primera_ite == 0:
            matriz = esquina_noro_sol.iloc[:-1,:-1].to_numpy()
            matriz = matriz.astype('float')
            matriz[matriz == 0] = 'nan' 
            matriz_no_bas = matriz.copy()
            matriz_circuito = matriz.copy()
            matriz_costo = esquina_noro.iloc[:-1,:-1].to_numpy()
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
    
    
    
