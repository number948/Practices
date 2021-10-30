"""A modo de ejercicio, escriba una funcion llamada mueveRect que
tome un Rectangulo y dos parametros llamados dx y dy. Tiene que
cambiar la posicion del rectangulo anadiendo dx a la coordenada x
de esquina y anadiendo dy a la coordenada y de esquina."""

class Rectanghulo:
    pass
class Punto:
    pass

bob = Rectanghulo()
bob.anchura = 100.0
bob.altura = 200.0
bob.esquina = Punto()
bob.esquina.x = 0.0;
bob.esquina.y = 0.0;

dx = 50.0
dy = 10.0
def mueveRect(bob,dx,dy):
    
    bob.esquina.x = bob.esquina.x + dx
    bob.esquina.y = bob.esquina.y + dy
    return #bob.esquina.x and bob.esquina.y
    

def imprime(bob,dx,dy):
    print()


mueveRect(bob,dx,dy)
imprime(bob,dx,dy)

