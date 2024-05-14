from dataclasses import dataclass, field
from datetime import datetime
import itertools

from vuelo import Vuelo


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
        return (
            f"No Reservacion: {self.no_reservacion}\n"
            f"Pasajero: {self.pasajero}\n"
            f"Asiento: {self.asiento}\n"
            f"Vuelo: {self.vuelo}"
        )
