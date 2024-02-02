#Crea una clase llamada "Estudiante" con atributos como nombre, edad y calificación. Implementa un método en la clase para 
#verificar si el estudiante ha aprobado o no (calificación mayor o igual a 60).

print("\n******* Bienvenido Usuario *******\n")
#Crear clase
class Estudiante:
    def __init__(self):
        self.nombre_E = None
        self.edad = None
        self.calificacion = None

    def ingresar_nombre(self):
        self.nombre_E = input("Ingrese el nombre del estudiante: ")

    def ingresar_edad(self):
        self.edad = int(input("Ingrese la edad del estudiante: "))

    def ingresar_calificacion(self):
        self.calificacion = int(input("Ingrese la calificación del estudiante: "))

    #Condicion 
    def ha_aprobado(self):
        return self.calificacion >= 60

# Crear una instancia de la clase Estudiante
estudiante = Estudiante()

# Ingresar los datos del estudiante
estudiante.ingresar_nombre()
estudiante.ingresar_edad()
estudiante.ingresar_calificacion()

# Imprimir los datos del estudiante y verificar si ha aprobado o no ha aprobabo
print("\nDatos del estudiante:")
print("Nombre:", estudiante.nombre_E)
print("Edad:", estudiante.edad)
print("Calificación:", estudiante.calificacion)
if estudiante.ha_aprobado():
    print("¿Ha aprobado el estudiante? Sí")
    print("!!MUCHAS FELICITACIONES SIGA ASI¡¡")
else:
    print("¿Ha aprobado el estudiante? No")
    print("NO SE DESANIME , VUELVA A INTENTAR¡¡")

print("\n*********************************************")