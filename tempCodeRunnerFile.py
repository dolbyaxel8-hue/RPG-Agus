from personaje import Personajes
import random
import time
from objetos import espada_madera, espada_hierro, espada_diamante,lupa,armadura_bronce,armadura_hierro,armadura_diamante,escama_ouroboros
espada_hierro1 = espada_hierro("espada de hierro", 25,2,0)
espada_madera1 = espada_madera("espada de madera",15,1,0)
espada_diamante1 = espada_diamante("espada de diamante",40,3,0)
armadura_bronce1 = armadura_bronce("armadura de bronce",15,0.1,0)
armadura_hierro1 = armadura_hierro("armadura de hierro",25,0.2,0)
armadura_diamante1 = armadura_diamante("armadura de diamanate",40,0.3,0)
escama_ouroboros1 = escama_ouroboros("escama de ouroboros",50,50,0)
lupa1 = lupa("lupa",30,0,0)
items = {"espada de madera": espada_madera1, "espada de hierro": espada_hierro1, "espada de diamante": espada_diamante1, "armadura de bronce": armadura_bronce1, "armadura de hierro": armadura_hierro1, "armadura de diamante": armadura_diamante1, "escama de ouroboros": escama_ouroboros1}

def a():
    time.sleep(1)
def nuevo_nivel():
     print("╔══════════════════════╗")
     print("║   ⭐NUEVO NIVEL⭐    ║")
     print("╚══════════════════════╝")
     time.sleep(1)
def daño_hecho(a,b,c):
    return(a*(b+b*c))
def daño_recibido(d,e,f,g):
    return(d*(e-e*g+e*f))
class Jugador(Personajes):
    def __init__(self,nombre,vida,vida_maxima,daño,nivel,pociones,oro,experiencia,defensa,inventario,piso,envenenado,quemado,atrapado,envenenado_F, esquive1,esquive2,congelado, Ouroboros_encontrado):
        super(). __init__(nombre,vida,daño,oro,experiencia)
        self.nivel=nivel
        self.pociones = pociones
        self.vida_maxima = vida_maxima
        self.defensa = defensa
        self.inventario = inventario
        self.piso = piso
        self.envenenado = envenenado
        self.quemado = quemado
        self.atrapado = atrapado
        self.envenenado_F = envenenado_F
        self.esquive1 = esquive1
        self.esquive2 = esquive2
        self.congelado = congelado
        self.Ouroboros_encontrado = Ouroboros_encontrado
    def hacer_daño(self,enemigo,cantidad):
        enemigo.vida -= cantidad
        print("has hecho", cantidad, "de daño")
    def combate(self,enemigo):
        if self.piso >= 6:
            print("╔════════════════════════════════════════════════╗")
            print("║             DELANTE TUYO SE ENCUENTRA          ║")
            print("║                  EL OUROBOROS                  ║")
            print("╚════════════════════════════════════════════════╝")
            self.Ouroboros_encontrado = 1
        else:
            print("╔══════════════════════╗")
            print("║        COMBATE       ║")
            print("╚══════════════════════╝")
            print("te has encontrado con",enemigo.nombre)
        while True:
         if enemigo.vida <= 0:
             break
         if self.vida <= 0:
             break
         print("1. ⚔️ Atacar")
         print("2. 🧪 curarme")
         print("3. 🎒 inventario")
         print("4. 📜 estadisticas")
         decision = input("¿que opcion eliges?")
         if decision == "1":
             self.atacar(enemigo)
         if decision == "2":
             self.curar()
         if decision == "3":
             self.mostrar_I()
         if decision == "4":
             self.mostrar_E()
    def status(self,enemigo):
        if self.envenenado > 0:
            print("el veneno te quita vida", self.envenenado, "turnos restantes")
            if self.vida <= 5:
             self.vida = 1
             self.envenenado -= 1
             time.sleep(1)
            else:
             self.vida -= 5
             self.envenenado -= 1
             time.sleep(1)
        if self.quemado > 0:
            print("el fuego te quita vida", self.quemado, "turnos restantes")
            if self.vida <= 10:
                self.vida = 1
                self.quemado -= 1
                a()
            else:
                self.vida -= 10
                self.quemado -=1
                a()
        if self.congelado > 0:
            print("el hielo te quita vida", self.congelado, "turnos restantes")
            if self.vida <= 10:
                self.vida = 1
                self.congelado -= 1
                a()
            else:
                self.vida -= 10
                self.congelado -=1
                a()
        if self.atrapado >0:
            print("estas atrapado, la araña te golpea ")
            d = float(random.choice(["1","1","1","1","1","1","1","1","1","0"]))
            f = float(random.choice(["0","0","0","0","0","0","0","0","0","0.5"]))
            e = float(enemigo.daño)
            g = float(self.defensa)
            if d == 0:
             print(enemigo.nombre, "ha fallado su ataque")
            if f == 0.5:
             print(enemigo.nombre, "ha hecho un golpe critico")
            print("has recibido", daño_recibido(d,e,f,g),"de daño")
            enemigo.ataque_esp(self)
            time.sleep(1)
            self.vida -= daño_recibido(d,e,f,g)
            self.atrapado -=1 
        if self.envenenado_F > 0:
            print("el veneno profundo te quita vida", self.envenenado_F, "turnos restantes")
            if self.vida <= 5:
             self.vida = 1
             self.envenenado_F -= 1
             a()
            else:
             self.vida -= 5
             self.envenenado_F -= 1
             a()
    def atacar(self,enemigo):
        self.status(enemigo)
        print("decides atacar al", enemigo.nombre)
        time.sleep(1)
        enemigo.esquive(self)
        if lupa1.comprado >0:
           a = 1
        else:
           if self.esquive1 >0:
               a = float(random.choice(["1","1","1","1","0"]))
               self.esquive1 -= 1
           if self.esquive2 >0:
               a = float(random.choice(["1","0","0"]))
               self.esquive2 -=1
           else:
               a = float(random.choice(["1","1","1","1","1","1","1","1","1","0"]))
        b = float(self.daño)
        c = float(random.choice(["0","0","0","0","0","0","0","0","0","0.5"]))
        if a == 0:
            print(self.nombre, "ha fallado el ataque")
        if c == 0.5:
            print(self.nombre, "ha hecho un golpe critico")
        print("has hecho", self.hacer_daño(enemigo,round(daño_hecho(a,b,c), 1)), "de daño")
        time.sleep(1)
        if enemigo.vida > 0:
            d = float((random.choice(["1","1","1","1","1","1","1","1","1","0"])))
            f = float(random.choice(["0","0","0","0","0","0","0","0","0","0.5"]))
            e = float(enemigo.daño)
            g = float(self.defensa)
            if d == 0:
             print(enemigo.nombre, "ha fallado su ataque")
            if f == 0.5:
             print(enemigo.nombre, "ha hecho un golpe critico")
            enemigo.recibir_daño(self,round(daño_recibido(d,f,e,g), 1))