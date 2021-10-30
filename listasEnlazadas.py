class Nodo:
    def __init__(self, carga = None, siguiente = None):
        self.carga = carga
        self.siguiente = siguiente

    def __str__(self):
        return str(self.carga)

    def imprimeLista(self):
        while self:
        
            print(self),
            self = self.siguiente
        


nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)

#nodo1.imprimeLista(nodo1)


# HACIENDO QUE NODOS HAGAN REFERENCIA AL SIGUIENTE:
#  ENLAZANDO LA LISTA DE NODOS

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3


nodo1.imprimeLista()

#print(nodo1)


