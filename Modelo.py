import sys
from Controlador import*
# El modelo se encarga de la gestión de los datos.
class Modelo:
    def __init__(self):
        self.cadenas = []

    # Añade una cadena a la lista.
    def agregar(self, cadena):
        self.cadenas.append(cadena)

    # Devuelve la lista de cadenas.
    def recuperarCadenas():
        return self.cadenas
    # Los actores MVC son globales en este ejemplo...
    def vista():
        vista = Vista ()
        return vista
    def controlador():
        controlador = Controlador ()
        return controlador
    def modelo():
        modelo = Modelo()
        return modelo
    # Vamos a recuperar dos líneas de la entrada estándar.
    for _ in range(2):
        controlador.almacenarEntrada()
    # Después las guardamos en un archivo.
    controlador.guardarCadenas()