
class Perro:
    def __init__(self, nombre, edad, peso, raza, color, propietario, direccion, telefono):
    
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.raza = raza
        self.color = color
        self.propietario = propietario
        self.direccion = direccion
        self.telefono = telefono
        self.estado = "NO ATENDIDO"  
        self.clasificacion = self.clasificar_perro()

    def clasificar_perro(self):
        
        if self.peso < 10:
            return "Perro Pequeño"
        else:
            return "Perro Grande"

    def atender_perro(self):
       
        self.estado = "ATENDIDO"

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Raza: {self.raza}")
        print(f"Color: {self.color}")
        print(f"Propietario: {self.propietario}")
        print(f"Dirección: {self.direccion}")
        print(f"Teléfono: {self.telefono}")
        print(f"Estado: {self.estado}")
        print(f"Clasificación: {self.clasificacion}")

def main():
    print("Registro de Perro en la Veterinaria")
    print("Estado del perro: NO ATENDIDO")  

    nombre = input("Nombre del perro: ")
    edad = int(input("Edad del perro (en años): "))
    peso = float(input("Peso del perro (en kg): "))
    raza = input("Raza del perro: ")
    color = input("Color del perro: ")
    propietario = input("Nombre del propietario: ")
    direccion = input("Dirección del propietario: ")
    telefono = input("Teléfono del propietario: ")

    perro = Perro(nombre, edad, peso, raza, color, propietario, direccion, telefono)

    perro.atender_perro()

    print(f"\nEstado del perro después de ser atendido: {perro.estado}")
    perro.mostrar_informacion()

if __name__ == "__main__":
    main()