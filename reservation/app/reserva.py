from dataclasses import dataclass
from .vuelo import Vuelo
from random import randint


@dataclass
class Reserva:
    pasajero: str
    vuelo: Vuelo
    asiento: int

    def __post_init__(self):
        if self.asiento > self.vuelo.no_asientos or self.asiento < 1:
            raise ValueError(f"Asiento {self.asiento} no valido para este vuelo.")
        else:
            self.vuelo.no_asientos -= 1

    @classmethod
    def reservation(cls):
        pasajero = input("Nombre del pasajero:")
        while True:
            try:
                no_vuelo = int(input("Vuelo seleccionado: "))
                vuelo = [
                    x
                    for x in Vuelo.vuelos
                    if x.no_vuelo == no_vuelo and Vuelo.no_asientos > 0
                ][0]
                break
            except ValueError as e:
                print("Por favor ingrese el No del Vuelo")
            except IndexError as e:
                print("Vuelo inexistente, corija por favor")
        asiento = randint(1, int(vuelo.no_asientos))

        return cls(pasajero, vuelo, asiento)
