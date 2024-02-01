#Escribe un programa que solicite al usuario ingresar dos números y luego muestre la suma, resta, multiplicación y división de esos números.
print("*******Bienvenido Usuario*******\n")

print("Ingrese un número entero: ")
num1 = int(input())

print("Ingrese un número entero: ")
num2 = int(input())

suma = num1 + num2
resta = num1 - num2
mult = num1 * num2

if num2 != 0:
    div = num1 / num2
    
else:
    print("No se puede dividir entre cero.")

print("RESULTADOS TOTALES")
print("El resultado de la suma es:", suma)
print("El resultado de la resta es:", resta)
print("El resultado de la multiplicación es:", mult)
print("El resultado de la división es:", div)
print("")

print("*********************************************")