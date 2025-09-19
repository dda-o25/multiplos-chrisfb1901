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
if numero2 != 0 and numero1 % numero2 == 0:
    print("El número", numero1, "es múltiplo del",numero2)
elif numero1 != 0 and numero2 % numero1 == 0:
   print("El número", numero2, "es múltiplo del",numero1)
# Salidas 
else:
    print("Ninguno de los números es múltiplo del otro")


    
