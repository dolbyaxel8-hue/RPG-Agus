
class tienda:
    def __init__(self,nombre,inventario):
        self.inventario = inventario
        self.nombre = nombre
    def mostrar_inventario(self):
        print(self.inventario)
class vendedora_ambulante(tienda):
    def __init__(self,nombre,inventario):
        super(). __init__(nombre,inventario)
class tienda_normal(tienda):
    def __init__(self,nombre,inventario):
        super(). __init__(nombre,inventario)
class tienda_epica(tienda):
    def __init__(self,nombre,inventario):
        super(). __init__(nombre,inventario)
    