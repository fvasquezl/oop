from dataclasses import asdict, dataclass, field
from datetime import datetime
from random import randint
from typing import List

from reserva import Reserva
from vuelo import Vuelo
from tabulate import tabulate


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

    sistema_reservas = SistemaReservas([vuelo1, vuelo2])

    # # Crear reservaciones
    reservacion1 = sistema_reservas.create_reservation(
        "Juan Pérez", vuelo1, sistema_reservas
    )
    reservacion2 = sistema_reservas.create_reservation(
        "María González", vuelo2, sistema_reservas
    )

    # print(reservacion1)
    # print(reservacion2)

    vuelos = SistemaReservas.get_todos_los_vuelos(sistema_reservas)

    # reservaciones_vuelo1 = SistemaReservas.get_reservaciones_por_vuelo(
    #     vuelo1, sistema_reservas
    # )
    # print(f"Reservaciones para el vuelo {vuelo1.no_vuelo}")
    # for reservacion in reservaciones_vuelo1:
    #     print(reservacion)
