"""
Andrés Enrique Jaime de la Rosa 763799
"""

# Declaraciones
vocales = "aeiouáéíóú"

# Entradas
palabra = input("Introduzca una palabra ")

# Proceso
if palabra[0].lower() in vocales:
    print(palabra,"comienza con vocal")
else:
    print(palabra,"no comienza con vocal")
