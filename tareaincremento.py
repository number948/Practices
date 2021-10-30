

class Hora:
    pass

hora = Hora()
#segundos = Hora()
hora.horas = 9
hora.segundos = 3


def incremento(hora, segundos):
    hora.segundos = hora.segundos + segundos

    while hora.segundos >= 60 and hora.minutos >= 60:
        hora.segundos = hora.segundos - 60
        hora.minutos = hora.minutos - 60
        hora.minutos = hora.minutos + 1
        hora.horas = hora.horas + 1

