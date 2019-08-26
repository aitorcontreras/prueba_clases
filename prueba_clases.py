# Clase

class Elemento(object):

    def __init__(self, name):
        self.name = name

    def underscore(self): 
        self.name = name
        under = name.find('_')
        return under


# Lista

lista = ['Mod_ACTIVO', 'Mod_ORDEN', 'Mod_url']



# For loops

for i in lista:
    i = Elemento(i)
    print(i.name)

# Este último de abajo es el que no funciona

"""
for i in lista:
    i = Elemento(i)
    print(i.underscore())
"""