# Definición de la clase Vehiculo
# Una clase es como un "molde" para crear objetos que representan vehículos
class Vehiculo:

    # Método constructor - se ejecuta automáticamente al crear un nuevo vehículo
    # self hace referencia al objeto que se está creando
    # Los parámetros son los datos necesarios para crear un vehículo
    def __init__(self, placa, marca, modelo, kilometraje):

        # Asigna la placa recibida al atributo placa del objeto
        self.placa = placa
        
        # Asigna la marca recibida al atributo marca del objeto
        self.marca = marca
        
        # Asigna el modelo recibido al atributo modelo del objeto
        self.modelo = modelo
        
        # Asigna el kilometraje recibido al atributo kilometraje del objeto
        self.kilometraje = kilometraje
        
        # Inicializa el combustible en 0 para el nuevo vehículo
        # Este atributo no se recibe como parámetro, se crea con valor por defecto
        self.combustible = 0

    # Método para mostrar la información del vehículo
    # Este método permite visualizar todos los datos del vehículo
    def mostrar_info(self):

        # Imprime el valor del atributo placa
        print("Placa:", self.placa)
        
        # Imprime el valor del atributo marca
        print("Marca:", self.marca)
        
        # Imprime el valor del atributo modelo
        print("Modelo:", self.modelo)
        
        # Imprime el valor del atributo kilometraje
        print("Kilometraje:", self.kilometraje)
        
        # Imprime el valor del atributo combustible
        print("Combustible registrado:", self.combustible)