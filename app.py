from flask import Flask, render_template
import random

from jugador import Jugador
from enemigos import (
    Lobo,
    Goblin,
    Serpiente,
    Esqueleto
)
from personaje import efectos


app = Flask(__name__)


# EFECTOS DEL JUGADOR

efectos_jugador = efectos(0,0,0,0,0)



# CREAR JUGADOR

jugador = Jugador(
    "Semidios Axel",
    100,
    100,
    20,
    1,
    3,
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



# CREAR ENEMIGOS

def crear_enemigo():

    enemigos = [

        Lobo(
            "Lobo",
            60,
            10,
            20,
            30
        ),

        Goblin(
            "Goblin",
            50,
            8,
            15,
            20
        ),

        Serpiente(
            "Serpiente",
            40,
            12,
            25,
            35
        ),

        Esqueleto(
            "Esqueleto",
            80,
            15,
            30,
            50
        )

    ]

    return random.choice(enemigos)



# ENEMIGO INICIAL

enemigo = crear_enemigo()


mensaje = f"🐺 Aparece un {enemigo.nombre}"



@app.route("/")
def inicio():

    return render_template(
        "juego.html",
        jugador=jugador,
        enemigo=enemigo,
        mensaje=mensaje
    )



@app.route("/atacar", methods=["POST"])
def atacar():

    global mensaje
    global historial


    if enemigo.vida > 0:

        vida_antes = enemigo.vida

        jugador.atacar(enemigo)


        daño = vida_antes - enemigo.vida


        historial.append(
            f"⚔️ {jugador.nombre} hace {daño} de daño a {enemigo.nombre}"
        )


        if enemigo.vida <= 0:

            enemigo.vida = 0

            historial.append(
                f"🏆 Has derrotado al {enemigo.nombre}"
            )


        else:

            daño_recibido = 10

            historial.append(
                f"🐺 {enemigo.nombre} contraataca"
            )


        mensaje = "⚔️ Combate realizado"


    else:

        mensaje = "🏆 El enemigo ya está derrotado"



    return render_template(
        "juego.html",
        jugador=jugador,
        enemigo=enemigo,
        mensaje=mensaje,
        historial=historial
    )


@app.route("/curar", methods=["POST"])
def curar():

    global mensaje


    if jugador.pociones > 0:

        jugador.pociones -= 1

        jugador.vida += 20


        if jugador.vida > jugador.vida_maxima:

            jugador.vida = jugador.vida_maxima


        mensaje = "🧪 Te has curado 20 de vida"


    else:

        mensaje = "❌ No tienes pociones"



    return render_template(
        "juego.html",
        jugador=jugador,
        enemigo=enemigo,
        mensaje=mensaje
    )



@app.route("/nuevo", methods=["POST"])
def nuevo():

    global enemigo
    global mensaje


    enemigo = crear_enemigo()


    mensaje = f"🐺 Aparece un {enemigo.nombre}"
    historial = []


    return render_template(
        "juego.html",
        jugador=jugador,
        enemigo=enemigo,
        mensaje=mensaje
    )



if __name__ == "__main__":

    app.run()