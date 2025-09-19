"""

Christian Alonso Flores Burgos

Fecha
19 de septiembre de 2025

El programa determina si dos valores son múltiplos entre sí.

"""

# Declaraciones
# Entradas
numero1 = int(input("Introduce un número:"))
numero2 = int(input("Introduce otro número:"))

# Proceso
if numero1<numero2:
    numero1, numero2 = numero2, numero1

residuo=numero1 % numero2

# Salidas
if residuo==0:
    print("El", numero1, "y", numero2, "sí son múltiplos.")
else:
    print("El", numero1, "y", numero2, "no son múltiplos.")
