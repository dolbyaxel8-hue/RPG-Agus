
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

    def __init__(self,nombre,precio,estadistica,comprado):
        super().__init__(nombre,precio,estadistica,comprado)


    def usar(self,jugador):

        jugador.lupa = True


    def explicar(self):

        print("🔍 Ahora tus ataques nunca fallan")
espada_hierro1 = espada_hierro("espada de hierro", 25,2,0)
espada_madera1 = espada_madera("espada de madera",15,1,0)
espada_diamante1 = espada_diamante("espada de diamante",40,3,0)
armadura_bronce1 = armadura_bronce("armadura de bronce",15,0.1,0)
armadura_hierro1 = armadura_hierro("armadura de hierro",25,0.2,0)
armadura_diamante1 = armadura_diamante("armadura de diamanate",40,0.3,0)
escama_ouroboros1 = escama_ouroboros("escama de ouroboros",150,50,0)
lupa1 = lupa("lupa",30,0,0)
items = {"espada de madera": espada_madera1, "espada de hierro": espada_hierro1, "espada de diamante": espada_diamante1, "armadura de bronce": armadura_bronce1, "armadura de hierro": armadura_hierro1, "armadura de diamante": armadura_diamante1, "escama de ouroboros": escama_ouroboros1}