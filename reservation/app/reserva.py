from dataclasses import dataclass, field
import itertools
from .vuelo import Vuelo
from random import randint

id_gen = itertools.count(start=1, step=1).__next__


@dataclass
class Reserva:
    pasajero: str
    vuelo: Vuelo
    asiento: int
    no_reservacion: int = field(default_factory=id_gen)

    def __post_init__(self):
        if self.asiento > self.vuelo.no_asientos or self.asiento < 1:
            raise ValueError(f"Asiento {self.asiento} no valido para este vuelo.")
        else:
            self.vuelo.no_asientos -= 1

    def __repr__(self) -> str:
        return f"\nNo Reservacion: {self.no_reservacion}\nPasajero: {self.pasajero}\nAsiento: {self.asiento}\nVuelo: {self.vuelo}"

    @classmethod
    def create_reservation(cls):
        pasajero = input("Nombre del pasajero:")
        while True:
            try:
                no_vuelo = int(input("Vuelo seleccionado: "))
                vuelo = next(
                    (
                        v
                        for v in Vuelo.vuelos
                        if v.no_vuelo == no_vuelo and v.no_asientos > 0
                    ),
                    None,
                )
                if vuelo:
                    break
                else:
                    print(
                        "Vuelo inexistente o sin asientos disponibles, corrija por favor"
                    )
            except ValueError as e:
                print("Por favor ingrese el No del Vuelo")

        asiento = randint(1, int(vuelo.no_asientos))

        return cls(pasajero, vuelo, asiento)


"""
Implementar injection dependency
"""
