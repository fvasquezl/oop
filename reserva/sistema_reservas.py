from dataclasses import asdict, dataclass, field
from datetime import datetime
from random import randint
from typing import List

from reserva import Reserva
from vuelo import Vuelo
from tabulate import tabulate
from collections import defaultdict


@dataclass
class SistemaReservas:
    vuelos: List[Vuelo] = field(default_factory=list)
    reservaciones: List[Reserva] = field(default_factory=list)

    @classmethod
    def create_reservation(
        cls, pasajero: str, vuelo: Vuelo, s_reservas: "SistemaReservas"
    ) -> Reserva:
        asiento = randint(1, vuelo.no_asientos)
        reservacion = Reserva(pasajero=pasajero, vuelo=vuelo, asiento=asiento)
        s_reservas.reservaciones.append(reservacion)
        vuelo.no_asientos -= 1
        return reservacion

    @classmethod
    def get_reservaciones_por_vuelo(
        cls, vuelo: Vuelo, s_reservas: "SistemaReservas"
    ) -> List[Reserva]:
        reservaciones_vuelo = []
        for reservacion in s_reservas.reservaciones:
            if reservacion.vuelo == vuelo:
                reservaciones_vuelo.append(reservacion)
        return reservaciones_vuelo

    @classmethod
    def get_todos_los_vuelos(cls, s_reservas: "SistemaReservas") -> List[Vuelo]:
        headers = []
        data = []
        if s_reservas.vuelos:
            headers = list(asdict(s_reservas.vuelos[0]).keys())
        for vuelo in s_reservas.vuelos:
            data.append(list(asdict(vuelo).values()))

        print(tabulate(data, headers=headers))

    @classmethod
    def crear_reservacion_manual(cls, s_reservas: "SistemaReservas") -> None:
        # Solicitar información al usuario
        nombre_pasajero = input("Ingrese el nombre del pasajero: ")
        no_vuelo = int(input("Ingrese el número de vuelo: "))

        # Buscar el vuelo correspondiente
        vuelo = next((v for v in s_reservas.vuelos if v.no_vuelo == no_vuelo), None)

        if vuelo:
            if vuelo.no_asientos > 0:
                # Crear la reservación
                reservacion = cls.create_reservation(nombre_pasajero, vuelo, s_reservas)
                print(
                    f"Reservación creada exitosamente para el vuelo {vuelo.no_vuelo} con el asiento {reservacion.asiento}"
                )
            else:
                print(
                    f"Lo sentimos, el vuelo {vuelo.no_vuelo} no tiene asientos disponibles."
                )
        else:
            print(f"No se encontró un vuelo con el número {no_vuelo}.")

    @classmethod
    def listar_reservaciones_por_vuelo(cls, s_reservas: "SistemaReservas") -> None:
        # Crear un diccionario para almacenar los pasajeros por vuelo
        pasajeros_por_vuelo = defaultdict(list)
        for vuelo in s_reservas.vuelos:
            for reservacion in s_reservas.reservaciones:
                print(reservacion.vuelo)

        # Iterar sobre las reservaciones y agruparlas por vuelo
        # for reservacion in s_reservas.reservaciones:
        #     # print(reservacion.vuelo.no_vuelo)
        #     pasajeros_por_vuelo[
        #         (
        #             reservacion.vuelo.no_vuelo,
        #             reservacion.vuelo.origen,
        #             reservacion.vuelo.destino,
        #         )
        #     ].append(reservacion.pasajero)

        # # # Imprimir los vuelos y sus pasajeros
        # for vuelo_info, pasajeros in pasajeros_por_vuelo.items():
        #     no_vuelo, origen, destino = vuelo_info
        #     print(f"Vuelo {no_vuelo}: {origen} -> {destino}")
        #     print("\nPasajeros:")
        #     headers = ["Nombre"]
        #     data = [[pasajero] for pasajero in pasajeros]
        #     print(tabulate(data, headers=headers, tablefmt="grid"))
        #     print()


if __name__ == "__main__":

    vuelo1 = Vuelo.create_vuelo(
        no_vuelo=1234,
        origen="Ciudad de México",
        destino="Cancún",
        fecha_salida=datetime(2023, 6, 1, 8, 0),
        fecha_llegada=datetime(2023, 6, 1, 10, 30),
        no_asientos=150,
    )

    vuelo2 = Vuelo.create_vuelo(
        no_vuelo=5678,
        origen="Cancún",
        destino="Monterrey",
        fecha_salida=datetime(2023, 6, 2, 12, 0),
        fecha_llegada=datetime(2023, 6, 2, 14, 30),
        no_asientos=100,
    )

    vuelo3 = Vuelo.create_vuelo(
        no_vuelo=9876,
        origen="Tijuana",
        destino="Puebla",
        fecha_salida=datetime(2023, 6, 3, 12, 0),
        fecha_llegada=datetime(2023, 6, 3, 14, 30),
        no_asientos=100,
    )

    sistema_reservas = SistemaReservas([vuelo1, vuelo2, vuelo3])

    # # Crear reservaciones
    reservacion1 = sistema_reservas.create_reservation(
        "Juan Pérez", vuelo1, sistema_reservas
    )
    reservacion2 = sistema_reservas.create_reservation(
        "María González", vuelo2, sistema_reservas
    )
    reservacion3 = sistema_reservas.create_reservation(
        "Faustino Vasquez", vuelo1, sistema_reservas
    )

    # print(reservacion1)
    # print(reservacion2)

    # vuelos = SistemaReservas.get_todos_los_vuelos(sistema_reservas)

    # SistemaReservas.crear_reservacion_manual(sistema_reservas)

    SistemaReservas.listar_reservaciones_por_vuelo(sistema_reservas)

    # reservaciones_vuelo1 = SistemaReservas.get_reservaciones_por_vuelo(
    #     vuelo1, sistema_reservas
    # )
    # print(f"Reservaciones para el vuelo {vuelo1.no_vuelo}")
    # for reservacion in reservaciones_vuelo1:
    #     print(reservacion)
