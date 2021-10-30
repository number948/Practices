class Hora:
    pass

hora = Hora()
hora.horas = 11
hora.minutos = 59
hora.segundos = 30

def imprimeHora(hora):
    print (str(hora.horas) + ":" + str(hora.minutos) + ":" + str(hora.segundos))



imprimeHora(hora)