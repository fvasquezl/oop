from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Vuelo:
    """
    Representa un vuelo con información como número de vuelo, origen, destino,
    fecha de salida, fecha de llegada y número de asientos.
    """

    no_vuelo: int
    origen: str
    destino: str
    fecha_salida: datetime
    fecha_llegada: datetime
    no_asientos: int = field(default=0, init=True)

    def __post_init__(self):
        """
        Valida que la fecha de salida sea anterior a la fecha de llegada
        y que los atributos 'origen', 'destino' no sean cadenas vacías
        y que 'no_asientos' sea un valor positivo.
        """

        if self.fecha_salida >= self.fecha_llegada:
            raise ValueError(
                "La fecha de salida debe ser anterior a la fecha de llegada"
            )
        if not self.origen or not self.destino:
            raise ValueError("El origen y destino no pueden ser cadenas vacías")

        if self.no_asientos <= 0:
            raise ValueError("El número de asientos debe ser un valor positivo")

    def __repr__(self):
        """
        Devuelve una representación legible del objeto Vuelo.
        """
        return (
            f"Vuelo {self.no_vuelo}: {self.origen} -> {self.destino}\n"
            f"Salida: {self.fecha_salida.strftime('%Y-%m-%d %H:%M')}\n"
            f"Llegada: {self.fecha_llegada.strftime('%Y-%m-%d %H:%M')}\n"
            f"Asientos disponibles: {self.no_asientos}"
        )
