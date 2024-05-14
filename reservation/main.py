"""
2. **Diseña un sistema de reservas de vuelos**
   - Crea una clase `Vuelo` con atributos como número de vuelo,
    origen, destino, fecha y hora de salida/llegada, y cantidad de asientos disponibles.
   - Crea una clase `Reserva` que represente una reserva para un vuelo específico y contenga información como el nombre del pasajero y el asiento asignado.
   - Implementa una clase `SistemaReservas` que gestione una lista de vuelos y reservas, y permita a los usuarios realizar reservas, cancelarlas y ver los vuelos disponibles.
"""

from dataclasses import asdict, dataclass
from app.vuelo import Vuelo
from app.reserva import Reserva


@dataclass
class Main:
    @staticmethod
    def menu():
        options = {
            1: "Lista de vuelos",
            2: "Lista de reservas",
            3: "Crear reservacion",
            4: "Cancelar reservacion",
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
                            Vuelo.mostrar_vuelos()
                        elif choice == 2:
                            print("Crea Reservacion")
                            reservation = Reserva.create_reservation()
                            print(reservation)
                        elif choice == 3:
                            print("Cancela Reservacion")
                else:
                    print("La opcion seleccionada es invalida")

            except ValueError as e:
                print("Please enter a valid number.")
            except Exception as e:
                print(repr(e))


if __name__ == "__main__":

    vuelo1 = Vuelo(
        no_vuelo=10,
        origen="Tijuana",
        destino="Veracruz",
        fecha="30/09/24",
        hora_salida="9:20",
        hora_llegada="13:00",
        no_asientos=180,
    )

    vuelo2 = Vuelo(
        no_vuelo=11,
        origen="Veracruz",
        destino="Tijuana",
        fecha="30/09/24",
        hora_salida="9:20",
        hora_llegada="13:00",
        no_asientos=190,
    )

    vuelo3 = Vuelo(
        no_vuelo=12,
        origen="Tijuana",
        destino="Puebla",
        fecha="30/09/24",
        hora_salida="9:20",
        hora_llegada="13:00",
        no_asientos=2,
    )
    Vuelo.agregar_vuelo(vuelo1)
    Vuelo.agregar_vuelo(vuelo2)
    Vuelo.agregar_vuelo(vuelo3)

    main = Main()
    main.menu()
