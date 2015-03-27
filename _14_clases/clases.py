

class ClaseA(object):

    AtributoClase = None

    def mostrar(self, nombre):
        self.nombre = nombre
        print('nombre {0}, atributo {1}'.format(nombre, str(ClaseA.AtributoClase)))

    def asignar(valor):
        ClaseA.AtributoClase = valor

