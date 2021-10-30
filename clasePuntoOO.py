class Punto:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return ("" + str(self.x) + ','+ str(self.y) + "" )

    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)

    def __sub__(self, otro1):
        return Punto(self.x - otro1.x, self.y - otro1.y)

    def __mul__(self, otro):
        return Punto(self.x * otro.x, self.y * otro.y)

    def __rmul__(self, otro):
        return Punto(otro * self.x, otro * self.y)

    





p = Punto(3, 4)

p1 = Punto(5, 7)

p3 = p + p1
p4 = p - p1

p5 = p * p1

p6 = 2 * p1

print(p3)

print(p4)

print(p5)

print(p6)
