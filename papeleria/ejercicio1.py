class Articulo:
    def __init__(self, tipo, marca, hojas_o_tipo, precio_compra):
        self.tipo = tipo
        self.marca = marca
        self.hojas_o_tipo = hojas_o_tipo
        self.precio_compra = precio_compra
        self.precio_venta = self.calcular_precio_venta()
    
    def calcular_precio_venta(self):
        return round(self.precio_compra * 1.30, 2)

    def mostrar_informacion(self):
        return f"Tipo: {self.tipo}, Marca: {self.marca}, " \
               f"Característica: {self.hojas_o_tipo}, " \
               f"Precio de Compra: ${self.precio_compra}, " \
               f"Precio de Venta: ${self.precio_venta}"

# Función para registrar un cuaderno
def registrar_cuaderno():
    marca = "HOJITAS"
    hojas = input("Ingrese el número de hojas del cuaderno (50 o 100): ")
    precio_compra = float(input(f"Ingrese el precio de compra del cuaderno de {hojas} hojas: "))
    return Articulo(tipo="Cuaderno", marca=marca, hojas_o_tipo=f"{hojas} hojas", precio_compra=precio_compra)

# Función para registrar un lápiz
def registrar_lapiz():
    marca = "RAYAS"
    tipo_lapiz = input("Ingrese el tipo de lápiz (Grafito o Colores): ").capitalize()
    precio_compra = float(input(f"Ingrese el precio de compra del lápiz {tipo_lapiz}: "))
    return Articulo(tipo="Lápiz", marca=marca, hojas_o_tipo=tipo_lapiz, precio_compra=precio_compra)

# Función para mostrar la información de los artículos
def mostrar_articulos(articulos):
    if articulos:
        print("\nArtículos registrados:")
        for articulo in articulos:
            print(articulo.mostrar_informacion())
    else:
        print("No hay artículos registrados.")

def menu():
    articulos_registrados = []

    while True:
        print("\n--- Menú de Opciones ---")
        print("1. Registrar cuaderno")
        print("2. Registrar lápiz")
        print("3. Mostrar artículos registrados")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            cuaderno = registrar_cuaderno()
            articulos_registrados.append(cuaderno)
        elif opcion == "2":
            lapiz = registrar_lapiz()
            articulos_registrados.append(lapiz)
        elif opcion == "3":
            mostrar_articulos(articulos_registrados)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

menu()
