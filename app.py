from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "RPG Agus funcionando"

if __name__ == "__main__":
    app.run()