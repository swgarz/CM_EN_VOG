# pseudocodigo costo minimo
      
 Inicio
 Leer costo_mindatos
 Bandera <- true
 Fun_obj <- 0
 Mientras bandera sea verdadero 
     Mínimos <- vector de id los valores mínimos
     If mínimos es de tamaño 0 entonces
          Bandera <- false
          Romper ciclo 
 Fin Mientras
 
     minimo <- valor minimo del primer renglon
     count <- 0
     renglon <- 0
     columnas <- minimos[0]
     Repetir para i=1 incremento 1 hasta n
            aux <- minimo del renglon[i]
            Si aux < minimo   
                  renglon <- i
                  columna <- minimos[i]
                  minimo <- aux
     oferta <- valor de oferta del valor mínimo
     demanda <- valor de demanda del valor mínimo
     Si demanda != 0 y oferta != 0 Entonces
      Si oferta > demanda Entonces
            func_obj += oferta por el costo minimo
            costo minimo solucion <- demanda
            columna <- 0
            oferta <- oferta - demanda
            se elimina la columna
       SiNo
            fun_obj += demanda por el costo minimo
            costo minimo solucion <- oferta
            renglon <- 0
            demanda <- demanda - oferta
            se elimina el renglon
       Si el vector minimos [0] == 0 Entonces
            bandera <- False
            Romper ciclo
       SiNo
            Si demanda == 0 Entonces
                  eliminar tabla columnas
            SiNo 
                  elimiar tabla filas
     Escribir costo minimo solucion
     
     Leer datos
     indice en fuentes
     n_col <- costo minimo solucion
     n_ren <- costo minimo
     optimiza_met <- true
     primera_ite <- 0
     Escribir "Solucion inicial"
     Mientras optimiza_met
      Si primera_ite == 0
            matriz <- matriz costo minimo solucion
            matriz <- matriz dato float
            matriz [matriz == 0] <- not a number
            matriz_no_bas <- copia matriz
            matriz_circuito <- copia matriz
      SiNo
            matriz <- copia matriz_circuito
            matriz_no_bas <- copia matriz
            matriz_circuito <- copia matriz
      primera_ite += 1
      
      ls_u <- [np.nan Para i=1 incremento 1 hasta n_ren]
      ls_v <- [np.nan para i=1 incremento 1 hasta n_col]
      ren <- 1
      col <- 1
      bandera <- 0
      ls_u [0] <- 0
      ls_basicas <- []
      Para ren=1 incremento 1 hasta n_ren
            Para col=1 incremento 1 hasta n_col
                  SiNo valor nulo en matriz 
                        valor append a ls_basicas
                        SiNo valor nulo en ls_u y valor nulo en ls_v
                              ls_v <- matriz_costo - ls_u
                        Si valor nulo ls_u y no valor nulo ls_v
                              ls_u <- matriz_costo - ls_v
Para ren=1 incremento 1 hasta tamaño de ls_u
      Si valor nulo en ls_u
            Para col=1 incremento 1 hasta n_col
                  SiNo malor nulo en matriz 
                        ls_v <- matriz_costo - ls_u
 Para col=1 incremento 1 hasta tamaño de ls_v
      Si valor nulo en ls_v
            Para ren=1 incremento 1 hasta n_ren
                  SiNo valor nulo en matriz 
                        ls_v <- matriz_costo - ls_u 
  r_entrada <- 0
  c_entrada <- 0
  entrada <- -1000
  demanda <- []
  oferta <- []
  Para ren=1 incremento 1 hasta n_ren
      Para col=1 incremento 1 hasta n_col
            Si valor nulo en matriz_no_bas Entonces
                  matriz_no_bas <- ls_u + ls_v - matriz_costo
                  Si matriz_no_bas > entrada Entonces
                        entrada <- matriz_no_bas
                        r_entrada <- ren
                        c_entrada <- col
                  SiNo 
                     matriz_no_bas <- 0
   Si entrada < 0 Entonces
      optimiza_met <- false
      Romper ciclo
                        
   circuito <- false
   ban_cir <- 0
   ls_circuito <- []
   r_e <- r_entrada
   c_e <- c_entrada
   ls_aux <- ls_basicas
   valor append a ls_basicas
   ls_basicas_clone <- copia ls_basicas
   n<-4
   ###### concepto prueba
   matriz_circuito2 <- copia matriz
   matriz_circuito2 [r_entrada][c_entrada] <- 1
   ban_cir_t <- false
   Para c=1 n=4 incremento 4 hasta el tamaño de ls_basicas + 1
      
   
              
  
 
 
 # pseudocodigo Esquina Noroeste
 
 # pseudocodigo Vogel
 
