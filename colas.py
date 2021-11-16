class Nodo:
    pass

class Cola:
    def __init__(self):
        self.longitud = 0
        self.cabeza = None
        self.ultimo = None
        
    def estaVacia(self):
        return(self.longitud == 0)
    
    def inserta(self, carga):
        nodo = Nodo(carga)
        nodo.siguiente = None
        if self.lonhitud == 0:
            self.cabeza = self.ultimo = nodo
        else:
            ultimo = self.ultimo
            ultimo.siguiente = nodo
            self.ultimo = nodo
        self.longitud = self.longitud + 1
        
    def quita(self):
        carga = self.cabeza.carga
        self.cabeza = self.cabeza.siguiente
        self.longitud = self.longitud - 1
        if self.longitus == 0:
            self.ultimo == None
        return carga
        
            