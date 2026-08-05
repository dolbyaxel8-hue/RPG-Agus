from abc import ABC, abstractmethod
class Personajes(ABC):
    def __init__(self,nombre,vida,daño,oro,experiencia):
        self.nombre = nombre
        self.vida = vida
        self.daño = daño
        self.oro = oro
        self.experiencia = experiencia
    @abstractmethod
    def ataque_esp(self):
        pass
    @abstractmethod
    def esquive(self):
        pass
    @abstractmethod
    def recibir_daño(self):
        pass
class efectos:
    def __init__(self,envenenado,envenenado_F,quemado,congelado,atrapado):
        self.envenenado = envenenado
        self.envenenado_F = envenenado_F
        self.quemado = quemado
        self.congelado = congelado
        self.atrapado = atrapado