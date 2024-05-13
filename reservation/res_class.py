"""
2. **Diseña un sistema de reservas de vuelos**
   - Crea una clase `Vuelo` con atributos como número de vuelo,
    origen, destino, fecha y hora de salida/llegada, y cantidad de asientos disponibles.
   - Crea una clase `Reserva` que represente una reserva para un vuelo específico y contenga información como el nombre del pasajero y el asiento asignado.
   - Implementa una clase `SistemaReservas` que gestione una lista de vuelos y reservas, y permita a los usuarios realizar reservas, cancelarlas y ver los vuelos disponibles.
"""

from dataclasses import dataclass, field, asdict
from typing import List, Optional, ClassVar


@dataclass
class Vuelo:
    no_vuelo: Optional[int] = field(default=0)
    origen: Optional[str] = field(default=None)
    destino: Optional[str] = field(default=None)
    fecha: Optional[str] = field(default=None)
    hora_salida: Optional[str] = field(default=None)
    hora_llegada: Optional[str] = field(default=None)
    no_asientos: Optional[int] = field(default=0)

    vuelos: ClassVar[List["Vuelo"]] = []
    # vuelos: list["Vuelo"] = field(default_factory=list, repr=False)

    # def __post_init__(self):
    #     self.vuelos.append(self)

    # def __repr__(self):
    #     return self.vuelo_repr()

    # def vuelo_repr(self):
    #     return f"Vuelo({self.no_vuelo}, {self.origen}, {self.destino}, {self.fecha}, {self.hora_salida}, {self.hora_llegada}, {self.no_asientos})"

    @classmethod
    def agregar_vuelo(cls, vuelo):
        cls.vuelos.append(vuelo)

    @classmethod
    def mostrar_vuelos(cls):
        if not cls.vuelos:
            print("No hay vuelos registrados.")
        else:
            print("Lista de vuelos:")
            for vuelo in cls.vuelos:
                print(asdict(vuelo))

    @staticmethod
    def generate_labels(vuelo: "Vuelo", create=True):
        labels = {}
        for k, v in vuelo.__dict__.items():
            lb = k.split("_")
            label = " ".join(lb).title()
            if create:
                labels[k] = f"{label}: "
            else:
                labels[k] = f"{label} [{v}]: "
        return labels

    @classmethod
    def create_update_vuelo(cls, vuelo: "Vuelo", create=True):
        labels = Vuelo.generate_labels(vuelo, create)

        if create:
            no_vuelo = input(labels["no_vuelo"]) or vuelo.no_vuelo
        else:
            print(f"Updating fly: {vuelo.no_vuelo}")
            no_vuelo = vuelo.no_vuelo

        origen = input(labels["origen"]) or vuelo.origen
        destino = input(labels["destino"]) or vuelo.destino
        fecha = input(labels["fecha"]) or vuelo.fecha
        hora_salida = input(labels["hora_salida"]) or vuelo.hora_salida
        hora_llegada = input(labels["hora_llegada"]) or vuelo.hora_llegada
        no_asientos = input(labels["no_asientos"]) or vuelo.no_asientos
        return cls(
            no_vuelo, origen, destino, fecha, hora_salida, hora_llegada, no_asientos
        )

    # def __repr__(self) -> str:
    #     return asdict(Vuelo)


@dataclass
class Reserva:
    vuelo: Vuelo
    pasajero: str
    asiento: int

    def __post_init__(self):
        if self.asiento > self.vuelo.no_asientos or self.asiento < 1:
            raise ValueError(f"Asiento {self.asiento} no valido para este vuelo.")
        else:
            self.vuelo.no_asientos -= 1

    def __repr__(self) -> str:
        return f"Reserva({self.vuelo},'{self.pasajero},{self.asiento})"


@dataclass
class SistemaReservas:
    vuelos: list[Vuelo]

    @staticmethod
    def menu():
        options = {
            1: "Lista de vuelos",
            2: "Crear reservacion",
            3: "Cancelar reservacion",
            4: "Salir",
        }
        while True:
            print("\nMenu Principal:")
            for option, description in options.items():
                print(f"[{option}] {description}")
            try:
                choice = int(input("Opcion Seleccionada:"))
                if choice in options:
                    if choice == 4:
                        print("Hasta la vista Baby!")
                        break
                    else:
                        if choice == 1:
                            print("lista de vuelos")
                        elif choice == 2:
                            print("Crea Reservacion")
                        elif choice == 3:
                            print("Cancela Reservacion")
                else:
                    print("La opcion seleccionada es invalida")

            except ValueError as e:
                print("Please enter a valid number.")
            except Exception as e:
                print(repr(e))

    def alta_reservacion(self):
        pass


@dataclass
class Vuelos:
    vuelos: List["Vuelo"] = field(default_factory=list, repr=False)

    def __post_init__(self):
        self.vuelos.append(self)

    @classmethod
    def mostrar_vuelos(cls):

        if not cls.vuelos:
            print("No hay vuelos registrados.")
        else:
            print("Lista de vuelos:")
            for vuelo in cls.vuelos:
                print(vuelo)


if __name__ == "__main__":
    # SistemaReservas.menu()

    vuelo0 = Vuelo(
        no_vuelo=14,
        origen="Veracruz",
        destino="Tijuana",
        fecha="30/09/24",
        hora_salida="9:20",
        hora_llegada="13:00",
        no_asientos=180,
    )

    vuelo1 = Vuelo(
        no_vuelo=14,
        origen="Veracruz",
        destino="Tijuana",
        fecha="30/09/24",
        hora_salida="9:20",
        hora_llegada="13:00",
        no_asientos=190,
    )

    vuelo2 = Vuelo(
        no_vuelo=14,
        origen="Veracruz",
        destino="Tijuana",
        fecha="30/09/24",
        hora_salida="9:20",
        hora_llegada="13:00",
        no_asientos=200,
    )

    vuelos = Vuelos([vuelo0, vuelo1, vuelo2])
    vuelos.mostrar_vuelos()

    # Vuelo.agregar_vuelo(vuelo0)
    # Vuelo.agregar_vuelo(vuelo1)
    # Vuelo.agregar_vuelo(vuelo2)

    # Vuelo.mostrar_vuelos()
