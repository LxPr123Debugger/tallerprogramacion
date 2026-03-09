from Servicios.Gestion_Flota import GestionFlota


def menu():

    sistema = GestionFlota()

    while True:

        try:

            print("\n============================")
            print("       SISTEMA SIGEF")
            print("============================")
            print("1. Registrar vehículo")
            print("2. Actualizar kilometraje")
            print("3. Registrar combustible")
            print("4. Mostrar vehículos")
            print("5. Salir")

            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                sistema.registrar_vehiculo()

            elif opcion == 2:
                sistema.actualizar_kilometraje()

            elif opcion == 3:
                sistema.registrar_combustible()

            elif opcion == 4:
                sistema.mostrar_vehiculos()

            elif opcion == 5:
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida.")

        except ValueError:
            print("Debe ingresar un número válido.")

        except Exception as e:
            print("Error inesperado:", e)


if __name__ == "__main__":
    menu()