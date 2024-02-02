#Crear un programa que convierta km a millas
print("\n******* Bienvenido Usuario *******\n")

def km_milla(km):
    millas = km * 0.621371
    return millas

try:
    kilometros = float(input("Ingrese la cantidad de kilómetros: "))
    if kilometros > 0:
        millas = km_milla(kilometros)
        print(f"{kilometros} km equivalen a {millas:.3f} millas.")  # Mostrar 3 decimales
    else:
        print("Por favor, ingrese una distancia válida en kilómetros mayor que 0.")
except ValueError:
    print("Dato ingresado no válido¡¡¡¡")

print("\n*********************************************")