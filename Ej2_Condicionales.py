#Crea un programa que determine si un número ingresado por el usuario es positivo, negativo o cero.
print("*******Bienvenido Usuario*******\n")

print("Ingrese un número entero:")
numero = float(input())

print("RESULTADO TOTAL\n")
if numero > 0:
    print("El número ingresado es positivo:", numero)
elif numero < 0:
    print("El número ingresado es negativo:", numero)
else:
    print("El número ingresado es cero:", numero)

print("*********************************************")