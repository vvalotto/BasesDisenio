class MiClase(object):

    def __init__(self):
        self.publica = 'Es Publica'
        self._privada = 'Es Privada'
        self.__muy_privada = "Muy Privada"


if __name__ == '__main__':
    clase = MiClase()
    print(clase.publica)
    print(clase._privada)
    print(clase._MiClase__muy_privada)