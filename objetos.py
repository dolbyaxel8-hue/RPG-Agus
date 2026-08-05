
class objetos_B:
    def __init__(self,nombre,precio,estadistica,comprado):
        self.precio = precio
        self.estadistica = estadistica
        self.nombre = nombre
        self.comprado = comprado
    def usar(self,jugador):
        print("a")
    def explicar(self):
         print("a")
class espada_madera(objetos_B):
    def __init__(self,nombre,precio,estadisticas,comprado):
        super(). __init__(nombre,precio,estadisticas,comprado)
    def usar(self,jugador):
        jugador.daño += self.estadistica
    def explicar(self):
            print("te ha subido el ataque")
class espada_hierro(objetos_B):
    def __init__(self,nombre,precio,estadisticas,comprado):
        super(). __init__(nombre,precio,estadisticas,comprado)
    def usar(self,jugador):
        jugador.daño += self.estadistica
    def explicar(self):
            print("te ha subido el ataque")
class espada_diamante(objetos_B):
    def __init__(self,nombre,precio,estadisticas,comprado):
        super(). __init__(nombre,precio,estadisticas,comprado)
    def usar(self,jugador):
        jugador.daño += self.estadistica
    def explicar(self):
        print("te ha subido el ataque")
class armadura_hierro(objetos_B):
    def __init__(self,nombre,precio,estadisticas,comprado):
        super(). __init__(nombre,precio,estadisticas,comprado)
    def usar(self,jugador):
        jugador.defensa += self.estadistica
    def explicar(self):
            print("te ha subido la defensa")
class armadura_bronce(objetos_B):
    def __init__(self,nombre,precio,estadisticas,comprado):
        super(). __init__(nombre,precio,estadisticas,comprado)
    def usar(self,jugador):
        jugador.defensa += self.estadistica
    def explicar(self):
                print("te ha subido la defensa")
class armadura_diamante(objetos_B):
    def __init__(self,nombre,precio,estadisticas,comprado):
        super(). __init__(nombre,precio,estadisticas,comprado)
    def usar(self,jugador):
        jugador.defensa += self.estadistica
    def explicar(self):
                print("te ha subido la defensa")
class escama_ouroboros(objetos_B):
    def __init__(self,nombre,precio,estadisticas,comprado):
        super(). __init__(nombre,precio,estadisticas,comprado)
    def usar(self,jugador):
        jugador.vida_maxima += self.estadistica
    def explicar(self):
                print("te ha subido la vida maxima")
class lupa(objetos_B):
    def __init__(self,nombre,precio,estadisticas,comprado):
        super(). __init__(nombre,precio,estadisticas,comprado)