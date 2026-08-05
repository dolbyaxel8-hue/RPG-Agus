from flask import Flask, render_template, request
from jugador import Jugador
from enemigos import Lobo
from personaje import efectos

app = Flask(__name__)


# Crear efectos
efectos_jugador = efectos()


# Crear jugador
jugador = Jugador(
    "Semidios Axel",
    100,      # vida
    100,      # vida maxima
    20,       # daño
    1,        # nivel
    3,        # pociones
    0,        # oro
    0,        # experiencia
    0,        # defensa
    [],       # inventario
    1,        # piso
    0,        # esquive1
    0,        # esquive2
    0,        # Ouroboros
    efectos_jugador
)


# Crear enemigo
enemigo = Lobo(
    "Lobo",
    60,
    10,
    20,
    30
)


mensaje = "Un lobo aparece..."


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

    daño = jugador.daño

    jugador.hacer_daño(enemigo, daño)

    mensaje = f"Has hecho {daño} de daño al {enemigo.nombre}"

    return render_template(
        "juego.html",
        jugador=jugador,
        enemigo=enemigo,
        mensaje=mensaje
    )


@app.route("/curar", methods=["POST"])
def curar():

    global mensaje

    if jugador.pociones > 0:
        jugador.pociones -= 1
        jugador.vida += 20

        if jugador.vida > jugador.vida_maxima:
            jugador.vida = jugador.vida_maxima

        mensaje = "Te has curado 20 puntos ❤️"

    else:
        mensaje = "No tienes pociones"

    return render_template(
        "juego.html",
        jugador=jugador,
        enemigo=enemigo,
        mensaje=mensaje
    )


if __name__ == "__main__":
    app.run()