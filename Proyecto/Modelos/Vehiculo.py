class Vehiculo:

    def __init__(self, placa, marca, modelo, kilometraje):

        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.kilometraje = kilometraje
        self.combustible = 0

    def mostrar_info(self):

        print("Placa:", self.placa)
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Kilometraje:", self.kilometraje)
        print("Combustible registrado:", self.combustible)