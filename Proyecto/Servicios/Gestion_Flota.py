# Importa la clase Vehiculo desde el módulo Modelos.Vehiculo
# Esto permite usar la clase Vehiculo definida en otro archivo
from Modelos.Vehiculo import Vehiculo

# Definición de la clase GestionFlota
# Esta clase administra una colección de vehículos y sus operaciones
class GestionFlota:

    # Método constructor - se ejecuta al crear un nuevo objeto GestionFlota
    def __init__(self):

        # Inicializa una lista vacía para almacenar los vehículos
        # Cada vehículo será un objeto de la clase Vehiculo
        self.vehiculos = []

    # Método para registrar un nuevo vehículo en la flota
    # Corresponde al RF-01: Gestión de Inventario de Flota
    def registrar_vehiculo(self):

        # Solicita al usuario ingresar la placa del vehículo
        placa = input("Ingrese la placa: ")
        
        # Solicita al usuario ingresar la marca del vehículo
        marca = input("Ingrese la marca: ")
        
        # Solicita al usuario ingresar el modelo del vehículo
        modelo = input("Ingrese el modelo: ")
        
        # Solicita al usuario ingresar el kilometraje inicial (convertido a float)
        kilometraje = float(input("Ingrese kilometraje inicial: "))

        # Crea un nuevo objeto Vehiculo con los datos ingresados
        vehiculo = Vehiculo(placa, marca, modelo, kilometraje)

        # Agrega el nuevo vehículo a la lista de vehículos
        self.vehiculos.append(vehiculo)

        # Confirma al usuario que el registro fue exitoso
        print("Vehículo registrado correctamente.")

    # Método para actualizar el kilometraje de un vehículo existente
    # Corresponde al RF-02: Control de Kilometraje
    def actualizar_kilometraje(self):

        # Solicita la placa del vehículo a actualizar
        placa = input("Ingrese la placa del vehículo: ")
        
        # Solicita el nuevo kilometraje (convertido a float)
        nuevo_km = float(input("Ingrese el nuevo kilometraje: "))

        # Recorre la lista de vehículos para encontrar el indicado
        for vehiculo in self.vehiculos:

            # Compara la placa ingresada con la placa del vehículo actual
            if vehiculo.placa == placa:

                # Actualiza el atributo kilometraje del vehículo
                vehiculo.kilometraje = nuevo_km

                # Confirma la actualización
                print("Kilometraje actualizado.")
                
                # Sale del método después de encontrar y actualizar
                return

        # Si no encuentra el vehículo después de recorrer toda la lista
        print("Vehículo no encontrado.")

    # Método para registrar carga de combustible a un vehículo
    # Corresponde al RF-04: Gestión de Combustible
    def registrar_combustible(self):

        # Solicita la placa del vehículo
        placa = input("Ingrese la placa del vehículo: ")
        
        # Solicita la cantidad de litros cargados (convertido a float)
        litros = float(input("Ingrese litros de combustible: "))

        # Recorre la lista de vehículos para encontrar el indicado
        for vehiculo in self.vehiculos:

            # Compara la placa ingresada con la placa del vehículo actual
            if vehiculo.placa == placa:

                # Incrementa el atributo combustible del vehículo
                # Usa += para sumar los litros al valor existente
                vehiculo.combustible += litros

                # Confirma el registro de combustible
                print("Combustible registrado.")
                
                # Sale del método después de encontrar y actualizar
                return

        # Si no encuentra el vehículo después de recorrer toda la lista
        print("Vehículo no encontrado.")

    # Método para mostrar todos los vehículos registrados
    # Útil para visualizar el estado de la flota
    def mostrar_vehiculos(self):

        # Verifica si la lista de vehículos está vacía
        # len() devuelve la cantidad de elementos en la lista
        if len(self.vehiculos) == 0:

            # Informa al usuario que no hay vehículos
            print("No hay vehículos registrados.")
            
            # Sale del método sin mostrar nada más
            return

        # Recorre todos los vehículos en la lista
        for vehiculo in self.vehiculos:

            # Imprime un separador visual entre vehículos
            print("\n------------------")
            
            # Llama al método mostrar_info() de cada vehículo
            # Este método está definido en la clase Vehiculo
            vehiculo.mostrar_info()