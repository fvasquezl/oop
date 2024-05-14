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

    def __repr__(self) -> str:
        return f"No vuelo: {self.no_vuelo}, Origen: {self.origen}, Destino: {self.destino}, Fecha: {self.fecha}, Salida: {self.hora_salida}, Llegada: {self.hora_llegada}, No asiento: {self.no_asientos}"

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
