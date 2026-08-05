from personaje import Personajes
import random
class Goblin(Personajes):
    def __init__(self,nombre,vida,daño,oro,experiencia):
        super(). __init__(nombre,vida,daño,oro,experiencia)
    def ataque_esp(self,jugador):
        pass
    def esquive(self,jugador):
        pass
    def recibir_daño(self,jugador,daño):
        jugador.vida -= daño
        print("la", jugador.nombre,"ha recibido", daño, "de daño")
class Serpiente(Personajes):
    def __init__(self,nombre,vida,daño,oro,experiencia):
        super(). __init__(nombre,vida,daño,oro,experiencia)
    def ataque_esp(self,jugador):
        if random.randint(1,4) == 4:
            print("la serpiente te ha envenenado")
            jugador.efectos.envenenado = 3
    def esquive(self,jugador):
        pass
    def recibir_daño(self,jugador,daño):
        jugador.vida -= daño
        print("la", jugador.nombre,"ha recibido", daño, "de daño")
class Dragon(Personajes):
    def __init__(self,nombre,vida,daño,oro,experiencia):
        super(). __init__(nombre,vida,daño,oro,experiencia)
    def ataque_esp(self,jugador):
        if random.randint(1,4) == 4:
            print("el dragon te ha quemado")
            jugador.efectos.quemado = 2
    def esquive(self,jugador):
        pass
    def recibir_daño(self,jugador,daño):
        jugador.vida -= daño
        print("la", jugador.nombre,"ha recibido", daño, "de daño")
class Esqueleto(Personajes):
    def __init__(self,nombre,vida,daño,oro,experiencia):
        super(). __init__(nombre,vida,daño,oro,experiencia)
    def ataque_esp(self,jugador):
            pass
    def esquive(self,jugador):
        pass
    def recibir_daño(self,jugador,daño):
        jugador.vida -= daño
        print("la", jugador.nombre,"ha recibido", daño, "de daño")
class Lobo(Personajes):
    def __init__(self,nombre,vida,daño,oro,experiencia):
        super(). __init__(nombre,vida,daño,oro,experiencia)
    def ataque_esp(self,jugador):
        if random.randint(1,2) == 2:
            print("el lobo te ataca otra vez")
            daño_L = None
            daño_L = random.randint(1,15)
            print("el lobo te hace", daño_L," de daño")
            jugador.vida -= daño_L
    def esquive(self,jugador):
        pass
    def recibir_daño(self,jugador,daño):
        jugador.vida -= daño
        print("la", jugador.nombre,"ha recibido", daño, "de daño")
class Araña(Personajes):
    def __init__(self,nombre,vida,daño,oro,experiencia):
        super(). __init__(nombre,vida,daño,oro,experiencia)
    def ataque_esp(self,jugador):
        if random.randint(1,4) == 4:
            print("la araña te atrapa en su telaraña")
            jugador.efectos.atrapado += 1
    def esquive(self,jugador):
        pass
    def recibir_daño(self,jugador,daño):
        jugador.vida -= daño
        print("la", jugador.nombre,"ha recibido", daño, "de daño")
class Escorpion(Personajes):
    def __init__(self,nombre,vida,daño,oro,experiencia):
        super(). __init__(nombre,vida,daño,oro,experiencia)
    def ataque_esp(self,jugador):
        if random.randint(1,4) == 4:
            print("el escorpion te ha envenenado")
            jugador.efectos.envenenado_F = 3
    def esquive(self,jugador):
        pass
    def recibir_daño(self,jugador,daño):
        jugador.vida -= daño
        print("la", jugador.nombre,"ha recibido", daño, "de daño")
class Mantis(Personajes):
    def __init__(self,nombre,vida,daño,oro,experiencia):
        super(). __init__(nombre,vida,daño,oro,experiencia)
    def ataque_esp(self,jugador):
        pass
    def esquive(self,jugador):
        jugador.esquive_1 += 1
        print("la mantis es propensa a esquivar tus ataques")
    def recibir_daño(self,jugador,daño):
        jugador.vida -= daño
        print("la", jugador.nombre,"ha recibido", daño, "de daño")
class Fantasma(Personajes):
    def __init__(self,nombre,vida,daño,oro,experiencia):
        super(). __init__(nombre,vida,daño,oro,experiencia)
    def ataque_esp(self,jugador):
        pass
    def esquive(self,jugador):
        print("el fantasma es intangible la mayor parte del tiempo")
        jugador.esquive_2 += 1
    def recibir_daño(self,jugador,daño):
        jugador.vida -= daño
        print("la", jugador.nombre,"ha recibido", daño, "de daño")
class OUROBOROS(Personajes):
    def __init__(self,nombre,vida,daño,oro,experiencia):
        super(). __init__(nombre,vida,daño,oro,experiencia)
    def ataque_esp(self,jugador):
        ataque_ouroboros = None
        ataque_ouroboros = random.randint(1,4)
        if ataque_ouroboros == 1:
            print("el ouroboros te ha quemado con su aliento de fuego")
            jugador.efectos.quemado = 2
        if ataque_ouroboros == 2:
            print("la ouroboros te ha envenenado")
            jugador.efectos.envenenado_F = 3
        if ataque_ouroboros == 3:
            print("el ouroboros te congela con su mirada")
            jugador.efectos.congelado = 2   
        if ataque_ouroboros == 4:
            recoil = None
            recoil = random.randint(1,20)
            print("el golpe del ouroboros te manda volando haciendo", recoil, "puntos de daño")
            jugador.vida -= recoil
    def esquive(self,jugador):
        pass
    def recibir_daño(self,jugador,daño):
        jugador.vida -= daño
        print("la", jugador.nombre,"ha recibido", daño, "de daño")
    