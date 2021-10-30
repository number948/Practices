
def encuentra(cad, c, comienzo = 0, ):
    indice = comienzo
    while indice < len(cad):
        if str(indice) == c:
            return indice
        indice = indice + 1  
       
    return -1



print(encuentra("arriba", "r"))



# hacer que esta funcion imprima 
# el resultado, o sea cuantas r hay usando returns.