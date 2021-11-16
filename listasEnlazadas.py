


class Nodo:
    def __init__(self, carga = None, siguiente = None):
        self.carga = carga
        self.siguiente = siguiente
        

    def __str__(self):
        return str(self.carga)

    def imprimeLista(nodo, self):
        
        while nodo:
            print(nodo),
            nodo = nodo.siguiente
       

    def imprimeAlReves(self,lista):
        if lista == None: 
            return
        self.imprimeAlReves(lista.siguiente)
        print(lista)
        

    def imprimeAlRevesBonito(self,lista):
        print("["),
        if lista != None:
            cabeza = lista
            cola = lista.siguiente
            self.imprimeAlReves(cola)
            print(cabeza)
        print("]"),



    def eliminaSegundo(self, lista):
        if lista == None: return
        primero = lista
        segundo = lista.siguiente
        primero.siguiente = segundo.siguiente
        segundo.siguiente = None
        return segundo
        


nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)

#nodo1.imprimeLista(nodo1)


# HACIENDO QUE NODOS HAGAN REFERENCIA AL SIGUIENTE:
#  ENLAZANDO LA LISTA DE NODOS

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

#nodo1.imprimeLista(nodo1)


"""eliminado = nodo1.eliminaSegundo(nodo1)
nodo1.imprimeAlReves(eliminado)
nodo1.imprimeLista(nodo1)"""
nodo1.imprimeAlRevesBonito(nodo1)

#print(nodo1)


