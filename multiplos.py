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

if numero2==0:
    print("No se puede hacer una división entre 0")

else:
    residuo=numero1 % numero2
    if residuo==0:
# Salidas
        print("El", numero1, "es múltiplo de", numero2)
    else:
        print("Ninugno de los números es múltiplo de otro.")

