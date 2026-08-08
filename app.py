from flask import Flask, render_template, request, redirect, url_for
import random
import copy

from jugador import Jugador
from enemigos import (
    Goblin,
    Serpiente,
    Dragon,
    Esqueleto,
    Lobo,
    Araña,
    Escorpion,
    Mantis,
    Fantasma,
    OUROBOROS
)

from personaje import efectos
from objetos import espada_madera1, espada_hierro1, espada_diamante1,lupa1,armadura_bronce1,armadura_hierro1,armadura_diamante1,escama_ouroboros1,items

from tienda import (vendedora_ambulante1,tienda_normal1,tienda_epica1,tiendas1,
    tiendas2,
    tiendas3,
    tiendas4,
    tiendas5,
    tiendas_O
)


app = Flask(__name__)


# ==========================
# CREAR CLASES
# ==========================

efectos_jugador = efectos(0,0,0,0,0)


clases = {

    "exploradora": Jugador(
        "Exploradora",
        120,
        120,
        15,
        1,
        2,
        0,
        0,
        0,
        [],
        1,
        0,
        0,
        0,
        efectos_jugador
    ),


    "guerrera": Jugador(
        "Guerrera",
        90,
        90,
        20,
        1,
        1,
        0,
        0,
        0,
        [],
        1,
        0,
        0,
        0,
        efectos_jugador
    ),


    "semidiosa": Jugador(
        "Semidiosa",
        120,
        120,
        20,
        1,
        2,
        0,
        0,
        0,
        [],
        1,
        0,
        0,
        0,
        efectos_jugador
    )

}


jugador = None
enemigo = None
tienda_actual = None

mensaje = ""
historial = []

piso = 1

combates = 0
combates_piso = 0
exploraciones_sin_tienda = 0

# ==========================
# CREAR ENEMIGO
# ==========================

def sumar_combate():
    global piso

    global combates
    global combates_piso

    combates += 1
    combates_piso += 1

    comprobar_piso()
def crear_enemigo():

    if piso == 1:

        enemigos = [

            Lobo("Lobo",35,12,10,28),
            Goblin("Goblin",25,8,10,10),
            Serpiente("Serpiente",28,10,10,18)

        ]


    elif piso == 2:

        enemigos = [

            Lobo("Lobo",42,15,15,35),
            Araña("Araña",42,12,20,40),
            Esqueleto("Esqueleto",50,16,20,55)

        ]


    elif piso == 3:

        enemigos = [

            Araña("Araña",42,18,30,70),
            Escorpion("Escorpión",58,24,30,75),
            Esqueleto("Esqueleto",60,18,40,90)

        ]


    elif piso == 4:

        enemigos = [

            Mantis("Mantis",43,23,50,120),
            Dragon("Dragón",58,25,60,180)

        ]


    elif piso == 5:

        enemigos = [

            Dragon("Dragón",63,25,100,250),
            Fantasma("Fantasma",32,25,50,100)

        ]


    else:

        enemigos = []


    return copy.copy(random.choice(enemigos))



# ==========================
# PISOS
# ==========================


def comprobar_piso():

    global piso
    global mensaje
    global combates_piso

    if combates_piso >= 5 and piso == 1:
        jugador.registro.clear()

        piso = 2
        jugador.piso = 2
        combates_piso = 0
        mensaje = """
        ⭐ NUEVO PISO ⭐<br>
        🏰 PISO II<br>
        LAS GALERÍAS OLVIDADAS
        """


    elif combates_piso >= 5 and piso == 2:
        jugador.registro.clear()

        piso = 3
        jugador.piso = 3
        combates_piso = 0
        mensaje = """
        ⭐ NUEVO PISO ⭐<br>
        🏰 PISO III<br>
        LAS CATACUMBAS MALDITAS
        """


    elif combates_piso >= 5 and piso == 3:
        jugador.registro.clear()

        piso = 4
        jugador.piso = 4
        combates_piso = 0
        mensaje = """
        ⭐ NUEVO PISO ⭐<br>
        🏰 PISO IV<br>
        LOS SALONES DEL ABISMO
        """


    elif combates_piso >= 5 and piso == 4:
        jugador.registro.clear()

        piso = 5
        jugador.piso = 5
        combates_piso = 0
        mensaje = """
        ⭐ NUEVO PISO ⭐<br>
        🐉 EL TRONO DEL DRAGÓN
        """


    elif combates_piso >= 5 and piso == 5:
        jugador.registro.clear()

        piso = 6
        jugador.piso = 6
        combates_piso = 0
        mensaje = """
        🐍 PISO FINAL<br>
        ⚔️ EL OUROBOROS TE ESPERA
        """



