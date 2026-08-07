class tienda:

    def __init__(self, nombre, inventario):
        self.nombre = nombre
        self.inventario = inventario


    def mostrar_inventario(self):
        print(self.inventario)



class vendedora_ambulante(tienda):

    def __init__(self, nombre, inventario):
        super().__init__(nombre, inventario)



class tienda_normal(tienda):

    def __init__(self, nombre, inventario):
        super().__init__(nombre, inventario)



class tienda_epica(tienda):

    def __init__(self, nombre, inventario):
        super().__init__(nombre, inventario)



# ==========================
# CREAR TIENDAS
# ==========================


vendedora_ambulante1 = vendedora_ambulante(
    "Vendedora ambulante",
    [
        "espada de madera",
        "armadura de bronce",
        "pociones"
    ]
)


tienda_normal1 = tienda_normal(
    "Tienda normal",
    [
        "espada de hierro",
        "armadura de hierro",
        "pociones"
    ]
)


tienda_epica1 = tienda_epica(
    "Tienda épica",
    [
        "espada de diamante",
        "armadura de diamante",
        "lupa",
        "escama de ouroboros",
        "pociones"
    ]
)



# ==========================
# PROBABILIDADES POR PISO
# ==========================

# Piso 1:
# Solo común normalmente

tiendas1 = {

    "tiendas": [
        "vendedora_ambulante",
        "tienda_normal",
        "tienda_epica"
    ],

    "probabilidades": [
        10,
        2,
        0
    ]

}



# Piso 2

tiendas2 = {

    "tiendas": [
        "vendedora_ambulante",
        "tienda_normal",
        "tienda_epica"
    ],

    "probabilidades": [
        7,
        4,
        1
    ]

}



# Piso 3

tiendas3 = {

    "tiendas": [
        "vendedora_ambulante",
        "tienda_normal",
        "tienda_epica"
    ],

    "probabilidades": [
        3,
        6,
        2
    ]

}



# Piso 4
# Ya no aparece casi común

tiendas4 = {

    "tiendas": [
        "vendedora_ambulante",
        "tienda_normal",
        "tienda_epica"
    ],

    "probabilidades": [
        0,
        5,
        5
    ]

}



# Piso 5
# Más posibilidades de épica

tiendas5 = {

    "tiendas": [
        "vendedora_ambulante",
        "tienda_normal",
        "tienda_epica"
    ],

    "probabilidades": [
        0,
        3,
        7
    ]

}



# ==========================
# DICCIONARIO PARA BUSCAR TIENDA
# ==========================


tiendas_O = {

    "vendedora_ambulante": vendedora_ambulante1,

    "tienda_normal": tienda_normal1,

    "tienda_epica": tienda_epica1

}