# pseudocodigo Costo Mínimo
      
 
	SI __name__ = '__main__':
	costo_min <- LEER(voguel.csv)
	costo_min.dropna(inplace=True) 
	costo_min <- LEER(Archivo_Voguel)
	costo_min_sol <- costo_min 
	PARA i <- 0 HASTA n_renglones - 1 HACER
		PARA j HASTA N_columnas -1 HACER
			costo_min_sol[i][j] <- 0

	 bandera <- True
	 fun_obj <- 0
	 MIENTRAS True HACER 
	     minimos <- costo_min.iloc[:-1, :-1].idxmin(axis=1)
	     SI minimos.shape[0] = 0
		  bandera <- False
		  ESCRIBIR 'Proceso terminado' 
		  break

     	     minimo <- costo_min[costo_min.index[0], minimos[0]]
     	     count <- 0
             renglon <- 0
             columna <- minimos[0]
             PARA i <- 0 HASTA n_renglones -1 HACER
            	aux <- costo_min[costo_min.index[i], minimos[i]]
            	SI aux < minimo ENTONCES  
                  renglon <- i
                  columna <- minimos[i]
                  minimo <- aux
     	     oferta <- costo_min[renglon, -1]
     	     demanda <- costo_min[costo_min.index[-1], columna]
     	     SI demanda != 0 and oferta != 0 ENTONCES
     		SI oferta > demanda ENTONCES
		    func_obj <- func_obj + (costo_min[costo_min[renglon], columna] * demanda)
		    costo_min_sol[costo_min.index[renglon], columna] <- demanda 
		    costo_min[costo_min.index[-1], columna] <- 0
		    costo_min[renglon, -1] <- costo_min[renglon, -1] - demanda 
		    
		    costo_min.drop(columna_0)
	        SI NO ENTONCES
		    fun_obj <- func_obj + (costo_min[costo_min.index[renglon], columna] * oferta)
		    costo_min_sol[costo_min[renglon], columna] <- oferta
		    costo_min[renglon, -1] <- 0
		    costo_min[costo_index[-1], columna] <- costo_min[costo_min[-1], columna]
		    costo_min.drop(renglon_0) 
		SI minimos.shape[0] = 0
		    bandera <- False
		    break
		    ESCRIBIR "Proceso terminado"
		FINSI
		FINSI
	     SI NO ENTONCES
	     	SI demanda = 0
			costo_min.drop(columna_0)
		SI NO
			costo_min.drop(renglon_0)
		    
	     ESCRIBIR '**************************'
	     ESCRIBIR 'Funcion Objetivo', fun_obj
	     ESCRIBIR costo_min_sol
     
     costo_min <- LEER(vogel.csv)
     costo_min <- LEER(vogel.csv)
     n_col <- costo_min_sol.shape[1] - 1
     n_ren <- costo_min.shape[0] - 1
     optimiza_met <- true
     primera_ite <- 0
     ESCRIBIR 'Solucion inicial'
     MIENTRAS optimiza_met HACER
      SI primera_ite = 0
            matriz <- costo_min_sol[:-1, :-1].to_numpy()
            matriz <- matriz.astype('float')
            matriz [matriz = 0] <- 'nan'
            matriz_no_bas <- matriz
            matriz_circuito <- matriz
	    matriz_costo <- costo_min[:-1, :-1].to_numpy()
      SI NO
            matriz <- matriz_circuito
            matriz_no_bas <- matriz
            matriz_circuito <- matriz
      primera_ite <- + 1
      PARA i HASTA n_ren HACER
      	ls_u <- i
      FINPARA
      PARA i HASTA n_col HACER 
      	ls_v <- i
      FINPARA
      ren <- 1
      col <- 1
      bandera <- 0
      ls_u [0] <- 0
      ls_basicas <- []
      PARA ren=1 INCREMENTO 1 HASTA n_ren
            PARA col=1 INCREMENTO 1 HASTA n_col
                  SI not math.isnan(matriz[ren][col]) ENTONCES
                        ls_basicas.append((ren, col))
                        Si not SI not math.isnan(ls_u[ren]) AND math.isnan(ls_v[col]) ENTONCES 
                              ls_v[col] <- matriz_costo[ren][col] - ls_u[ren]
                        SINO SI math.isnan(ls_u[ren]) AND NOT math.isnan(ls_v[col]) ENTONCES
                              ls_u[ren] <- matriz_costo[ren][col] - ls_v[col]
		        FINSI
		   FINSI
	      FINPARA
     FINPARA
        PARA ren <- 0 HASTA len(ls_u) HACER
            SI math.isnan(ls_u[ren]) ENTONCES
                PARA col <- 0 HASTA n_col HACER
                    SI not math.isnan(matriz[ren][col]) ENTONCES
                        ls_v[col] <- matriz_costo[ren][col] - ls_u[ren]   
		    FINSI
		FINPARA
	     FINSI               
        FINPARA
	PARA col <- 0 HASTA len(ls_v) HACER
            SI math.isnan(ls_v[col]) ENTONCES
                PARA ren <- 0 HASTA n_ren HACER
                    SI not math.isnan(matriz[ren][col]) ENTONCES
                        ls_v[col] <- matriz_costo[ren][col] - ls_u[ren]      
		    FINSI                    
                FINPARA
	    FINSI
	 FINPARA
 
      r_entrada <- 0
      c_entrada <- 0
      entrada <- -1000
      demanda <- []
      oferta <- []
      PARA ren <- 0 HASTA n_ren HACER
            PARA col <- 0 HASTA n_col HACER
                SI math.isnan(matriz_no_bas[ren][col]) ENTONCES
                   matriz_no_bas[ren][col] <- ls_u[ren] + ls_v[col] - matriz_costo[ren][col]
                   SI matriz_no_bas[ren][col] > entrada ENTONCES
                       entrada <- matriz_no_bas[ren][col]
                       r_entrada <- ren
                       c_entrada <- col   
                   FINSI
                SI NO ENTONCES
                    matriz_no_bas[ren][col] <- 0
                FINSI
	    FINPARA
	FINPARA
	SI entrada < 0 ENTONCES
            optimiza_met <- False
            break 
        FINSI
	
      circuito <- false
      ban_cir <- 0
      ls_circuito <- []
      r_e <- r_entrada
      c_e <- c_entrada
      ls_aux <- ls_basicas
      ls_basicas.append((r_entrada, c_entrada))
      ls_basicas_clone <- ls_basicas
      
   <!-- Concepto de prueba -->
   
      n <- 4
      matriz_circuito2 <- matriz
      matriz_circuito2 [r_entrada][c_entrada] <- 1
      ban_cir_t <- False
      
      PARA c <- 0, n <- 4 HASTA enumerate(len(ls_basicas)+1) HACER
        comb <- itertools.combinations([c PARA c <- 0, i <- 0 HASTA enumerate(ls_basicas) FINPARA], n )                                         
        PARA com <- 0 HASTA comb HACER
		SI len(list(com)) % 2 = 0 
			criterio <- len(list(com))
		SI NO ENTONCES 
			criterio <- len(list(com)) - 1 
		FINSI
                                      
            SI len(ls_basicas)-1 in list(com) ENTONCES
                ord_circuito, costo_cir <- encuentra_circuito2(list(com), ls_basicas)
                num_extremos <- 0
                PARA i HASTA ord_circuito HACER
                    SI isextremo(matriz_circuito2, ls_basicas[i][0], ls_basicas[i][1]) ENTONCES
                       num_extremos = num_extremos + 1 
                    FINSI
                FINPARA
                SI costo_cir = criterio AND num_extremos>=4 ENTONCES
                    camino <- list(com)
                    ban_cir_t <- True
                    break
				FINSI
			FINSI
        FINPARA
        SI ban_cir_t ENTONCES
            break
        FINSI
    FINPARA
	
    ini <- ord_circuito.index(len(ls_basicas)-1)
    camino <- ord_circuito[ini:] + ord_circuito[0:ini]
    l_theta <- []
    l_theta_p <- []
    
    signos <- 1
    ban_alt <- False
    PARA c <- 0, i <- 0 HASTA enumerate(camino) HACER
        ren <- ls_basicas[i][0]
        col <- ls_basicas[i][1]
        SI c = 0 ENTONCES
            matriz_circuito[ren][col] <- 100000
        SI NO ENTONCES
            SI signos % 2 != 0 ENTONCES
                SI isextremo(matriz_circuito2, ren, col):
                    SI matriz_circuito[ren][col] = 0 ENTONCES
                        ban_alt <- True
                    FINSI
                    l_theta.append(matriz_circuito[ren][col])
                    signos = signos + 1
                FINSI
            SI NO ENTONCES
                SI isextremo(matriz_circuito2, ren, col):
                    l_theta_p.append(matriz_circuito[ren][col])
                    signos = signos + 1
				FINSI
			FINSI
        FINSI
    FINPARA
    theta <- min(l_theta)

    matriz_circuito2 <- matriz
    matriz_circuito2[r_entrada][c_entrada] <- theta
    signos <- 1
    PARA c <- 0, i <- 0 HASTA enumerate(camino) HACER
        ren <- ls_basicas[i][0]
        col <- ls_basicas[i][1]
        SI c = 0 ENTONCES
            matriz_circuito[ren][col] <- theta
        SI NO ENTONCES
            SI signos % 2 != 0 ENTONCES
                SI isextremo(matriz_circuito2, ren, col) ENTONCES
                    matriz_circuito[ren][col] <- matriz_circuito[ren][col] -  theta                                                 
                    signos <- signos + 1
                FINSI
            SI NO ENTONCES
                SI isextremo(matriz_circuito2, ren, col) ENTONCES                                                
                    matriz_circuito[ren][col] <- matriz_circuito[ren][col] + theta
                    signos <- + signos 1
				FINSI
			FINSI
		FINSI
    FINPARA
    ban_for <- False
        
    PARA ren <- 0 HASTA n_ren HACER
        PARA col <- 0 n_col HACER
            SI matriz_circuito[ren][col] = 0 ENTONCES
                matriz_circuito[ren][col] <- 'nan'
                ban_for <- True                        
                break
            FINSI
        FINPARA
        SI ban_for ENTONCES
               FINPARA
            break
        FINSI
	FINPARA
	ENDWHILE

	fun_obj2 <- 0
	PARA ren <- 0 HASTA n_ren HACER
	    PARA col <- 0 HASTA n_col HACER
		SI not math.isnan(matriz[ren][col]) ENTONCES
		    fun_obj2 <- fun_obj2 + (matriz[ren][col] * matriz_costo[ren][col])
		FINSI
		FINPARA
	FINPARA
	ESCRIBIR 'Funcion Objetivo:: ', fun_obj2
	ESCRIBIR matriz         

   
              
  
 
 
 # pseudocodigo Esquina Noroeste
      import pandas as pd
      import numpy as np
      import math
      import encuentra_circuitos as f_g
      import itertools
      import mlrose


      FUNCTION aptitud2(poA, poB):
    SI poA[0] = poB[0] OR poA[1] = poB[1] ENTONCES
        RETURN 2
    SI NO ENTONCES ENTONCES
        RETURN 1
    FINSI
      ENDFUNCTION


      FUNCTION encuentra_circuito2(orden, ls_basicas):
	    
	PARA i HASTA len(orden) HACER
		orden_aux <- i
	FINPARA
                   
    dist_list <- []
    PARA i in orden_aux:
        PARA j in orden_aux:
            SI i != j ENTONCES
                costo <- aptitud2(ls_basicas[orden[i]], ls_basicas[orden[j]])
                dist_list.append((i, j, costo))
            FINSI
		FINPARA
	FINPARA

    fitness_dists <- mlrose.TravellingSales(distances <- dist_list)
    problem_fit <- mlrose.TSPOpt(length <- len(orden), fitness_fn <- fitness_dists, maximize=True)
    best_state, best_fitness <- mlrose.genetic_alg(problem_fit, random_state <- 2)
	
    resul <- []
    PARA i <- 0 HASTA len(best_state) HACER
        resul.append(orden[i])
    FINPARA

    ini <- resul.index(len(ls_basicas)-1)
    resul <- resul[ini:] + resul[0:ini]
    result <- resul + [resul[0]]
    sum_total <- 0

    PARA i <- 0 HASTA len(result)-1 HACER
        costo <- aptitud2(ls_basicas[result[i]], ls_basicas[result[i+1]])
        SI costo = 1 ENTONCES
            best_fitness = best_fitness + .5
            RETURN resul, best_fitness/2            
        FINSI
    FINPARA
    RETURN resul, best_fitness/2
      ENDFUNCTION


      FUNCTION isextremo(matriz, ren, col):
    up, x_up, y_up <- arriba(ren, col, matriz)
    down, x_down, y_down <- abajo(ren, col, matriz)
    right, x_right, y_right <- derecha(ren, col, matriz)
    left, x_left, y_left <- izquierda(ren, col, matriz)
    SI down AND right ENTONCES
        RETURN True
    SINO SI left AND down ENTONCES
        RETURN True
    SINO SI up AND right ENTONCES
        RETURN True
    SINO SI up AND left ENTONCES
        RETURN True
    SI NO ENTONCES
        RETURN False
    FINSI
      ENDFUNCTION

      FUNCTION arriba(x, y, matriz):
    bandera <- False
    ren <- x - 1
    MIENTRAS ren >= 0 HACER
        SI not math.isnan(matriz[ren][y]):
            bandera <- True
            RETURN True, ren, y
        FINSI
        ren <- ren - 1
    ENDWHILE
    RETURN bandera , -1, -1
      ENDFUNCTION


      FUNCTION abajo(x, y, matriz):
    bandera <- False
    n_ren <- len(matriz[0])
    PARA ren in range(x+1, n_ren):
        SI not math.isnan(matriz[ren][y]):
            bandera <- True
            RETURN bandera, ren, y
        FINSI
    FINPARA
    RETURN bandera , -1, -1
      ENDFUNCTION

      FUNCTION derecha(x, y, matriz):
    bandera <- False
    n_col <- len(matriz[0][:])
    PARA col in range(y+1, n_col):
        SI not math.isnan(matriz[x][col]):
            bandera <- True
            RETURN True, x, col
        FINSI
    FINPARA
    RETURN bandera , -1, -1
      ENDFUNCTION


      FUNCTION izquierda(x, y, matriz):
    bandera <- False
    col <- y - 1
    MIENTRAS col>=0 HACER
        SI not math.isnan(matriz[x][col]):
            bandera <- True
            RETURN True, x, col
        FINSI
        col <- col - 1
    ENDWHILE
    RETURN bandera , -1, -1
       ENDFUNCTION


      SI __name__ = '__main__':

    esquina_noro <- LEER(Archivo_Vogel)       
    esquina_noro_sol <- LEER(Archivo_Vogel)
	
	
    PARA i <-0 HASTA n_renglones - 1 HACER
        PARA j HASTA n_columnas - 1 HACER
				esquina_noro_sol[i][j] <- 0                
		FINPARA
    FINPARA
	
    x <- 0
    y <- 0
    fun_obj <- 0
    bandera <- True
    ofer <- -1
    dem <- -1

    MIENTRAS True HACER        
        SI (ofer == 0 AND dem == 0) OR (num_renglones < 1):
            ESCRIBIR 'Proceso terminado'
            bandera <- False
            break        
        FINSI
		
        ind_oferta <- num_columnas -1
        ind_demanda <- num_renglones - 1           
        ofer <- esquina_noro[0, ind_oferta]
        dem <- esquina_noro[ind_demanda, 0]

        SI dem != 0 AND ofer != 0 ENTONCES                        
            SI dem > ofer ENTONCES
                esquina_noro_sol[x, y] <- ofer 
                fun_obj <- fun_obj + (esquina_noro[0, 0] * ofer) 
                esquina_noro[0, ind_oferta] <- esquina_noro[0, ind_oferta] - ofer
                esquina_noro[ind_demanda, 0] <- esquina_noro[ind_demanda, 0] - ofer
				
                esquina_noro.drop(renglon_0)
                x <- x + 1
            SI NO ENTONCES
                esquina_noro_sol[x, y] <- dem
                fun_obj <- fun_obj + esquina_noro[0, 0] * dem)
                esquina_noro[0, ind_oferta] <- esquina_noro[0, ind_oferta] - dem
                esquina_noro[ind_demanda, 0] <- esquina_noro[ind_demanda, 0] - dem
                esquina_noro.drop(columna_0)
                y <- y + 1
            FINSI
        SI NO ENTONCES           
            SI dem > ofer ENTONCES
                esquina_noro.drop(renglon_0)
                x <- x + 1
            SI NO ENTONCES
                esquina_noro.drop(columna_0)
                y <- y + 1
            FINSI        
        FINSI
        SI (ofer==0 AND dem == 0) OR (num_renglones<1):
            ESCRIBIR 'Proceso terminado'
            bandera <- False
            break
        FINSI
    ENDWHILE
	
    ESCRIBIR '******************************' 
    ESCRIBIR 'Funcion Objetivo: ', fun_obj
    ESCRIBIR esquina_noro_sol

    esquina_noro <- LEER(Archivo_Vogel)       
    esquina_noro_sol <- LEER(Archivo_Vogel)
		
    n_col <- esquina_noro_sol.shape[1] - 1
    n_ren <- esquina_noro_sol.shape[0] - 1
    optimiza_met <- True
    primera_ite <- 0
	
    ESCRIBIR '\nProceso optimizacion solucion inicial\n'
	
    MIENTRAS optimiza_met HACER
        SI primera_ite = 0 ENTONCES
            matriz <- esquina_noro_sol[:n_ren-1, :n_col-1]
            matriz <- matriz.astype('float')
            matriz[matriz = 0] <- 'nan' 
            matriz_no_bas <- matriz
            matriz_circuito <- matriz
            matriz_costo <- esquina_noro[:-1,:-1].to_numpy()
        SI NO ENTONCES
            matriz <- matriz_circuito
            matriz_no_bas <- matriz
            matriz_circuito <- matriz
        FINSI

        primera_ite <- primera_ite + 1
		
		PARA i HASTA n_ren HACER
			ls_u <- i
		FINPARA
		
		PARA i HASTA n_col HACER
			ls_v <- i
		FINPARA		
		

        ren <- 1
        col <- 1
        bandera <- 0
        ls_u[0] <- 0
        ls_basicas <- []
		
        PARA ren <- 0 HASTA n_ren HACER
            PARA col <- 0 HASTA n_col HACER
                SI not math.isnan(matriz[ren][col]) ENTONCES
                    ls_basicas.append((ren, col))
                    SI not math.isnan(ls_u[ren]) AND math.isnan(ls_v[col]) ENTONCES
                        ls_v[col] <- matriz_costo[ren][col] - ls_u[ren]                    
                    SINO SI math.isnan(ls_u[ren]) AND not math.isnan(ls_v[col]) ENTONCES
                        ls_u[ren] <- matriz_costo[ren][col] - ls_v[col]
		    FINSI
		FINSI
            FINPARA
        FINPARA

        PARA ren <- 0 HASTA len(ls_u) HACER
            SI math.isnan(ls_u[ren]) ENTONCES
                PARA col <- 0 HASTA n_col HACER
                    SI not math.isnan(matriz[ren][col]) ENTONCES
                        ls_v[col] <- matriz_costo[ren][col] - ls_u[ren]   
		    FINSI
		FINPARA
	    FINSI               
        FINPARA
		
        PARA col <- 0 HASTA len(ls_v) HACER
            SI math.isnan(ls_v[col]) ENTONCES
                PARA ren <- 0 HASTA n_ren HACER
                    SI not math.isnan(matriz[ren][col]) ENTONCES
                        ls_v[col] <- matriz_costo[ren][col] - ls_u[ren]      
		   FINSI                    
                FINPARA
	    FINSI
	FINPARA

        r_entrada <- 0
        c_entrada <- 0
        entrada <- -1000
        demanda <- [] 
        oferta <- [] 
        PARA ren <- 0 HASTA n_ren HACER
            PARA col <- 0 HASTA n_col HACER
                SI math.isnan(matriz_no_bas[ren][col]) ENTONCES
                   matriz_no_bas[ren][col] <- ls_u[ren] + ls_v[col] - matriz_costo[ren][col]
                   SI matriz_no_bas[ren][col] > entrada ENTONCES
                       entrada <- matriz_no_bas[ren][col]
                       r_entrada <- ren
                       c_entrada <- col   
                   FINSI
                SI NO ENTONCES
                    matriz_no_bas[ren][col] <- 0
                FINSI
			FINPARA
		FINPARA
		
        SI entrada < 0 ENTONCES
            optimiza_met <- False
            break
        FINSI
		
        circuito <- False
        ban_cir <- 0
        ls_circuito <- []
        r_e <- r_entrada
        c_e <- c_entrada
        
        ls_aux <- ls_basicas
        ls_basicas.append((r_entrada, c_entrada))
        ls_basicas_clone <- ls_basicas
        
        matriz_circuito2 <- matriz
        matriz_circuito2[r_entrada][c_entrada] <- 1
        ban_cir_t <- False
        PARA c <- 0, n <- 4 HASTA enumerate(len(ls_basicas)+1) HACER
            comb <- itertools.combinations([c PARA c <- 0, i <- 0 HASTA enumerate(ls_basicas) FINPARA], n )
                                             
            PARA com <- 0 HASTA comb HACER
                
				SI len(list(com)) % 2 = 0 
					criterio <- len(list(com))
				SI NO ENTONCES 
					criterio <- len(list(com)) - 1 
				FINSI
                                          
                SI len(ls_basicas)-1 in list(com) ENTONCES
                    ord_circuito, costo_cir <- encuentra_circuito2(list(com), ls_basicas)
                    num_extremos <- 0
                    PARA i HASTA ord_circuito HACER
                        SI isextremo(matriz_circuito2, ls_basicas[i][0], ls_basicas[i][1]) ENTONCES
                           num_extremos = num_extremos + 1 
                        FINSI
                    FINPARA
                    SI costo_cir = criterio AND num_extremos>=4 ENTONCES
                        camino <- list(com)
                        ban_cir_t <- True
                        break
					FINSI
				FINSI
            FINPARA
            SI ban_cir_t ENTONCES
                break
            FINSI
        FINPARA
		
        ini <- ord_circuito.index(len(ls_basicas)-1)
        camino <- ord_circuito[ini:] + ord_circuito[0:ini]
        l_theta <- []
        l_theta_p <- []
        
        signos <- 1
        ban_alt <- False
        PARA c <- 0, i <- 0 HASTA enumerate(camino) HACER
            ren <- ls_basicas[i][0]
            col <- ls_basicas[i][1]
            SI c = 0 ENTONCES
                matriz_circuito[ren][col] <- 100000
            SI NO ENTONCES
                SI signos % 2 != 0 ENTONCES
                    SI isextremo(matriz_circuito2, ren, col):
                        SI matriz_circuito[ren][col] = 0 ENTONCES
                            ban_alt <- True
                        FINSI
                        l_theta.append(matriz_circuito[ren][col])
                        signos = signos + 1
                    FINSI
                SI NO ENTONCES
                    SI isextremo(matriz_circuito2, ren, col):
                        l_theta_p.append(matriz_circuito[ren][col])
                        signos = signos + 1
					FINSI
				FINSI
            FINSI
        FINPARA
        theta <- min(l_theta)

        matriz_circuito2 <- matriz
        matriz_circuito2[r_entrada][c_entrada] <- theta
        signos <- 1
        PARA c <- 0, i <- 0 HASTA enumerate(camino) HACER
            ren <- ls_basicas[i][0]
            col <- ls_basicas[i][1]
            SI c = 0 ENTONCES
                matriz_circuito[ren][col] <- theta
            SI NO ENTONCES
                SI signos % 2 != 0 ENTONCES
                    SI isextremo(matriz_circuito2, ren, col) ENTONCES
                        matriz_circuito[ren][col] = matriz_circuito[ren][col] -  theta                                                 
                        signos += 1
                    FINSI
                SI NO ENTONCES
                    SI isextremo(matriz_circuito2, ren, col) ENTONCES                                                
                        matriz_circuito[ren][col] = matriz_circuito[ren][col] + theta
                        signos += 1
					FINSI
				FINSI
			FINSI
        FINPARA
        ban_for <- False
            
        PARA ren <- 0 HASTA n_ren HACER
            PARA col <- 0 n_col HACER
                SI matriz_circuito[ren][col] = 0 ENTONCES
                    matriz_circuito[ren][col] <- 'nan'
                    ban_for <- True                        
                    break
                FINSI
            FINPARA
            SI ban_for ENTONCES
                   FINPARA
                break
            FINSI
		FINPARA
    ENDWHILE
        
    fun_obj2 <- 0
    PARA ren <- 0 HASTA n_ren HACER
        PARA col <- 0 HASTA n_col HACER
            SI not math.isnan(matriz[ren][col]) ENTONCES
                fun_obj2 = fun_obj2 + (matriz[ren][col] * matriz_costo[ren][col])
            FINSI
		FINPARA
	FINPARA
    ESCRIBIR 'Funcion Objetivo:: ', fun_obj2
    ESCRIBIR matriz

 
 # pseudocodigo Vogel
 
      import pandas as pd
      import numpy as np
      import math
      import encuentra_circuitos as f_g
      import itertools
      import sys
      
      

      FUNCTION isextremo(matriz, ren, col):
    	up, x_up, y_up <- arriba(ren, col, matriz)
    	down, x_down, y_down <- abajo(ren, col, matriz)
    	right, x_right, y_right <- derecha(ren, col, matriz)
    	left, x_left, y_left <- izquierda(ren, col, matriz)
    
    	SI down AND right ENTONCES
        	RETURN True
    	SINO SI left AND down ENTONCES
        	RETURN True
    	SINO SI up AND right ENTONCES
        	RETURN True
    	SINO SI up AND left ENTONCES
        	RETURN True
    	SI NO ENTONCES
        	RETURN False
    	FINSI
      ENDFUNCTION

      FUNCTION arriba(x, y, matriz):
    	bandera <- False
    	ren <- x - 1
    	MIENTRAS ren >= 0 HACER
        	SI not math.isnan(matriz[ren][y]):
            		bandera <- True
            		RETURN True, ren, y
        	FINSI
        ren <- ren - 1
	ENDWHILE
	RETURN bandera , -1, -1
       ENDFUNCTION
       
       FUNCTION abajo(x, y, matriz):
    	bandera <- False
    	n_ren <- len(matriz[0])
    	PARA ren in range(x+1, n_ren):
        	SI not math.isnan(matriz[ren][y]):
            		bandera <- True
            		RETURN bandera, ren, y
        	FINSI
    	FINPARA
    	RETURN bandera , -1, -1
       ENDFUNCTION

       FUNCTION derecha(x, y, matriz):
    	bandera <- False
    	n_col <- len(matriz[0][:])
    	PARA col in range(y+1, n_col):
        	SI not math.isnan(matriz[x][col]):
            		bandera <- True
            		RETURN True, x, col
        	FINSI
    	FINPARA
    	RETURN bandera , -1, -1
       ENDFUNCTION
       
       FUNCTION izquierda(x, y, matriz):
    	bandera <- False
    	col <- y - 1
    	MIENTRAS col>=0 HACER
       		SI not math.isnan(matriz[x][col]):
            		bandera <- True
            		RETURN True, x, col
        	FINSI
        	col <- col - 1
    	ENDWHILE
    	RETURN bandera , -1, -1
       ENDFUNCTION
       
       SI __name__ = '__main__'
       		ruta <- ''
		vogel <- LEER(vogel.csv)
		vogel <- LEER(vogel.csv)
		
		ls_col <- []
		PARA col <- 0 list(vogel.columns)[:-1] HACER
			val_x_ren <- vogel[col][:-1].sort_values(ascending <- True)
			valex_ren <- list(val_x_ren[0:2])
			ls_col.append(abs(val_x_ren[0] - val__ren[1]))
		ls_col.append(0)
		row_df <- pd.DataFrame([ls_col], columns <- vogel.columns)
		vogel <- pd.concat([vogel, row_df]. ignore_index <- True)
		
		ls_ren <- []
		inidice_fila <- 0
		PARA indice_fila <- 0 HASTA vogel.shape[0]-2 HACER
			val_x_ren <- vogel[indice_fila][:-1].sort_values(ascending <- True)
			val_x_ren <- list(val_x_ren[0:2])
			ls_re.append(abs(val_ren[0] - val_x_ren[1]))
		ls_ren.append(0)
		ls_ren.append(0)
		vogel['penalizacion'] <- ls_ren
		vogel_sol <- vogel
		PARA i <- 0 HASTA vogel.shape[0]-2 HACER
			PARA j <- 0 HASTA (len(vogel.columns)-2) HACER
				vogel_sol[i,j] <- 0
		bandera <- True
		func_obj <- 0
		MIENTRAS bandera HACER
			SI len(vogel.columns) 0 2 or vogel.shape[0] = 2
				ESCRIBIR 'Se acabaron las columnas'
				bandera <- False
				break
			indice_pen_col <- vogel[:-2, -1].idxmax()
			max_pen_col<- vogel[:-2, -1].max()
			
			indice_pen_re <- vogel[-1, :-2].idmax()
			SI max_pen_col = 0 and max_pen_ren = 0
				ESCRIBIR 'Se termino el proceso'
				PARA i <-0 HASTA list(vogel.columns)[:-2]
					vogel_sol[i][list(vogel.index)[0]] <- vogel[i][-2:-1].values[0]
				bandera <- False
				FINPARA
			SI NO ENTONCES
				SI max_pen_col > max_pen_ren ENTONCES
					ESCRIBIR 'Buscara un renglon', indice_pen_col
					indice_pen_col_sol <- indice_pen_col
					indice_pen_col <- list(vogel.index).index(indice_pen_col)
					indice_val_min <- vogel[indide_pen_col, :-2.idxmin()
					oferta <- vogel[indice_pen_col, -2]
					demanda <- vogel[indice_val_min][-2:-1].values[0]
					SI demanda != 0 anda oferta != 0 ENTONCES
						SI oferta > demanda ENTONCES
							ESCRIBIR 'oferta>demanda'
							fun_obj <- oferta_obj + (vogel.iloc[indice_pen_col][indice_val_min] * demanda)
							vogel_sol[indice_pen_col_sol][indice_val_min] <- demanda
							vogel[indice_val_min][-2:-1].values[0] <- 0
							vogel[indice_pen_col,-2] <- vogel.iloc[indice_pen_col,-2] - demanda
							vogel[indice_pen_col, -1] <- 0
							vogel.drop(indice_val_min)
							SI oferta = demanda
								vogel.drop(indice_pen_col)
						SI NO 
							ESCRIBIR 'demanda < ofeta'
							fun_obj <- fun_obj + (vogel.iloc[indice_pen_col][indice_val_min] * oferta)
                        				vogel_sol[indice_pen_col_sol][indice_val_min] <- oferta
							vogel[indice_pen_col,-2] <- 0
							vogel[indice_val_min][-2:-1].values[0] <- vogel[indice_val_min][-2:-1].values[0] - oferta
							vogel[indice_pen_col,-1] <- 0
							vogel.drop(indice_pen_col_sol)
							
					SI NO ENTONCES
					    	SI demanda = 0 ENTONCES
							vogel.drop(indice_val_min)
						SI NO ENTONCES
							vogel.drop(indice_pen_col_sol)
				    SI NO ENTONCES
				    	ESCRIBIR 'Buscara por columna', indice_pen_ren
					indice_val_min <- vogel[indice_pen_ren]
					oferta <- vogel[indice_val_min,:][-2]
					demanda <- vogel[indice_pen_ren][-2:-1].values[0]
					SI demanda != 0 AND oferta != 0 ENTONCES
						SI oferta > demanda ENTONCES
							ESCRIBIR 'oferta > demanda'
							fun_obj <- func_obj +  (vogel[indice_pen_ren][indice_val_min] * demanda)
                        vogel_sol[indice_pen_ren][indice_val_min] <- demanda
                        vogel[indice_pen_ren][-2:-1].values[0] <- 0
                        vogel[indice_val_min,-2] <- vogel[list(vogel.index).index(indice_val_min),-2] - demanda
                        vogel[indice_pen_ren].iloc[-1] <- 0
                        vogel.drop(indice_pen_ren)
					         SI NO ENTONCES
						 	ESCRIBIR 'demanda < oferta'
							fun_obj <- func_obj + (vogel[indice_pen_ren][indice_val_min] * oferta)
                        vogel_sol[indice_pen_ren][indice_val_min] <- oferta
                        vogel[indice_val_min,-2] <- 0
                        vogel[indice_pen_ren][-2:-1].values[0] <- vogel[indice_pen_ren][-2:-1].values[0] - oferta
                        vogel[indice_pen_ren] <- 0
                        vogel.drop(indice_val_min)
					SI NO ENTONCES
						SI demanda = 0 ENTONCES
							vogel.drop(indice_pen_ren)
						SI NO ENTONCES
							vogel.drop(indice_val_min)
	ESCRIBIR '*********************'
	ESCRIBIR 'Funcion objetivo: ', fun_obj
	ESCRIBIR vogel_sol
	
	vogel <- LEER (vogel.csv)
	vogel <- LEER (vogel.csv)
	
	vogel_sol <- vogel[:-1]
	vogel_col <- vogel_sol[:,:-1]
	
	n_col <- vogel_sol.shape[1] - 1
	n_ren <- vogel_sol.shape[0] - 1
	optimiza_met <- True
	primera_ite <- 0
	ESCRIBIR 'Solucion inicial'
	MIENTRAS optimiza_met HACER
		SI primera_ite = 0 ENTONCES
		    matriz <- vogel_sol[:-1,:-1].to_numpy()
		    matriz <- matriz.astype('float')
		    matriz[matriz = 0] <- 'nan' 
		    matriz_no_bas <- matriz
		    matriz_circuito <- matriz
		    matriz_costo <- vogel[:-1,:-1].to_numpy()
		SI NO ENTONCES
		    matriz <- matriz_circuito
		    matriz_no_bas <- matriz
		    matriz_circuito <- matriz
		primera_ite <- primera_ite + 1
		
		PARA i HASTA n_ren HACER
		ls_u <- i
		FINPARA
	
		PARA i HASTA n_col HACER
		ls_v <- i
		FINPARA
		
		ren <- 1
		col <- 1
		bandera <- 0 
		ls_u[0] <- 0
		ls_basicas <- []
		 PARA ren <- 0 HASTA n_ren HACER
        		PARA col <- 0 HASTA n_col HACER
            			SI not math.isnan(matriz[ren][col]) ENTONCES
                			ls_basicas.append((ren, col))
                			SI not math.isnan(ls_u[ren]) AND math.isnan(ls_v[col]) ENTONCES
                    				ls_v[col] <- matriz_costo[ren][col] - ls_u[ren]                    
                			SINO SI math.isnan(ls_u[ren]) AND not math.isnan(ls_v[col]) ENTONCES
                   		 		ls_u[ren] <- matriz_costo[ren][col] - ls_v[col]
					FINSI
				FINSI
        		FINPARA
    		FINPARA
		
		PARA ren <- 0 HASTA len(ls_u) HACER
        		SI math.isnan(ls_u[ren]) ENTONCES
            			PARA col <- 0 HASTA n_col HACER
                			SI not math.isnan(matriz[ren][col]) ENTONCES
                    				ls_v[col] <- matriz_costo[ren][col] - ls_u[ren]   
					FINSI
				FINPARA
			FINSI               
    		FINPARA
		
		PARA col <- 0 HASTA len(ls_v) HACER
        		SI math.isnan(ls_v[col]) ENTONCES
            			PARA ren <- 0 HASTA n_ren HACER
                			SI not math.isnan(matriz[ren][col]) ENTONCES
                    				ls_v[col] <- matriz_costo[ren][col] - ls_u[ren]      
					FINSI                    
            			FINPARA
			FINSI
		FINPARA
		
		r_entrada <- 0
		c_entrada <- 0 
		entrada <- -1000
		demanda <- []
		oferta <- []
		PARA ren <- 0 HASTA n_ren HACER
        		PARA col <- 0 HASTA n_col HACER
            			SI math.isnan(matriz_no_bas[ren][col]) ENTONCES
               				matriz_no_bas[ren][col] <- ls_u[ren] + ls_v[col] - matriz_costo[ren][col]
               				SI matriz_no_bas[ren][col] > entrada ENTONCES
					   entrada <- matriz_no_bas[ren][col]
					   r_entrada <- ren
					   c_entrada <- col   
               				FINSI
            			SI NO ENTONCES
                			matriz_no_bas[ren][col] <- 0
            			FINSI
			FINPARA
		FINPARA
	    	SI entrada < 0 ENTONCES
        		optimiza_met <- False
        		break
    		FINSI
		
		circuito <- False
		ban_cir <- 0
		ls_circuito <- []
		
		r_e <- r_entrada
		c_e <- c_entrada
		
		ls_aux <- ls_basicas
		ls_basicas.append((r_entrada, c_entrada))
		ls_basicas_clone <- ls_basicas
						
						
<!-- concepto prueba -->

	matriz_circuito2 <- matriz
	    matriz_circuito2[r_entrada][c_entrada] <- 1
	    ban_cir_t <- False
	    PARA c <- 0, n <- 4 HASTA enumerate(len(ls_basicas)+1) HACER
		comb <- itertools.combinations([c PARA c <- 0, i <- 0 HASTA enumerate(ls_basicas) FINPARA], n )
                                         
        PARA com <- 0 HASTA comb HACER
            
			SI len(list(com)) % 2 = 0 
				criterio <- len(list(com))
			SI NO ENTONCES 
				criterio <- len(list(com)) - 1 
			FINSI
                                      
            SI len(ls_basicas)-1 in list(com) ENTONCES
                ord_circuito, costo_cir <- encuentra_circuito2(list(com), ls_basicas)
                num_extremos <- 0
                PARA i HASTA ord_circuito HACER
                    SI isextremo(matriz_circuito2, ls_basicas[i][0], ls_basicas[i][1]) ENTONCES
                       num_extremos = num_extremos + 1 
                    FINSI
                FINPARA
                SI costo_cir = criterio AND num_extremos>=4 ENTONCES
                    camino <- list(com)
                    ban_cir_t <- True
                    break
				FINSI
			FINSI
        FINPARA
        SI ban_cir_t ENTONCES
            break
        FINSI
    FINPARA
	
    ini <- ord_circuito.index(len(ls_basicas)-1)
    camino <- ord_circuito[ini:] + ord_circuito[0:ini]
    l_theta <- []
    l_theta_p <- []
    
    signos <- 1
    ban_alt <- False
    PARA c <- 0, i <- 0 HASTA enumerate(camino) HACER
        ren <- ls_basicas[i][0]
        col <- ls_basicas[i][1]
        SI c = 0 ENTONCES
            matriz_circuito[ren][col] <- 100000
        SI NO ENTONCES
            SI signos % 2 != 0 ENTONCES
                SI isextremo(matriz_circuito2, ren, col):
                    SI matriz_circuito[ren][col] = 0 ENTONCES
                        ban_alt <- True
                    FINSI
                    l_theta.append(matriz_circuito[ren][col])
                    signos = signos + 1
                FINSI
            SI NO ENTONCES
                SI isextremo(matriz_circuito2, ren, col):
                    l_theta_p.append(matriz_circuito[ren][col])
                    signos = signos + 1
				FINSI
			FINSI
        FINSI
    FINPARA
    theta <- min(l_theta)

    matriz_circuito2 <- matriz
    matriz_circuito2[r_entrada][c_entrada] <- theta
    signos <- 1
    PARA c <- 0, i <- 0 HASTA enumerate(camino) HACER
        ren <- ls_basicas[i][0]
        col <- ls_basicas[i][1]
        SI c = 0 ENTONCES
            matriz_circuito[ren][col] <- theta
        SI NO ENTONCES
            SI signos % 2 != 0 ENTONCES
                SI isextremo(matriz_circuito2, ren, col) ENTONCES
                    matriz_circuito[ren][col] = matriz_circuito[ren][col] -  theta                                                 
                    signos += 1
                FINSI
            SI NO ENTONCES
                SI isextremo(matriz_circuito2, ren, col) ENTONCES                                                
                    matriz_circuito[ren][col] = matriz_circuito[ren][col] + theta
                    signos += 1
				FINSI
			FINSI
		FINSI
    FINPARA
    ban_for <- False
        
    PARA ren <- 0 HASTA n_ren HACER
        PARA col <- 0 n_col HACER
            SI matriz_circuito[ren][col] = 0 ENTONCES
                matriz_circuito[ren][col] <- 'nan'
                ban_for <- True                        
                break
            FINSI
        FINPARA
        SI ban_for ENTONCES
               FINPARA
            break
        FINSI
	FINPARA
	ENDWHILE

	fun_obj2 <- 0
	PARA ren <- 0 HASTA n_ren HACER
	    PARA col <- 0 HASTA n_col HACER
		SI not math.isnan(matriz[ren][col]) ENTONCES
		    fun_obj2 = fun_obj2 + (matriz[ren][col] * matriz_costo[ren][col])
		FINSI
		FINPARA
	FINPARA
	ESCRIBIR 'Funcion Objetivo:: ', fun_obj2
	ESCRIBIR matriz