# ==========================
# INICIO
# ==========================


@app.route("/")
def inicio():

    return render_template(
        "inicio.html"
    )


@app.route("/seleccionar")
def seleccionar():

    return render_template("seleccionar.html")
@app.route("/elegir", methods=["POST"])
def elegir():

    global jugador
    global mensaje

    clase = request.form["clase"]

    jugador = copy.deepcopy(clases[clase])
    for objeto in items.values():
     objeto.comprado = 0

    mensaje = "🌙 Una nueva aventura comienza..."

    return redirect(
        url_for("mazmorra")
    )


# ==========================
# MAZMORRA
# ==========================
@app.route("/comenzar")
def comenzar():

    return redirect(
        url_for("mazmorra")
    )
@app.route("/intro")
def intro():
    import os
    print(os.getcwd())

    return render_template("intro.html")
@app.route("/elegir_personaje")
def elegir_personaje():

    return render_template("inicio.html")
@app.route("/elegir_clase", methods=["POST"])
def elegir_clase():

    global jugador
    global mensaje

    clase = request.form["clase"]

    jugador = copy.deepcopy(
        clases[clase]
    )

    mensaje = "🌙 Una nueva aventura comienza..."

    return redirect(
        url_for("mazmorra")
    )
@app.route("/mazmorra")
def mazmorra():

    return render_template(
        "juego.html",
        jugador=jugador,
        enemigo=None,
        mensaje=mensaje,
        registro=list(jugador.registro)
    )
@app.route("/tienda")
def tienda():

    global tienda_actual

    if tienda_actual is None:
        return redirect(url_for("mazmorra"))

    return render_template(
        "tienda.html",
        jugador=jugador,
        tienda=tienda_actual,
        items=items
    )
@app.route("/comprar/<nombre>")
def comprar(nombre):

    global tienda_actual

    # ==========================
    # POCIONES
    # ==========================

    if nombre == "pociones":

        if jugador.oro >= 30:

            jugador.oro -= 30
            jugador.pociones += 1

            jugador.registro.clear()
            jugador.registro.append("🧪 Has comprado una poción")

        else:

            jugador.registro.clear()
            jugador.registro.append("❌ No tienes suficiente oro")

        return redirect(url_for("tienda"))

    # ==========================
    # RESTO DE OBJETOS
    # ==========================

    objeto = items[nombre]

    if objeto.comprado == 1:

        jugador.registro.clear()
        jugador.registro.append("❌ Ya has comprado este objeto")

        return redirect(url_for("tienda"))

    if jugador.oro < objeto.precio:

        jugador.registro.clear()
        jugador.registro.append("❌ No tienes suficiente oro")

        return redirect(url_for("tienda"))

    jugador.oro -= objeto.precio

    objeto.usar(jugador)

    objeto.comprado = 1

    jugador.registro.clear()
    jugador.registro.append(f"🛒 Has comprado {objeto.nombre}")

    return redirect(url_for("tienda"))
@app.route("/salir_tienda")
def salir_tienda():

    global tienda_actual

    tienda_actual = None

    jugador.registro.clear()

    jugador.registro.append(
        "🚪 Has salido de la tienda"
    )

    return redirect(url_for("mazmorra"))
