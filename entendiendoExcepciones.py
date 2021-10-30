"""
a, b, c = 23, "t", "A"

try:
    resultado = a/b
except ZeroDivisionError:
    print("Error, division por cero.")
except TypeError:
    print("Error en el tipo de dato.")
"""

try:
    x = int(input("Dame un numero"))
    raise NumberError(7)
except :
    print("ese numero no sirve, prueve otra vez")