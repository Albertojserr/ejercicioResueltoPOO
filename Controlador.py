import sys
from Vista import*
from Modelo import*

# El controlador hace el enlace entre la vista y el modelo,
# realizando el procesamiento de datos.
class Controlador:

    # El controlador pide a la vista que recupere una cadena
    # en la entrada estándar, y luego solicita al modelo
    # que la almacene.
    def almacenarEntrada(self):
        cadena = vista.entrada()
        modelo.agregar(cadena.upper())

    # El controlador recupera las cadenas del modelo
    # y las escribirá en un archivo.
    def guardarCadenas(self):
        cadenas = modelo.recuperarCadenas()
        with open('test.txt', 'w') as f:
            for cadena in cadenas:
                f.write(cadena)