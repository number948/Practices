class Hora:
    pass

t1 = Hora()
t2 = Hora()
suma = Hora()
horaActual = Hora()
horaActual.horas = 9
horaActual.minutos = 14
horaActual.segundos = 30

horaPan = Hora()
horaPan.horas = 3
horaPan.minutos = 35
horaPan.segundos = 0


# creo que falta poner cuanto tarda para el pan y cual es la hora, los atributos de la clase hora que arriba puse en cero +
def sumaHora(t1, t2):
    
    suma.horas = t1.horas + t2.horas
    suma.minutos = t1.minutos + t2.minutos
    suma.segundos = t1.segundos + t2.segundos

    if suma.segundos >= 60:
        suma.segundos = suma.segundos -  60
        suma.minutos = suma.minutos + 1

    if suma.minutos >= 60:
        suma.minutos = suma.minutos - 60
        suma.horas = suma.horas + 1

    return suma

horaHecho = sumaHora(horaActual, horaPan)

def imprimeHora(suma, t1, t2):
    print (str(suma.horas) + ":" + str(suma.minutos) +
     ":" + str(suma.segundos))

imprimeHora(horaHecho,t1, t2)