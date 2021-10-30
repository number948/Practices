class Rectangulo:
    pass

class Punto:
    pass


# instanciando la clase
caja = Rectangulo()
caja.anchura = 100.0 #atributo
caja.altura = 200.0 #atributo

caja.anchura = caja.anchura + 50
caja.altura = caja.altura + 100

caja.esquina = Punto()
caja.esquina.x = 0.0;
caja.esquina.y = 0.0;

def encuentraCentro(caja):
    p = Punto()
    p.x = caja.esquina.x + caja.anchura/2.0
    p.y = caja.esquina.y + caja.altura/2.0
    print(p.x)
    print(p.y)
    return p


centro = encuentraCentro(caja)
#imprimePunto(centro)
print(centro)