#Define una función que tome dos parámetros y devuelva True si la suma de ambos es par y False si es impar
print("*******Bienvenido Usuario*******\n")

def suma_par(num1, num2):
    suma = num1 + num2
    return suma % 2 == 0

# Ejemplos de uso de la función

resultado1 = suma_par(4, 9)
print("La suma total de 4 y 9 da como resultado un numero par es: ?", resultado1)

resultado2 = suma_par(6, 8)
print("La suma total de 6 y 8 da como resultado un numero par es: ", resultado2)

print("\n")
print("*********************************************")