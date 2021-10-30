class Punto:
    pass


def mismoPunto(p1,p2):
    return(p1.x == p2.x) and (p1.y == p2.y)


p1 = Punto()
p1.x = 3
p1.y = 4
p2 = Punto()
p1.y = 3
p2.y = 4
print(p1 == p2)
p2 = p1
print(p1 == p2)

