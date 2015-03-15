__author__ = 'voval'
__version__ = '1.0.0'


def informar():
    print(__version__)
    print(__author__)

def funcion():
    print('Nueva funcion')

if __name__ == '__main__':
    informar()
else:
    funcion()