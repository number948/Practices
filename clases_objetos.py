class Punto:
    pass

blanco = Punto()

blanco.x = 3.0
blanco.y = 4.0

x = blanco.x

print(x)
print(blanco.y)

#print('+ str(blanco.x) + ',' + str(blanco.y) + ')
distanciaAlCuandrado = blanco.x * blanco.x + blanco.y * blanco.y
print(distanciaAlCuandrado)