from dataclasses import dataclass
from datetime import datetime


@dataclass
class Vuelo:
    no_vuelo: int
    origen: str
    destino: str
    fecha_salida: datetime
    fecha_llegada: datetime
    no_asientos: int

    def __post_init__(self):
        if self.fecha_salida >= self.fecha_llegada:
            raise ValueError(
                "La fecha de salida debe ser anterior a la fecha de llegada"
            )

    def __repr__(self):
        return (
            f"Vuelo {self.no_vuelo}: {self.origen} -> {self.destino}\n"
            f"Salida: {self.fecha_salida.strftime('%Y-%m-%d %H:%M')}\n"
            f"Llegada: {self.fecha_llegada.strftime('%Y-%m-%d %H:%M')}\n"
            f"Asientos disponibles: {self.no_asientos}"
        )

    @classmethod
    def create_vuelo(
        cls,
        no_vuelo: int,
        origen: str,
        destino: str,
        fecha_salida: datetime,
        fecha_llegada: datetime,
        no_asientos: int,
    ) -> "Vuelo":
        try:
            return cls(
                no_vuelo=no_vuelo,
                origen=origen,
                destino=destino,
                fecha_salida=fecha_salida,
                fecha_llegada=fecha_llegada,
                no_asientos=no_asientos,
            )
        except ValueError as e:
            print(f"Error: {e}")
            return None
