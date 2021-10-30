import copy

class Punto:
    pass


p1 = Punto()
p1.x = 3
p1.y = 4

p2 = copy.copy(p1)
p1 == p2
