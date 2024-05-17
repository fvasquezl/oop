from dataclasses import dataclass
from sistema_reservas import SistemaReservas


@dataclass
class Main:
    @staticmethod
    def menu():
        sistema_reservas = SistemaReservas()
        options = {
            1: "Lista de vuelos",
            2: "Lista de reservas",
            3: "Crear reservacion",
            4: "Crear vuelo",
            5: "Vuelos disponibles",
            6: "Salir",
        }
        while True:
            print("\nMenu Principal:")
            for option, description in options.items():
                print(f"[{option}] {description}")
            try:
                choice = int(input("Opcion Seleccionada:"))
                if choice in options:
                    if choice == 6:
                        print("Hasta la vista Baby!")
                        break
                    else:
                        if choice == 1:
                            SistemaReservas.get_todos_los_vuelos(sistema_reservas)
                        elif choice == 2:
                            SistemaReservas.listar_reservaciones_por_vuelo(
                                sistema_reservas
                            )
                        elif choice == 3:
                            SistemaReservas.crear_reservacion_manual(sistema_reservas)
                        elif choice == 4:
                            SistemaReservas.create_vuelo_manual(sistema_reservas)
                else:
                    print("La opcion seleccionada es invalida")

            except ValueError as e:
                print("Please enter a valid number.")
            except Exception as e:
                print(repr(e))


if __name__ == "__main__":

    main = Main()
    main.menu()
