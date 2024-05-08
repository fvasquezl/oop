"""
2. **Diseña un sistema de reservas de vuelos**
   - Crea una clase `Vuelo` con atributos como número de vuelo,
    origen, destino, fecha y hora de salida/llegada, y cantidad de asientos disponibles.
   - Crea una clase `Reserva` que represente una reserva para un vuelo específico y contenga información como el nombre del pasajero y el asiento asignado.
   - Implementa una clase `SistemaReservas` que gestione una lista de vuelos y reservas, y permita a los usuarios realizar reservas, cancelarlas y ver los vuelos disponibles.
"""


class Vuelo:
    def __init__(self) -> None:
        self.no_vuelo = None
        self.origen = None
        self.destino = None
        self.fecha = None
        self.hora_salida = None
        self.hora_llegada = None
        self.no_asientos = None
        self.vuelos = []

    def set_no_vuelo(self, no_vuelo):
        self.no_vuelo = no_vuelo

    def set_origen(self, origen):
        self.origen = origen

    def set_destino(self, destino):
        self.destino = destino

    def set_fecha(self, fecha):
        self.fecha = fecha

    def set_hora_salida(self, hora_salida):
        self.hora_salida = hora_salida

    def set_hora_llegada(self, hora_llegada):
        self.hora_llegada = hora_llegada

    def set_no_asientos(self, no_asientos):
        self.no_asientos = no_asientos

    def create_vuelo(self):
        self.set_no_vuelo(input("No vuelo: "))
        self.set_origen(input("Origen: "))
        self.set_destino(input("Destino: "))
        self.set_fecha(input("Fecha: "))
        self.set_hora_salida(input("Hora salida: "))
        self.set_hora_llegada(input("Hora llegada: "))
        self.set_no_asientos(input("No asientos: "))

    def create_vuelos(self):
        num_vuelos = int(input("ingrese el numero de vuelos:"))
        for i in range(1, num_vuelos + 1):
            print(f"\n--Ingrese datos vuelo no {i}--")
            nuevo_vuelo = Vuelo()
            nuevo_vuelo.create_vuelo()
            self.vuelos.append(nuevo_vuelo)
            print(nuevo_vuelo)

    def __str__(self) -> str:
        return f"\nNo Vuelo:{self.no_vuelo} Origen:{self.origen} Destino:{self.destino} Fecha:{self.fecha} Hora Salida:{self.hora_salida} Hora Llegada:{self.hora_llegada} No Asientos:{self.no_asientos}"


class Reserva:
    def __init__(self, vuelo, nombre_pasajero, asiento) -> None:
        self.vuelo: vuelo
        self.nombre_pasajero: nombre_pasajero
        self.asiento: asiento


class SistemaReservas:

    def menu(self):
        ans = True
        while ans:
            print(
                """
                [1] Lista de vuelos 
                [2] Crear reservacion 
                [3] Cancelar reservacion
                [4] Salir
                """
            )
            ans = input("Opcion Seleccionada:")
            if ans == "1":
                print("lista de vuelos")
            elif ans == "2":
                print("Crea Reservacion")
            elif ans == "3":
                print("Cancela Reservacion")
            elif ans == "4":
                ans = None
                print("Hasta la vista Baby!")
            else:
                print("La opcion seleccionada es invalida")

    def alta_reservacion(self):
        pass


vuelo = Vuelo()
vuelo.create_vuelos()
print(vuelo)
# vuelo.imprime_vuelo()
# sistema_reservas = SistemaReservas()
# sistema_reservas.menu()
