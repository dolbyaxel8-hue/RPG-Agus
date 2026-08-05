from personaje import Personajes, efectos
import random
import time
from objetos import espada_madera, espada_hierro, espada_diamante,lupa,armadura_bronce,armadura_hierro,armadura_diamante,escama_ouroboros
espada_hierro1 = espada_hierro("espada de hierro", 25,2,0)
espada_madera1 = espada_madera("espada de madera",15,1,0)
espada_diamante1 = espada_diamante("espada de diamante",40,3,0)
armadura_bronce1 = armadura_bronce("armadura de bronce",15,0.1,0)
armadura_hierro1 = armadura_hierro("armadura de hierro",25,0.2,0)
armadura_diamante1 = armadura_diamante("armadura de diamanate",40,0.3,0)
escama_ouroboros1 = escama_ouroboros("escama de ouroboros",150,50,0)
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
    def __init__(self,nombre,vida,vida_maxima,daño,nivel,pociones,oro,experiencia,defensa,inventario,piso, esquive1,esquive2, Ouroboros_encontrado,efectos):
        super(). __init__(nombre,vida,daño,oro,experiencia)
        self.nivel=nivel
        self.pociones = pociones
        self.vida_maxima = vida_maxima
        self.defensa = defensa
        self.inventario = inventario
        self.piso = piso
        self.esquive1 = esquive1
        self.esquive2 = esquive2
        self.Ouroboros_encontrado = Ouroboros_encontrado
        self.efectos = efectos
    def ataque_esp():
        pass
    def esquive():
        pass
    def recibir_daño():
        pass
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
         try:
             decision = int(input("¿que opcion eliges?"))
             if decision == 1:
              self.atacar(enemigo)
             if decision == 2:
              self.curar()
             if decision == 3:
              self.mostrar_I()
             if decision == 4:
              self.mostrar_E()
         except ValueError:
             print("escribe un numero")
    def status(self,enemigo):
        if self.efectos.envenenado > 0:
            print("el veneno te quita vida", self.efectos.envenenado, "turnos restantes")
            if self.vida <= 5:
             self.vida = 1
             self.efectos.envenenado -= 1
             time.sleep(1)
            else:
             self.vida -= 5
             self.efectos.envenenado -= 1
             time.sleep(1)
        if self.efectos.quemado > 0:
            print("el fuego te quita vida", self.efectos.quemado, "turnos restantes")
            if self.vida <= 10:
                self.vida = 1
                self.efectos.quemado -= 1
                a()
            else:
                self.vida -= 10
                self.efectos.quemado -=1
                a()
        if self.efectos.congelado > 0:
            print("el hielo te quita vida", self.efectos.congelado, "turnos restantes")
            if self.vida <= 10:
                self.vida = 1
                self.efectos.congelado -= 1
                a()
            else:
                self.vida -= 10
                self.efectos.congelado -=1
                a()
        if self.efectos.atrapado >0:
            print("estas atrapado, la araña te golpea ")
            d = float(random.choice(["1","1","1","1","1","1","1","1","1","0"]))
            f = float(random.choice(["0","0","0","0","0","0","0","0","0","0.5"]))
            e = float(enemigo.daño)
            g = float(self.defensa)
            if d == 0:
             print(enemigo.nombre, "ha fallado su ataque")
            if f == 0.5:
             print(enemigo.nombre, "ha hecho un golpe critico")
            enemigo.recibir_daño(self,round(daño_recibido(d,f,e,g), 1))
            enemigo.ataque_esp(self)
            time.sleep(1)
            self.efectos.atrapado -=1 
        if self.efectos.envenenado_F > 0:
            print("el veneno profundo te quita vida", self.efectos.envenenado_F, "turnos restantes")
            if self.vida <= 5:
             self.vida = 1
             self.efectos.envenenado_F -= 1
             a()
            else:
             self.vida -= 5
             self.efectos.envenenado_F -= 1
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
        self.hacer_daño(enemigo,round(daño_hecho(a,b,c), 1))
        time.sleep(1)
        if enemigo.vida > 0:
            d = int((random.choice(["1","1","1","1","1","1","1","1","1","0"])))
            f = float(random.choice(["0","0","0","0","0","0","0","0","0","0.5"]))
            e = float(enemigo.daño)
            g = float(self.defensa)
            if d == 0:
             print(enemigo.nombre, "ha fallado su ataque")
            if f == 0.5:
             print(enemigo.nombre, "ha hecho un golpe critico")
            enemigo.recibir_daño(self,round(daño_recibido(d,e,f,g), 1))
            if d > 0:
                enemigo.ataque_esp(self)
            time.sleep(1)
        if enemigo.vida <= 0:
           print("has derrotado al", enemigo.nombre, "la recompensa es", enemigo.oro, "de oro y", enemigo.experiencia, "puntos de experiencia")
           time.sleep(1)
           self.oro += enemigo.oro
           self.experiencia += enemigo.experiencia
    def curar(self):
       if self.pociones <= 0:
          print("no tienes pociones")
       else:
          print("tienes", self.pociones, "pociones")
          print("tienes", self.vida, "de vida")
          decision_C = None
          decision_C = input("¿deseas curarte?")
          if decision_C == "si":
             self.pociones -= 1
             if self.vida >= self.vida_maxima - 20:
                self.vida = self.vida_maxima
                print("estas al maximo de vida", self.vida_maxima)
             else:
                self.vida += 20
                print("tu vida actual es:", round(self.vida,1))
          else:
             print("decides no curarte")
    def tienda(self,tienda):
       print("╔══════════════════════╗")
       print("║        TIENDA        ║")
       print("╚══════════════════════╝")
       print("te has encontrado con", tienda.nombre, "tienes", self.oro, "de oro")
       print("la", tienda.nombre, "ofrece", tienda.inventario)
       while True:
        comprar_Duda = None
        print("1. si")
        print("2. no")
        comprar_Duda = int(input("¿deseas comprar algo?"))
        if comprar_Duda ==1:
           print("decides comprar")
           compra = None
           compra = input("¿que quieres comprar?")
           if compra in items and items[compra].comprado == 0:
               if self.oro >= items[compra].precio:
                print("decides comprar la", items[compra].nombre)
                self.oro -= items[compra].precio
                items[compra].usar(self)
                items[compra].explicar()
                time.sleep(0.5)
                print("oro restante", self.oro)
                items[compra].comprado += 1
                self.inventario.append(items[compra])
               else:
                  print("no tienes suficiente dinero")
           elif compra in items and items[compra].comprado >= 0:
               print("ya posees este objeto")
           elif compra == "lupa":
              if self.oro >= 30 and lupa1.comprado == 0:
                print("decides comprar la lupa")
                print("lupa añadida a tu inventario")
                print("oro restante", self.oro)
                self.oro -= 30
                lupa1.comprado +=1
                self.inventario.append(lupa1)
              else:
                 print("no tienes suficiente dinero o ya has comprado el objeto")
           elif compra == "pociones":
              if self.oro >= 30:
                 print("decides comprar una pocion")
                 self.oro -= 30
                 print("pocion añadida a tu inventario")
                 print("oro restante", self.oro)
                 self.pociones += 1
           else:
              print("no existe el objeto")
        else:
           print("decides no comprar")
           time.sleep(1)
           break
    def check_level(self):
        if self.nivel == 1 and self.experiencia >= 50:
          nuevo_nivel()
          print("has subido al nivel 2, vida maxima aumentada y 20 de vida ganados")
          self.daño += 0.5
          self.vida_maxima +=5
          self.nivel = 2
          self.vida += 20
          time.sleep(1)
        if self.nivel == 2 and self.experiencia >= 180:
                  nuevo_nivel()
                  print("has subido al nivel 3, vida maxima aumentada y 20 de vida ganados")
                  self.daño += 0.5
                  self.vida_maxima +=5
                  self.nivel = 3
                  self.vida += 20
                  time.sleep(1)
        if self.nivel == 3 and self.experiencia >= 260:
                  nuevo_nivel()
                  print("has subido al nivel 4, vida maxima aumentada y 20 de vida ganados")
                  self.daño += 0.5
                  self.vida_maxima +=5
                  self.nivel = 4
                  self.vida += 20
                  time.sleep(1)
        if self.nivel == 4 and self.experiencia >= 350:
                  nuevo_nivel()
                  print("has subido al nivel 5, vida maxima aumentada y 20 de vida ganados")
                  self.daño += 0.5
                  self.vida_maxima +=5
                  self.nivel = 5
                  self.vida += 20
                  time.sleep(1)
        if self.nivel == 5 and self.experiencia >= 450:
                  nuevo_nivel()
                  print("has subido al nivel 6, vida maxima aumentada y 20 de vida ganados")
                  self.daño += 0.5
                  self.vida_maxima +=5
                  self.nivel = 6
                  self.vida += 20
                  time.sleep(1)
        if self.nivel == 6 and self.experiencia >= 560:
                  nuevo_nivel()
                  print("has subido al nivel 7, vida maxima aumentada y 20 de vida ganados")
                  self.daño += 0.5
                  self.vida_maxima +=5
                  self.nivel = 7
                  self.vida += 20
                  time.sleep(1)
        if self.nivel == 7 and self.experiencia >= 680:
                  nuevo_nivel()
                  print("has subido al nivel 8, vida maxima aumentada y 20 de vidas ganados")
                  self.daño += 0.5
                  self.vida_maxima +=5
                  self.nivel = 8
                  self.vida += 20
                  time.sleep(1)
        if self.nivel == 8 and self.experiencia >= 810:
                  nuevo_nivel()
                  print("has subido al nivel 9, vida maxima aumentada y 20 de vida ganados")
                  self.daño += 0.5
                  self.vida_maxima +=5
                  self.nivel = 9
                  self.vida += 20
                  time.sleep(1)
        if self.nivel == 9 and self.experiencia >= 950:
                  nuevo_nivel()
                  print("has subido al nivel 10, vida maxima aumentada y 20 de vida ganados")
                  self.daño += 0.5
                  self.vida_maxima +=5
                  self.nivel = 10
                  self.vida += 20
                  time.sleep(1)
        if self.nivel == 10 and self.experiencia >= 1100:
                  nuevo_nivel()
                  print("vida maxima aumentada y 20 de vida ganados")
                  print("🏆 NIVEL MÁXIMO ALCANZADO 🏆")
                  self.daño += 0.5
                  self.vida_maxima +=5
                  self.vida += 20
                  self.nivel = 11
                  time.sleep(1)
    def mostrar_I(self):
        print("╔══════════════════════╗")
        print("║      INVENTARIO      ║")
        print("╚══════════════════════╝")
        for objeto in self.inventario:
            print("-",objeto.nombre)
            print("-------------------------")
        print(self.pociones,"pociones")
        print("=========================")
    def mostrar_E(self):
        print("╔══════════════════════╗")
        print("║        STATS         ║")
        print("╚══════════════════════╝")
        print("⚔️ ", round(self.daño, 1), "de daño")
        print("-------------------------")
        print("❤️ ", round(self.vida, 1), "de vida")
        print("-------------------------") 
        print("❤️‍🔥", round(self.vida_maxima, 1), "de vida maxima")
        print("-------------------------")
        print("🛡️ ", round(self.defensa,2), "de defensa")
        print("-------------------------")
        print("⭐ nivel", self.nivel)
        print("-------------------------")
        print("💰", self.oro, "de oro") 
        print("-------------------------")
        print("✨", self.experiencia, "de experiencia")
        print("-------------------------")