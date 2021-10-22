import sys

# La vista se encarga de recuperar la acción del usuario
# que consiste en escribir una línea de texto en la entrada estándar.
class Vista:
    def entrada(self):
        return sys.stdin.readline()