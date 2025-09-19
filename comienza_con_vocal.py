"""
Andrés Enrique Jaime de la Rosa 763799
El propósito de este código es determinar si una palábra comienza con una vocal
"""

# Declaraciones
vocales = "aeiouáéíóú"

# Entradas
palabra = input("Introduzca una palabra ")

# Proceso
if palabra[0].lower() in vocales:
    print(f"'{palabra}' comienza con vocal")
else:
    print(f"'{palabra}' no comienza con vocal")
