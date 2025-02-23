from flask import Flask, render_template, jsonify, session, request

app = Flask("Encuestas")
app.secret_key = "xxxx"


def _parser(text_name:str) -> str:
    if not text_name.endswith(".txt"):
        text_name += ".txt"

    with open(f"{text_name}", "r") as file:
        bloques = file.read().split("\n\n")[:-1]

    for bloque in bloques:
        info = bloque.split("\n")

        preguntas = info[0]
        codigos = info[1]

        puntuaciones = tuple()


    return preguntas, puntuaciones, 


def _calc_stats(stats:list) -> list:
    p_gced, p_gia, p_gei = list(map(int, stats))
    gced += p_gced
    gia += p_gia
    gei += p_gei
    #si lo hacemos así, hay que llamar a _calc_stats cuando el usuario haya respondido a todas las preguntas
    
    return gced*0.2, gia*0.2, gei*0.2


global respuestas

@app.route("/", methods=["GET", "POST"])
def home() -> str:
    preguntas, puntuaciones = _parser("preguntas.txt")

    if request.method == "GET":
        prueba_puntuaciones = {"GCED":0,
                               "GIA":0,
                               "GEI":0}

        respuestas = request.form.items()

        codigo_final = []
        for puntuacion, respuesta in zip(puntuaciones, respuestas):
            if respuesta == "d":
                codigo_final.append([k for k in puntuacion[0]])
            elif respuesta == "i":
                codigo_final.append([k for k in puntuacion[1]])
            elif respuesta == "a":
                codigo_final.append([k for k in puntuacion[2]])

        for codigo in codigo_final:
            prueba_puntuaciones["GCED"] += codigo[0]
            prueba_puntuaciones["GIA"]  += codigo[1]
            prueba_puntuaciones["GEI"]  += codigo[2]

    return render_template("index.html", preguntas=preguntas, respuestas=respuestas)


@app.route("/encuesta")
def encuesta():
    return render_template('encuesta.html')


@app.route("/guardar_respuestas", methods=["POST"])
def guardar_respuestas():
    data = request.json
    session["respuestas"] = data["respuestas"]
    return jsonify({"status": "success"})


@app.route("/resultados")
def resultados():
    respuestas = session.get("respuestas", [])
    respuestas = list(enumerate(respuestas, start=1))
    return render_template("resultados.html", respuestas=respuestas)


if __name__ == "__main__":
    app.run(debug=True)
