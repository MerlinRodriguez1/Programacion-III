class Vehiculo:
    def __init__(self, tipo, nacionalidad, precio_compra):
        self.tipo = tipo
        self.nacionalidad = nacionalidad
        self.ruedas = 4
        self.capacidad_pasajeros = 5
        self.caracteristicas = []
        self.precio_compra = precio_compra
        self.precio_venta = self.calcular_precio_venta()
    
    def calcular_precio_venta(self):
        return round(self.precio_compra * 1.40, 2)

    def agregar_caracteristicas(self):
        print("Ingrese las 10 principales características del vehículo:")
        for i in range(10):
            while True:
                try:
                    caracteristica = input(f"Característica {i + 1}: ").strip()
                    if caracteristica:
                        self.caracteristicas.append(caracteristica)
                        break
                    else:
                        print("La característica no puede estar vacía. Inténtelo de nuevo.")
                except Exception as e:
                    print(f"Error: {e}. Inténtelo de nuevo.")

    def mostrar_informacion(self):
        caracteristicas_str = ', '.join(self.caracteristicas)
        return (f"Tipo: {self.tipo}, Nacionalidad: {self.nacionalidad}, Ruedas: {self.ruedas}, "
                f"Capacidad para Pasajeros: {self.capacidad_pasajeros}, Características: {caracteristicas_str}, "
                f"Precio de Compra: ${self.precio_compra}, Precio de Venta: ${self.precio_venta}")

def solicitar_entrada(mensaje, tipo_dato, valor_default=None):
    while True:
        try:
            entrada = input(mensaje)
            if entrada == '' and valor_default is not None:
                return valor_default
            valor = tipo_dato(entrada)
            if tipo_dato == float and valor < 0:
                raise ValueError("El valor no puede ser negativo.")
            return valor
        except ValueError as ve:
            print(f"Error: {ve}. Inténtelo de nuevo.")
        except Exception as e:
            print(f"Error: {e}. Inténtelo de nuevo.")

def registrar_vehiculo():
    tipo = solicitar_entrada("Ingrese el tipo de vehículo ( Sedan, SUV, Pickup): ", str)
    nacionalidad = solicitar_entrada("Ingrese la nacionalidad del vehículo (Nacional o Importado): ", str).capitalize()
    while nacionalidad not in ("Nacional", "Importado"):
        print("Nacionalidad no válida. Debe ser Nacional o Importado.")
        nacionalidad = solicitar_entrada("Ingrese la nacionalidad del vehículo (Nacional o Importado): ", str).capitalize()
    
    precio_compra = solicitar_entrada("Ingrese el precio de compra del vehículo: ", float)
    
    vehiculo = Vehiculo(tipo=tipo, nacionalidad=nacionalidad, precio_compra=precio_compra)
    vehiculo.agregar_caracteristicas()
    
    return vehiculo

def mostrar_vehiculos(vehiculos):
    if vehiculos:
        vehiculos_info = [f'"{vehiculo.mostrar_informacion()}"' for vehiculo in vehiculos]
        return ', '.join(vehiculos_info)
    else:
        return "No hay vehículos registrados."

def menu():
    vehiculos_registrados = []

    while True:
        print("\n--- Menú de Opciones ---")
        print("1. Registrar vehículo")
        print("2. Mostrar vehículos registrados")
        print("3. Salir")
        
        opcion = solicitar_entrada("Seleccione una opción: ", int)
        
        if opcion == 1:
            vehiculo = registrar_vehiculo()
            vehiculos_registrados.append(vehiculo)
        elif opcion == 2:
            vehiculos_info = mostrar_vehiculos(vehiculos_registrados)
            print("\nVehículos registrados:")
            print(vehiculos_info)
        elif opcion == 3:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

menu()
