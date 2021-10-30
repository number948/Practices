class Hora:
    def imprimeHora(hora):
        print(str(hora.horas) + ":" +
            str(hora.minutos) + ":" +
            str(hora.segundos))
    
    def incremento(self, segundos):
        self.segundos = segundos + self.segundos

        while self.segundos >= 60:
            self.segundos = self.segundos - 60
            self.minutos = self.minutos + 1

        while self.minutos >= 60:
            self.minutos = self.minutos - 60
            self.horas = self.horas + 1


    def convierteASegundos(self,t):
        minutos = t.horas * 60 + t.minutos
        segundos = minutos * 60 + t.segundos
        return segundos

    def haceHora(self, segundos):
        hora = Hora()
        hora.horas = segundos/3600
        segundos = segundos - hora.horas * 3600
        hora.minutos = segundos/60
        segundos = segundos - hora.minutos * 60
        hora.segundos = segundos
        return hora
        
    
    def despues(self, hora2):
    
        if self.horas > hora2.horas:
            return 1
        if self.horas < hora2.horas:
            return 0

        if self.minutos > hora2.minutos:
            return 1

        if self.minutos < hora2.minutos:
            return 0
        if self.segundos > hora2.segundos:
            return 1

        return 0

horaActual = Hora()
horaHecho = Hora()
horaActual.horas = 9
horaActual.minutos = 14
horaActual.segundos = 30

horaActual.imprimeHora()
horaActual.incremento(500)
if horaHecho.despues(horaActual):
    print(" el pan estará hecho después de empezar")