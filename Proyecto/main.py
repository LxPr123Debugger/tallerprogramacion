# Importa la clase GestionFlota desde el módulo Servicios.Gestion_Flota
# Esto permite usar todas las funcionalidades de gestión de flota
from Servicios.Gestion_Flota import GestionFlota


# Definición de la función menu()
# Esta función muestra la interfaz principal del sistema SIGEF
def menu():

    # Crea una instancia del sistema de gestión de flota
    # Este objeto contiene todos los métodos para administrar vehículos
    sistema = GestionFlota()

    # Bucle infinito que mantiene el programa ejecutándose
    # Solo se detiene cuando el usuario elige la opción 5 (Salir)
    while True:

        # Bloque try para manejar errores (excepciones)
        # Evita que el programa se cierre si el usuario ingresa datos incorrectos
        try:

            # Muestra el encabezado del sistema
            print("\n============================")
            print("       SISTEMA SIGEF")
            print("============================")
            
            # Muestra las opciones disponibles para el usuario
            print("1. Registrar vehículo")
            print("2. Actualizar kilometraje")
            print("3. Registrar combustible")
            print("4. Mostrar vehículos")
            print("5. Salir")

            # Solicita al usuario que ingrese una opción
            # int() convierte el texto ingresado a número entero
            # Si el usuario ingresa texto no numérico, genera una excepción ValueError
            opcion = int(input("Seleccione una opción: "))

            # Estructura condicional para ejecutar la opción seleccionada
            # Cada opción llama al método correspondiente del objeto sistema
            
            # Opción 1: Registrar un nuevo vehículo
            if opcion == 1:
                sistema.registrar_vehiculo()

            # Opción 2: Actualizar kilometraje de un vehículo existente
            elif opcion == 2:
                sistema.actualizar_kilometraje()

            # Opción 3: Registrar carga de combustible a un vehículo
            elif opcion == 3:
                sistema.registrar_combustible()

            # Opción 4: Mostrar todos los vehículos registrados
            elif opcion == 4:
                sistema.mostrar_vehiculos()

            # Opción 5: Salir del sistema
            elif opcion == 5:
                print("Saliendo del sistema...")
                break  # Rompe el bucle while y termina el programa

            # Si el usuario ingresa un número diferente a 1-5
            else:
                print("Opción inválida.")

        # Captura específicamente errores de valor (cuando no se ingresa un número)
        # Por ejemplo: si el usuario escribe "hola" en lugar de un número
        except ValueError:
            print("Debe ingresar un número válido.")

        # Captura cualquier otro tipo de error inesperado
        # Esto evita que el programa se cierre por errores desconocidos
        except Exception as e:
            print("Error inesperado:", e)


# Este bloque verifica si el archivo se está ejecutando directamente
# Si es así, llama a la función menu() para iniciar el programa
# Esto permite que el archivo pueda ser importado sin ejecutar el menú automáticamente
if __name__ == "__main__":
    menu()