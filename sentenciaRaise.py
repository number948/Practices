def tomaNumero():
    x = input(" elige un numerito: ")
    if x == 17:
        raise ErrorNumeroMalo('17 es un mal numero')
    return x



tomaNumero()
    