
class Carta:

    listaDePalos = ["Tréboles", "Diamantes", "Corazones", "Picas"]

    listaDeValores = ["nada", "As", "2", "3",
     "4", " 5", " 6", " 7", " 8", " 9", " 10", " Sota", " Reina", " Rey"] 


    def __str__(self):
        return ((self.listaDeValores[self.valor] ) + " de " +   self.listaDePalos[self.palo] )

    def __init__(self, palo = 0, valor = 0):
        self.palo = palo
        self.valor = valor

#COMPARAR VALORES DE LOS PALOS
    def __cmp__(self, otro):
        #CONTROLAR EL PALO
        if self.palo > otro.palo: return 1
        if self.palo < otro.palo: return -1
        #SI SON DEL MISMO PALO. CONTROLAR EL VALOR
        if self.valor > otro.valor: return 1
        if self.valor < otro.valor: return -1
        #SI LOS VALORES SON IGUALES, ES EMPATE
        return 0

class Mazo:

    def __str__(self):
        s = "La mano de " + self.nombre
        if self.estaVacio():
            s = s + "está vacía \n"
        else:
            s = s + "contiene \n"
        return s + Mazo.__str__(self)



    def __init__(self):
        self.cartas = []
        for palo in range(4):
            for valor in range(1, 14):
                self.cartas.append(Carta(palo, valor))

    def __str__(self):
        s = " "
        for i in range(len(self.cartas)):
            s = s + " " + (str(self.cartas[i])) + "\n"
        return s

    def mezclar(self):
        import random
        nCartas = len(self.cartas)
        for i in range(nCartas):
            j = random.randrange(i, nCartas)
            self.cartas[i], self.cartas[j] =  self.cartas[i], self.cartas[j]

    def elimaCarta(self, carta):
        if carta in self.cartas:
            self.cartas.remove(carta)
            return 1
        else:
            return 0
    
    def darCarta(self):
        return self.cartas.pop()

    def estaVacio(self):
        return (len(self.cartas) == 0)

    def repartir(self, manos, nCartas= 999):
        nManos= len(manos)
        for i in range(nCartas):
            if self.estaVacio(): break
            carta = self.darCarta()
            mano = manos[i % nManos]
            mano.agregaCarta(carta)
            
class Mano(Mazo):
    def __init__(self, nombre=""):
        self.cartas = []
        self.nombre = nombre

    def agregaCarta(self, carta):
        self.cartas.append(carta)

class JuegoDeCartas:
    def __init__(self):
        self.mazo = Mazo()
        self.mazo.mezclar()

        

class ManoDeLaMona(Mano):
    def eliminaCoincidencias(self):
        cant = 0
        cartasOriginales = self.cartas[:]
        for carta in cartasOriginales:
            empareja = Carta(3 - carta.palo, carta.valor)
            if empareja in self.cartas:
                self.cartas.remove(carta)
                self.cartas.remove(empareja)
                print("Mano %s: %s con %S" %(self.nombre,carta,empareja))
                cant = cant + 1
        return cant
class JuegoDeLaMona(JuegoDeCartas):
    def jugar(self, nombres):
        self.mazo.eliminaCarta(Carta(0, 12))

        self.manos = []
        for nombre in nombres:
            self.manos.apped(ManoDeLaMona(nombre))
        
        self.mazo.repetir(self.manos)
        print("-------Se han repartido las cartas")
        self.muestraManos()

        emparejadas = self.eliminaTodasLasCoincidencias()
        print("------Coincidencias eliminadas, el juego comienza")
        self.muestraManos()

        turno = 0
        cantManos = len(self.manos)
        while emparejadas < 25:
            emparejadas = emparejadas + self.JugarUnTurno(turno)
            turno = (turno + 1 ) % cantManos

        print("------El juego terminó")
        self.muestraManos()


    def eliminaTodasLasCoincidencias(self):
        cant = 0
        for mano in self.manos:
            cant = cant + mano.eliminaCoincidencias()
        return cant






mazo1 = Mazo()
mazo1.mezclar()
 
juego = JuegoDeCartas()
mano = ManoDeLaMona("hugo")
juego.mazo.repartir([mano], 13)
mano.eliminaCoincidencias()
#mano = Mano("hugo")
#mazo1.repartir([mano], 5)

print("La mano de Hugo contiene: \n", mano)












"""carta1= Carta(1,11)

#carta1.listaDePalos[1]  = "Ballenas Bailarinas"
print(carta1)

carta2 = Carta(1,3)
print(carta2)"""