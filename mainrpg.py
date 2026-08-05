import random
import time
import copy
import json
from personaje import Personajes, efectos
from jugador import Jugador
from enemigos import Goblin, Serpiente, Dragon, Esqueleto, Lobo, Araña, Escorpion, Mantis, Fantasma, OUROBOROS
from tienda import vendedora_ambulante, tienda_normal, tienda_epica
combates = 0
combates_P = 0
def pisos():
    if combates_P >= 5 and jugadores[player].piso == 1:
     jugadores[player].piso =2
     print("╔══════════════════════════════════════╗")
     print("║              -PISO II-               ║")
     print("║        LAS GALERIAS OLVIDADAS        ║")
     print("╚══════════════════════════════════════╝")
     time.sleep(1)
     print("sientes una presencia observándote...")
    if combates_P >= 10 and jugadores[player].piso == 2:
     jugadores[player].piso =3
     print("╔══════════════════════════════════════╗")
     print("║             -PISO III-               ║")
     print("║       LAS CATACUMBAS MALDITAS        ║")
     print("╚══════════════════════════════════════╝")
     time.sleep(1)
     print("un escalofrio recorre tu espalda...")
    if combates_P >= 15 and jugadores[player].piso == 3:
     jugadores[player].piso =4
     print("╔══════════════════════════════════════╗")
     print("║              -PISO IV-               ║")
     print("║        LOS SALONES DEL ABISMO        ║")
     print("╚══════════════════════════════════════╝")
     time.sleep(1)
     print("el frio se apodera de tu cuerpo...")
    if combates_P >= 20 and jugadores[player].piso == 4:
     jugadores[player].piso =5
     print("╔══════════════════════════════════════╗")
     print("║               -PISO V-               ║")
     print("║          EL TRONO DEL DRAGON         ║")
     print("╚══════════════════════════════════════╝")
     time.sleep(1)
     print("notas la presencia de una enorme criatura...")
    if combates_P >= 25 and jugadores[player].piso == 5:
     jugadores[player].piso =6
     print("╔══════════════════════════════════════╗")
     print("║               -PISO VI-              ║")
     print("║                  FIN                 ║")
     print("╚══════════════════════════════════════╝")
     time.sleep(1)
     print("delante tuyo se encuentra el jefe final")
     print("con un escalofriante chillido, empieza la pelea")
def introduccion():
    print("╔════════════════════════════╗")
    print("║                            ║")
    print("║        RPG PARA AGUS       ║")
    print("║                            ║")
    print("╚════════════════════════════╝")
    time.sleep(2)
    print("🌙 Una nueva aventura comienza...")
    time.sleep(2)
    print("En un mundo olvidado por los dioses (Ek)")
    print("criaturas peligrosas acechan en cada rincón.")
    time.sleep(2)
    print("👹 Goblins, 🐍 bestias y 🐉 dragones")
    print("esperan a aquellas niñas valientes que se atrevan")
    print("a enfrentarse a ellos.")
    time.sleep(2)
    print("Tu objetivo es simple:")
    print("⚔️ Sobrevive")
    print("💰 Consigue riquezas")
    print("⭐ Aumenta tu poder")
    print("🏆 Salva a tu principe")
    time.sleep(2)
    print("╔══════════════════════╗")
    print("║     COMIENZA TU      ║")
    print("║      AVENTURA        ║")
    print("╚══════════════════════╝")
    time.sleep(2)
