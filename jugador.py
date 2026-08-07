from personaje import Personajes, efectos
import random
import time
from objetos import espada_madera1, espada_hierro1, espada_diamante1,lupa1,armadura_bronce1,armadura_hierro1,armadura_diamante1,escama_ouroboros1,items


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
        self.registro = []
        self.lupa = False
    def mensaje(self,texto):
        self.registro.append(texto)
    def ataque_esp(self):
        pass
    def esquive():
        pass
    def recibir_daño():
        pass
    def hacer_daño(self,enemigo,cantidad):

     enemigo.vida -= cantidad

     if cantidad <= 0:

         self.registro.append(
            "❌ Has fallado el ataque")

     else:

         self.registro.append(
            f"⚔️ Has hecho {cantidad} de daño")
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
            self.registro.append(
    f"☠️ El veneno te hace daño ({self.efectos.envenenado} turnos restantes)")
            if self.vida <= 5:
             self.vida = 1
             self.efectos.envenenado -= 1
            else:
             self.vida -= 5
             self.efectos.envenenado -= 1
        if self.efectos.quemado > 0:
            self.registro.append(
    f"🔥 La quemadura sigue activa ({self.efectos.quemado} turnos restantes)")
            if self.vida <= 10:
                self.vida = 1
                self.efectos.quemado -= 1
            else:
                self.vida -= 10
                self.efectos.quemado -=1
        if self.efectos.congelado > 0:
            self.registro.append(
    f"❄️ El hielo sigue activo ({self.efectos.congelado} turnos restantes)")
            if self.vida <= 10:
                self.vida = 1
                self.efectos.congelado -= 1
            else:
                self.vida -= 10
                self.efectos.congelado -=1
        if self.efectos.atrapado >0:
            self.registro.append(
    "🕸️ Estás atrapado por la telaraña")
            d = float(random.choice(["1","1","1","1","1","1","1","1","1","0"]))
            f = float(random.choice(["0","0","0","0","0","0","0","0","0","0.5"]))
            e = float(enemigo.daño)
            g = float(self.defensa)
            if d == 0:
             self.registro.append(
    f"❌ {enemigo.nombre} ha fallado su ataque")
            if f == 0.5:
             self.registro.append(
    f"💥 {enemigo.nombre} ha hecho un golpe crítico")
            enemigo.recibir_daño(self,round(daño_recibido(d,f,e,g), 1))
            enemigo.ataque_esp(self)
            self.efectos.atrapado -=1 
        if self.efectos.envenenado_F > 0:
            self.registro.append(
    f"☠️ Veneno profundo activo ({self.efectos.envenenado_F} turnos restantes)")
            if self.vida <= 5:
             self.vida = 1
             self.efectos.envenenado_F -= 1
            else:
             self.vida -= 5
             self.efectos.envenenado_F -= 1
    def atacar(self,enemigo):
           self.status(enemigo)

           self.registro.append(
           f"⚔️ Atacas a {enemigo.nombre}"
)
           enemigo.esquive(self)

           if self.lupa:

            a = 1

           else:

                if self.esquive1 > 0:

                 a = float(random.choice(["1","1","1","1","0"]))
                 self.esquive1 -= 1

                elif self.esquive2 > 0:

                 a = float(random.choice(["1","0","0"]))
                 self.esquive2 -= 1

                else:

                 a = float(random.choice(["1","1","1","1","1","1","1","1","1","0"]))

           b = float(self.daño)

           c = float(random.choice(["0","0","0","0","0","0","0","0","0","0.5"]))

           if a == 0:

            self.registro.append(
        f"❌ {self.nombre} ha fallado el ataque")

           if c == 0.5:

            self.registro.append(
        f"💥 {self.nombre} ha hecho un golpe crítico")

           self.hacer_daño(enemigo, round(daño_hecho(a, b, c), 1))

           if enemigo.vida > 0:

            d = int(random.choice(["1","1","1","1","1","1","1","1","1","0"]))

            f = float(random.choice(["0","0","0","0","0","0","0","0","0","0.5"]))

            e = float(enemigo.daño)

            g = float(self.defensa)

            if d == 0:

             self.registro.append(
            f"❌ {enemigo.nombre} ha fallado su ataque")

            if f == 0.5:

             self.registro.append(
            f"💥 {enemigo.nombre} ha hecho un golpe crítico")

            enemigo.recibir_daño(self, round(daño_recibido(d, e, f, g), 1))

            if d > 0:

             enemigo.ataque_esp(self)
           if enemigo.vida <= 0:
            enemigo.vida = 0
            self.registro.append(
            f"🏆 Has derrotado al {enemigo.nombre}")
            self.registro.append(
            f"💰 +{enemigo.oro} oro")
            self.registro.append(
            f"✨ +{enemigo.experiencia} experiencia")
            self.oro += enemigo.oro
            self.experiencia += enemigo.experiencia
            self.check_level()
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
           break
    def check_level(self):

     niveles = {
        1: 50,
        2: 180,
        3: 260,
        4: 350,
        5: 450,
        6: 560,
        7: 680,
        8: 810,
        9: 950,
        10: 1100
    }


     while self.nivel in niveles and self.experiencia >= niveles[self.nivel]:

        self.nivel += 1

        self.daño += 1

        self.vida_maxima += 5

        self.vida += 20

        if self.vida > self.vida_maxima:
            self.vida = self.vida_maxima


        self.registro.append(
            f"⭐ Has subido al nivel {self.nivel}"
        )

        self.registro.append(
            "⚔️ +1 daño"
        )

        self.registro.append(
            "❤️ +5 vida máxima"
        )

        self.registro.append(
            "🧪 Recuperas 20 de vida"
        )


     if self.nivel >= 10:

        self.nivel = 10
                  
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