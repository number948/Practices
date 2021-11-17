class Arbol:
    def __init__(self, carga, izquierda = None, derecha = None):
        self.carga = carga
        self.izquierda = izquierda
        self.derecha = derecha
        
    def __str__(self):
        return str(self.carga)
    
    def imprimeArbol(self,arbol):
        if arbol == None: return
        
        self.imprimeArbol(arbol.izquierda)
        print((arbol.carga))
        self.imprimeArbol(arbol.derecha)
    
    def imprimeArbolSangrado(self,arbol, nivel = 0):
        if arbol == None: return
        self.imprimeArbolSangrado(arbol.derecha, nivel + 1)
        print(' ' * nivel + str(arbol.carga))
        self.imprimeArbolSangrado(arbol.izquierda, nivel + 1)
        
    def tomaToken(listaToken, esperado):
        if listaToken[0] == esperado:
            del listaToken[0]
            return 1
        else:
            return 0
        
    
    
arbol = Arbol('+',Arbol(1),Arbol('*', Arbol(2), Arbol(3)))

#arbol.imprimeArbol(arbol)
arbol.imprimeArbolSangrado(arbol)

