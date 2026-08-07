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
        jugador.registro.append(
    f"👹 {jugador.nombre} recibe {daño} de daño"
)
class Serpiente(Personajes):
    def __init__(self,nombre,vida,daño,oro,experiencia):
        super(). __init__(nombre,vida,daño,oro,experiencia)
    def ataque_esp(self,jugador):
        if random.randint(1,4) == 4:
            jugador.registro.append(
            "🐍 La serpiente te ha envenenado"
        )
            jugador.efectos.envenenado = 3
    def esquive(self,jugador):
        pass
    def recibir_daño(self,jugador,daño):
        jugador.vida -= daño
        jugador.registro.append(
    f"👹 {jugador.nombre} recibe {daño} de daño"
)
class Dragon(Personajes):
    def __init__(self,nombre,vida,daño,oro,experiencia):
        super(). __init__(nombre,vida,daño,oro,experiencia)
    def ataque_esp(self,jugador):
        if random.randint(1,4) == 4:
            jugador.registro.append(
    "🐉 El dragón te ha quemado"
)
            jugador.efectos.quemado = 2
    def esquive(self,jugador):
        pass
    def recibir_daño(self,jugador,daño):
        jugador.vida -= daño
        jugador.registro.append(
    f"👹 {jugador.nombre} recibe {daño} de daño"
)
class Esqueleto(Personajes):
    def __init__(self,nombre,vida,daño,oro,experiencia):
        super(). __init__(nombre,vida,daño,oro,experiencia)
    def ataque_esp(self,jugador):
            pass
    def esquive(self,jugador):
        pass
    def recibir_daño(self,jugador,daño):
        jugador.vida -= daño
        jugador.registro.append(
    f"👹 {jugador.nombre} recibe {daño} de daño"
)
class Lobo(Personajes):
    def __init__(self,nombre,vida,daño,oro,experiencia):
        super(). __init__(nombre,vida,daño,oro,experiencia)
    def ataque_esp(self,jugador):
        if random.randint(1,2) == 2:
            jugador.registro.append(
    "🐺 El lobo te ataca otra vez"
)
            daño_L = None
            daño_L = random.randint(1,15)
            jugador.registro.append(
    f"🐺 El lobo hace {daño_L} de daño extra"
)
            jugador.vida -= daño_L
    def esquive(self,jugador):
        pass
    def recibir_daño(self,jugador,daño):
        jugador.vida -= daño
        jugador.registro.append(
    f"👹 {jugador.nombre} recibe {daño} de daño"
)
class Araña(Personajes):
    def __init__(self,nombre,vida,daño,oro,experiencia):
        super(). __init__(nombre,vida,daño,oro,experiencia)
    def ataque_esp(self,jugador):
        if random.randint(1,4) == 4:
            jugador.registro.append(
    "🕷️ La araña te atrapa en su telaraña"
)
            jugador.efectos.atrapado += 1
    def esquive(self,jugador):
        pass
    def recibir_daño(self,jugador,daño):
        jugador.vida -= daño
        jugador.registro.append(
    f"👹 {jugador.nombre} recibe {daño} de daño"
)
class Escorpion(Personajes):
    def __init__(self,nombre,vida,daño,oro,experiencia):
        super(). __init__(nombre,vida,daño,oro,experiencia)
    def ataque_esp(self,jugador):
        if random.randint(1,4) == 4:
            jugador.registro.append(
                " El escorpión te ha envenenado"
            )
            jugador.efectos.envenenado_F = 3
    def esquive(self,jugador):
        pass
    def recibir_daño(self,jugador,daño):
        jugador.vida -= daño
        jugador.registro.append(
    f"👹 {jugador.nombre} recibe {daño} de daño"
)
class Mantis(Personajes):
    def __init__(self,nombre,vida,daño,oro,experiencia):
        super(). __init__(nombre,vida,daño,oro,experiencia)
    def ataque_esp(self,jugador):
        pass
    def esquive(self,jugador):
        jugador.esquive1 += 1
        jugador.registro.append(
    "🦗 La mantis se prepara para esquivar ataques"
)
    def recibir_daño(self,jugador,daño):
        jugador.vida -= daño
        jugador.registro.append(
    f"👹 {jugador.nombre} recibe {daño} de daño"
)
class Fantasma(Personajes):
    def __init__(self,nombre,vida,daño,oro,experiencia):
        super(). __init__(nombre,vida,daño,oro,experiencia)
    def ataque_esp(self,jugador):
        pass
    def esquive(self,jugador):
        jugador.registro.append(
    "👻 El fantasma se vuelve intangible"
)
        jugador.esquive2 += 1
    def recibir_daño(self,jugador,daño):
        jugador.vida -= daño
        jugador.registro.append(
    f"👹 {jugador.nombre} recibe {daño} de daño"
)
class OUROBOROS(Personajes):
    def __init__(self,nombre,vida,daño,oro,experiencia):
        super(). __init__(nombre,vida,daño,oro,experiencia)
    def ataque_esp(self,jugador):
        ataque_ouroboros = None
        ataque_ouroboros = random.randint(1,4)
        if ataque_ouroboros == 1:
            jugador.registro.append(
    "🐍 Ouroboros te ha quemado con su aliento de fuego"
)
            jugador.efectos.quemado = 2
        if ataque_ouroboros == 2:
            jugador.registro.append(
    "🐍 Ouroboros te ha envenenado con sus colmillos"
)
            jugador.efectos.envenenado_F = 3
        if ataque_ouroboros == 3:
            jugador.registro.append(
    "🐍 Ouroboros te ha congelado con su mirada"
)
            jugador.efectos.congelado = 2   
        if ataque_ouroboros == 4:
            recoil = None
            recoil = random.randint(1,20)
            jugador.registro.append(
        f"🐍 El golpe de Ouroboros te manda volando y hace {recoil} de daño"
    )
            jugador.vida -= recoil
    def esquive(self,jugador):
        pass
    def recibir_daño(self,jugador,daño):
        jugador.vida -= daño
        jugador.registro.append(
    f"👹 {jugador.nombre} recibe {daño} de daño"
)
    