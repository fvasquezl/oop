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

    """
    Este Metodo obtiene una lista de todos los vuelo que se tienen registrados
    """

    @classmethod
    def get_todos_los_vuelos(cls, s_reservas: "SistemaReservas") -> List[Vuelo]:
        headers = []
        data = []
        if s_reservas.vuelos:
            headers = list(asdict(s_reservas.vuelos[0]).keys())
        for vuelo in s_reservas.vuelos:
            data.append(list(asdict(vuelo).values()))

        print(tabulate(data, headers=headers))

    """
    Este Metodo crea una reervacion automaticamente pasando los datos de pasajero y vuelo
    """

    @classmethod
    def create_reservation(
        cls, pasajero: str, vuelo: Vuelo, s_reservas: "SistemaReservas"
    ) -> Reserva:
        asiento = randint(1, vuelo.no_asientos)
        reservacion = Reserva(pasajero=pasajero, vuelo=vuelo, asiento=asiento)
        s_reservas.reservaciones.append(reservacion)
        vuelo.no_asientos -= 1
        return reservacion

    """
    Este Metodo pregunta por los datos de pasajero y vuelo y con ellos crea una reservacion
    """

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

    """
    Este Metodo obtiene una lista de todas las reservaciones que hay en un vuelo
    """

    @classmethod
    def get_reservaciones_por_vuelo(
        cls, vuelo: Vuelo, s_reservas: "SistemaReservas"
    ) -> List[Reserva]:
        reservaciones_vuelo = []
        for reservacion in s_reservas.reservaciones:
            if reservacion.vuelo == vuelo:
                reservaciones_vuelo.append(reservacion)
        return reservaciones_vuelo

    """
    Este metodo lista las reservaciones que tiene cada vuelo
    """

    @classmethod
    def listar_reservaciones_por_vuelo(cls, s_reservas: "SistemaReservas") -> None:
        # Crear un diccionario para almacenar los pasajeros por vuelo
        for vuelo in s_reservas.vuelos:
            reservaciones_vuelo = cls.get_reservaciones_por_vuelo(
                vuelo=vuelo, s_reservas=s_reservas
            )
            if reservaciones_vuelo:
                print(f"\nVuelo {vuelo.no_vuelo}: {vuelo.origen} -> {vuelo.destino}")
                headers = ["Pasajero", "Asiento"]
                data = [[r.pasajero, r.asiento] for r in reservaciones_vuelo]
                print(tabulate(data, headers=headers))
            else:
                print(f"\nEl vuelo {vuelo.no_vuelo} aún no tiene pasajeros.")

    @classmethod
    def create_vuelo_manual(
        cls,
        s_reservas: "SistemaReservas",
    ) -> "Vuelo":
        try:
            no_vuelo = int(input("Ingrese el No de Vuelo: "))
            origen = input("Ingrese el origen: ")
            destino = input("Ingrese el destino: ")
            fecha_salida = datetime.strptime(
                input("Ingrese la fecha de Salida (YYYY-MM-DD HH:MM): "),
                "%Y-%m-%d %H:%M",
            )
            fecha_llegada = datetime.strptime(
                input("Ingrese la fecha de llegada (YYYY-MM-DD HH:MM): "),
                "%Y-%m-%d %H:%M",
            )
            no_asientos = int(input("Ingrese el No de asientos: "))

            vuelo = Vuelo(
                no_vuelo=no_vuelo,
                origen=origen,
                destino=destino,
                fecha_salida=fecha_salida,
                fecha_llegada=fecha_llegada,
                no_asientos=no_asientos,
            )

            vuelo = s_reservas.vuelos.append(vuelo)
            return vuelo

        except ValueError:
            print("Hubo un error en los datos. Por favor, revise las entradas.")
            return None


if __name__ == "__main__":

    sistema_reservas = SistemaReservas()
    

    vuelo2 = sistema_reservas.create_vuelo_manual(sistema_reservas)

    vuelos = SistemaReservas.get_todos_los_vuelos(sistema_reservas)

    SistemaReservas.crear_reservacion_manual(sistema_reservas)

    SistemaReservas.listar_reservaciones_por_vuelo(sistema_reservas)
