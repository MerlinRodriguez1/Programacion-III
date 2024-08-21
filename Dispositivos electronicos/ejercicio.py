class Dispositivo:
    def __init__(self, tipo, marca, caracteristicas, precio_compra):
        self.tipo = tipo
        self.marca = marca
        self.caracteristicas = caracteristicas
        self.precio_compra = precio_compra
        self.precio_venta = self.calcular_precio_venta()
    
    def calcular_precio_venta(self):
        """Calcula el precio de venta con un margen de ganancia del 70%"""
        return round(self.precio_compra * 1.70, 2)

    def mostrar_informacion(self):
        """Devuelve una cadena con la información del dispositivo"""
        caracteristicas_str = ', '.join(self.caracteristicas)
        return f"Tipo: {self.tipo}, Marca: {self.marca}, Características: {caracteristicas_str}, " \
               f"Precio de Compra: ${self.precio_compra}, Precio de Venta: ${self.precio_venta}"

def registrar_dispositivo():
    """Función para registrar un dispositivo electrónico"""
    tipo = input("Ingrese el tipo de dispositivo (Celular, Tablet, Portátil): ").capitalize()
    while tipo not in ("Celular", "Tablet", "Portátil"):
        print("Tipo de dispositivo no válido. Debe ser Celular, Tablet o Portátil.")
        tipo = input("Ingrese el tipo de dispositivo (Celular, Tablet, Portátil): ").capitalize()
    
    marca = "PHR"
    caracteristicas = []
    print("Ingrese las 6 principales características del dispositivo:")
    for i in range(6):
        caracteristica = input(f"Característica {i + 1}: ")
        caracteristicas.append(caracteristica)
    
    precio_compra = float(input("Ingrese el precio de compra del dispositivo: "))
    
    return Dispositivo(tipo=tipo, marca=marca, caracteristicas=caracteristicas, precio_compra=precio_compra)

def mostrar_dispositivos(dispositivos):
    """Muestra la información de todos los dispositivos registrados"""
    if dispositivos:
        print("\nDispositivos registrados:")
        for dispositivo in dispositivos:
            print(dispositivo.mostrar_informacion())
    else:
        print("No hay dispositivos registrados.")

def menu():
    """Función principal que ejecuta el menú de opciones"""
    dispositivos_registrados = []

    while True:
        print("\n--- Menú de Opciones ---")
        print("1. Registrar dispositivo")
        print("2. Mostrar dispositivos registrados")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            dispositivo = registrar_dispositivo()
            dispositivos_registrados.append(dispositivo)
        elif opcion == "2":
            mostrar_dispositivos(dispositivos_registrados)
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

menu()
