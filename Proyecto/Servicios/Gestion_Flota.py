from Modelos.Vehiculo import Vehiculo

class GestionFlota:

    def __init__(self):

        self.vehiculos = []

    def registrar_vehiculo(self):

        placa = input("Ingrese la placa: ")
        marca = input("Ingrese la marca: ")
        modelo = input("Ingrese el modelo: ")
        kilometraje = float(input("Ingrese kilometraje inicial: "))

        vehiculo = Vehiculo(placa, marca, modelo, kilometraje)

        self.vehiculos.append(vehiculo)

        print("Vehículo registrado correctamente.")

    def actualizar_kilometraje(self):

        placa = input("Ingrese la placa del vehículo: ")
        nuevo_km = float(input("Ingrese el nuevo kilometraje: "))

        for vehiculo in self.vehiculos:

            if vehiculo.placa == placa:

                vehiculo.kilometraje = nuevo_km

                print("Kilometraje actualizado.")
                return

        print("Vehículo no encontrado.")

    def registrar_combustible(self):

        placa = input("Ingrese la placa del vehículo: ")
        litros = float(input("Ingrese litros de combustible: "))

        for vehiculo in self.vehiculos:

            if vehiculo.placa == placa:

                vehiculo.combustible += litros

                print("Combustible registrado.")
                return

        print("Vehículo no encontrado.")

    def mostrar_vehiculos(self):

        if len(self.vehiculos) == 0:

            print("No hay vehículos registrados.")
            return

        for vehiculo in self.vehiculos:

            print("\n------------------")
            vehiculo.mostrar_info()