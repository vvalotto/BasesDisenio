def saludar(idioma):
    def saludar_es():
        print('Hola')

    def saludar_en():
        print ('Hi')

    def saludar_fr():
        print ('Salut')

    saludos = {'es': saludar_es,
               'en': saludar_en,
               'fr': saludar_fr}

    return saludos[idioma]

f = saludar('es')
f()