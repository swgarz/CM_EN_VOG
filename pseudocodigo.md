# pseudocodigo costo minimo
      
 Inicio
 Leer costo_min  
 
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
              
  
 
 
 # pseudocodigo Esquina Noroeste
 
 # pseudocodigo Vogel
 
 
 
 
 
# Notas
shape Devuelve la dimensión del array, es decir, una tupla de enteros indicando el tamaño del array en cada dimensión. Para una matriz de n filas y m columnas obtendremos (n,m).

axis =1 igual a columna, axis=0 a renglon
