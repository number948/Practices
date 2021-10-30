def copiaArchivo(archViejo, archNuevo):
    f1 = open("archViejo.txt", "r")
    f2 = open("archNuevo.txt", "w")
    while 1:
        texto = f1.read(5)
        if texto == "":
            break
        f2.write(texto)
    f1.close()
    f2.close()
    return