@app.route("/avanzar", methods=["POST"])
def avanzar():

    global enemigo
    global mensaje
    global combates
    global combates_piso
    global tienda_actual
    global exploraciones_sin_tienda
    jugador.registro.clear()
    exploraciones_sin_tienda += 1
    sumar_combate()

    if "NUEVO" in mensaje:

     jugador.registro.append(mensaje)

     mensaje = ""

     return redirect(
        url_for("mazmorra"))

    

    # ======================
    # EVENTOS ALEATORIOS
    # ======================

    evento = random.randint(1,10)


    if evento == 10:

     oro = random.randint(10,60)

     jugador.oro += oro
     jugador.registro.clear()

     jugador.registro.append(
        "🧰 Has encontrado un cofre"
     )

     jugador.registro.append(
        f"💰 Has conseguido {oro} de oro"
     )

     return redirect(
        url_for("mazmorra")
     )
    # ======================
    # TIENDA
    # ======================

    if exploraciones_sin_tienda >= 4 or random.randint(1, 5) == 5:

     if piso == 1:
        datos = tiendas1
     elif piso == 2:
        datos = tiendas2
     elif piso == 3:
        datos = tiendas3
     elif piso == 4:
        datos = tiendas4
     else:
        datos = tiendas5

     nombre = random.choices(
        datos["tiendas"],
        weights=datos["probabilidades"]
     )[0]
     exploraciones_sin_tienda = 0
     tienda_actual = tiendas_O[nombre]
     return redirect(url_for("tienda"))



    # ======================
    # ENEMIGO
    # ======================

    if piso == 6:

        enemigo = OUROBOROS(
            "Ouroboros",
            200,
            50,
            300,
            300
        )

    else:

        enemigo = crear_enemigo()

    jugador.registro.append(
    f"⚔️ Aparece {enemigo.nombre}")



    mensaje = (
        f"⚔️ Aparece {enemigo.nombre}"
    )


    return redirect(
        url_for("combate")
    )
@app.route("/combate")
def combate():

    global enemigo
    global mensaje
    if jugador.vida <= 0:

     return redirect(url_for("game_over"))

    if enemigo and enemigo.vida <= 0:

        enemigo = None

        mensaje = (
            "🏆 Victoria<br>"
            "🚪 Puedes continuar explorando"
        )


    return render_template(
        "juego.html",
        jugador=jugador,
        enemigo=enemigo,
        mensaje=mensaje,
        registro=list(jugador.registro)
    )


@app.route("/atacar", methods=["POST"])
def atacar():

    global mensaje
    global enemigo

    jugador.registro.clear()

    jugador.atacar(enemigo)
    if jugador.vida <= 0:

     jugador.vida = 0

     jugador.registro.append(
        "☠️ Has muerto..."
    )

     return redirect(
        url_for("game_over")
    )


    if enemigo.vida <= 0:
            if enemigo.nombre == "Ouroboros":
                return redirect(url_for("final"))

            enemigo = None


    jugador.registro.append(
        f"❤️ Tu vida: {jugador.vida}/{jugador.vida_maxima}"
    )


    mensaje = ""


    return redirect(
        url_for("combate")
    )
@app.route("/game_over")
def game_over():

    return render_template(
        "game_over.html",
        jugador=jugador
    )
@app.route("/curar", methods=["POST"])
def curar():

    global mensaje

    jugador.registro.clear()

    if jugador.pociones > 0:

        jugador.pociones -= 1

        vida_anterior = jugador.vida

        jugador.vida += 20

        if jugador.vida > jugador.vida_maxima:
            jugador.vida = jugador.vida_maxima


        curado = jugador.vida - vida_anterior


        jugador.registro.append(
            f"🧪 Te has curado {curado} de vida"
        )

        jugador.registro.append(
            f"❤️ Tu vida: {jugador.vida}/{jugador.vida_maxima}"
        )


    else:

        jugador.registro.append(
            "❌ No tienes pociones"
        )


    mensaje = ""

    return redirect(
        url_for("combate")
    )
@app.route("/final")
def final():

    return render_template("final.html")
@app.route("/debug")
def debug():

    global jugador

    jugador = copy.deepcopy(clases["semidiosa"])

    jugador.piso = 6
    jugador.daño = 35
    jugador.vida = 999
    jugador.vida_maxima = 999

    return redirect(url_for("test_ouroboros"))


@app.route("/test_ouroboros")
def test_ouroboros():

    global enemigo

    enemigo = OUROBOROS(
        "Ouroboros",
        120,
        30,
        300,
        300
    )

    return redirect(url_for("combate"))



if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )