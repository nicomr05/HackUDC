from flask import Flask, render_template

app = Flask("Pagina")
app.secret_key = "gcedgeigia"


def _parser(text_name:str) -> str:
    if not text_name.endswith(".txt"):
        text_name += ".txt"

    with open(f"{text_name}", "r") as file:
        paquetes = file.read().split("\n\n")[:-1]
        preguntas = paquetes.split("\n")[::2] #mantiene solo los elementos pares de la lista
        puntuaciones = paquetes.split("\n")[1::2]

    preguntas = []
    points = []
    for i in range(len(filas)):
        if i%2 == 0:
            preguntas.append(filas[i])
        else:
            puntuaciones.append(tuple(filas[i].split(" ")))

    return preguntas, points

gced = []
gia = []
gei = []
def _calc_stats(stats:list) -> list:
    p_gced, p_gia, p_gei = list(map(int, puntuaciones))
    gced
    
        
    return stats


@app.route("/", methods=["GET", "POST"])
def home() -> str:
    preguntas, puntuaciones = _parser("preguntas.txt")
    return render_template("pagina_principal.html", lista = preguntas)


@app.route("/encuesta")
def encuesta():
    return render_template('encuesta.html')  # Página principal con la encuesta


@app.route("/guardar_respuestas", methods=["POST"])
def guardar_respuestas():
    data = request.json
    session["respuestas"] = data["respuestas"]  # Guardar respuestas en sesión
    return jsonify({"status": "success"})


@app.route("/resultados")
def resultados():
    respuestas = session.get("respuestas", [])
    respuestas = list(enumerate(respuestas, start=1))  # Enumerar antes de enviarlo a la plantilla
    return render_template("resultados.html", respuestas=respuestas)


if __name__ == "__main__":
    app.run(debug=True)