efectos1 = efectos(0,0,0,0,0)
Exploradora = Jugador("exploradora",120,120,15,1,2,0,0,0,[],1,0,0,0,efectos1)
Guerrera = Jugador("guerrera",90,90,20,1,1,0,0,0,[],1,0,0,0,efectos1)
semidiosa = Jugador("semidiosa",120,120,20,1,2,0,0,0,[],1,0,0,0,efectos1)
Dev = Jugador("dev",1,1,2,1,3,100,100,0,[],1,0,0,0,efectos1)
jugadores = {"exploradora": Exploradora, "guerrera": Guerrera, "dev": Dev, "semidiosa": semidiosa}
Goblin1 = Goblin("Goblin",20,8,5,10)
Serpiente1 = Serpiente("serpiente",28,10,5,18)
Dragon1 = Dragon("Dragon",100,35,40,180)
Esqueleto1 = Esqueleto("esqueleto",50,16,20,55)
Lobo1 = Lobo("lobo",35,12,10,28)
Araña1 = Araña("araña",42,14,20,40)
Escorpion1 = Escorpion("escorpion",58,24,30,75)
Mantis1 = Mantis("mantis",68,28,30,100)
Fantasma1 = Fantasma("fantasma",20,5,5,5)
OUROBOROS1 = OUROBOROS("ouroboros",200,50,300,300)
enemigos1 = {"enemigos": [Goblin1, Serpiente1, Lobo1], "probabilidades": [55,30,15]}
enemigos2 = {"enemigos": [Goblin1, Serpiente1, Lobo1, Araña1, Esqueleto1], "probabilidades": [30,30,20,15,5]}
enemigos3 = {"enemigos": [Serpiente1, Lobo1, Araña1, Esqueleto1, Escorpion1], "probabilidades": [25,25,20,20,10]}
enemigos4 = {"enemigos": [Lobo1, Araña1, Esqueleto1, Escorpion1, Mantis1, Dragon1], "probabilidades": [15,20,20,25,13,2]}
enemigos5 = {"enemigos": [Esqueleto1, Escorpion1, Mantis1, Dragon1,  Fantasma1], "probabilidades": [25,25,25,20,5]}
enemigos6 = {"enemigos": [OUROBOROS1], "probabilidades": [100]}
vendedora_ambulante1 = vendedora_ambulante("vendedora_ambulante", ["espada de madera, 15 de oro", "armadura de bronce, 15 de oro", "pociones, 30 de oro"])
tienda_normal1 = tienda_normal("tienda_normal", ["espada de hierro, 25 de oro", "armadura de hierro, 25 de oro", "pociones, 30 de oro"])
tienda_epica1 = tienda_epica("tienda_epica", ["espada de diamante, 40 de oro", "armadura de diamante, 40 de oro", "lupa, 30 de oro","escama de ouroboros, 150 de oro" "pociones, 30 de oro"])
tiendas1 = {"tiendas": ["vendedor_ambulante","tienda_normal","tienda_epica"], "probabilidades":[10,4,0]}
tiendas2 = {"tiendas": ["vendedor_ambulante","tienda_normal","tienda_epica"], "probabilidades":[7,6,1]}
tiendas3 = {"tiendas": ["vendedor_ambulante","tienda_normal","tienda_epica"], "probabilidades":[2,6,3]}
tiendas4 = {"tiendas": ["vendedor_ambulante","tienda_normal","tienda_epica"], "probabilidades":[1,6,3]}
tiendas5 = {"tiendas": ["vendedor_ambulante","tienda_normal","tienda_epica"], "probabilidades":[0,5,4]}
tiendas_O = {"vendedor_ambulante": vendedora_ambulante1, "tienda_normal": tienda_normal1, "tienda_epica": tienda_epica1}
introduccion()
player = input("¿que clase deseas ser, exploradora, guerrera o semidiosa?")
print("entras en la mazmorra")
time.sleep(1)
print("╔══════════════════════════════════════╗")
print("║               PISO I                 ║")
print("║       LA ENTRADA A LA MAZMORRA       ║")
print("╚══════════════════════════════════════╝")
time.sleep(1)
while True:
    if jugadores[player].vida <= 0:
       break
    if jugadores[player]. vida >0 and jugadores[player].Ouroboros_encontrado ==1:
       break
    pasillo = None
    pasillo = input("¿donde deseas ir a la izquierda o a la derecha?")
    if pasillo == "dev":
        print("a")
    else:
     time.sleep(0.5)
     jugadores[player].check_level()
     pisos()
     if jugadores[player].piso == 1:
         enemigos_P = enemigos1
         tiendas_P = tiendas1
     elif jugadores[player].piso == 2:
         enemigos_P = enemigos2
         tiendas_P = tiendas2
     elif jugadores[player].piso == 3:
         enemigos_P = enemigos3
         tiendas_P = tiendas3
     elif jugadores[player].piso == 4:
         enemigos_P = enemigos4
         tiendas_P = tiendas4
     elif jugadores[player].piso == 5:
         enemigos_P = enemigos5
         tiendas_P = tiendas5
     elif jugadores[player].piso >= 6:
        enemigos_P = enemigos6
        tiendas_P = tiendas5
     if combates == 4:
         combates = 0
         tienda = random.choices(tiendas_P["tiendas"], weights=tiendas_P["probabilidades"])[0]
         jugadores[player].tienda(tiendas_O[tienda])
     if random.randint(1, 8) == 8:
         tienda = random.choices(tiendas_P["tiendas"], weights=tiendas_P["probabilidades"])[0]
         jugadores[player].tienda(tiendas_O[tienda])
     elif random.randint(1,8) == 8:
        tesoro = None
        tesoro = random.randint(1,50)
        print("te has encontrado un tesoro con",tesoro, "de oro")
        time.sleep(1)
        jugadores[player].oro += tesoro
     enemigo = random.choices(enemigos_P["enemigos"], weights=enemigos_P["probabilidades"])[0]
     enemigo = copy.copy(enemigo)
     combates += 1
     combates_P += 1
     jugadores[player].combate(enemigo)
if jugadores[player].vida <= 0 and jugadores[player].Ouroboros_encontrado == 1:
    print("╔══════════════════════╗")
    print("║       DERROTA        ║")
    print("╚══════════════════════╝")
    print("has muerto peleando contra el ouroboros")
    time.sleep(1)
    print("el mundo confia en que puedas vencerlo, mi niña")
elif jugadores[player].vida <= 0:
        print("╔══════════════════════╗")
        print("║       DERROTA        ║")
        print("╚══════════════════════╝")
        time.sleep(1)
        print("🩷 has perdido mi niña, pero puedes volver a intentarlo 🩷")
if jugadores[player].vida > 0 and jugadores[player].Ouroboros_encontrado == 1:
        print("╔══════════════════════╗")
        print("║       VICTORIA       ║")
        print("╚══════════════════════╝")
        print("has vencido al Ouroboros")
        time.sleep(2)
        print("has salvado a tu principito")
        time.sleep(2)
        print("te amo Agus")
