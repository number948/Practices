"""nombreArch = input("Introduce un nombre de archivo ")
try:
    f = open (nombreArch, "r")
except:
    print("No hay ningun archivo que se llame ", nombreArch)  """  

#encapsulado en funcion

def existe(nombreArch):
    nombreArch = input("Introduce un nombre de archivo ")
    try:
        f = open (nombreArch)
        f.close()
        print(1)
        return 1
    except:
        print(0)
        return 0


existe("nombreArch")