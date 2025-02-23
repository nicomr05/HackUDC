from flask import Flask, render_template, jsonify, session, request
from json import load


app = Flask("Encuestas")
app.secret_key = "xxxx"

class InfoManager():
    def __init__(self, file_name:str) -> None:
        self.__info = self.__infoParser(file_name)
        self.__preguntas =     [lote["Pregunta"] for lote in self.info]
        self.__puntuaciones =   [(lote["Desacuerdo"],
                                  lote["Indiferencia"],
                                  lote["Acuerdo"]) for lote in self.info]
        self.prueba_puntuaciones = [0,0,0]
        self.respuestas = []

    def __infoParser(self, name:str) -> str:
        if not name.endswith(".json"):
            name += ".json"

        with open(name, "r") as json_file:
            info = load(json_file)

        return info


    def add(self, score:str):
        for i in range(3):
            self.prueba_puntuaciones[i] += 1


    def calculateStats(self) -> list:
        return [i for i in self.prueba_puntuaciones]


    @property
    def info(self) -> list:
        return self.__info

    @property
    def preguntas(self) -> list:
        return self.__preguntas
    
    @property
    def puntuaciones(self) -> list:
        return self.__puntuaciones


MGR = InfoManager("preguntas.json")


@app.route("/", methods=["GET", "POST"])
def home() -> str:

    return render_template("index.html")


@app.route("/encuesta")
def encuesta():
    if request.method == "GET":
        respuestas = request.form.items()
        respuestas = [i[1] for i in respuestas]
        for puntuacion, respuesta in zip(MGR.puntuaciones, respuestas):
            if respuesta == "d":
                MGR.add(puntuacion[0])
            elif respuesta == "i":
                MGR.add(puntuacion[1])
            elif respuesta == "a":
                MGR.add(puntuacion[2])
            
            MGR.respuestas.append(respuesta)

    return render_template('encuesta.html', preguntas=MGR.preguntas)


@app.route("/guardar_respuestas", methods=["POST"])
def guardar_respuestas():
    data = request.json
    session["respuestas"] = data["respuestas"]
    return jsonify({"status": "success"})


@app.route("/resultados")
def resultados():
    return render_template("resultados.html", estadisticas=MGR.calculateStats(), respuestas=MGR.respuestas)


if __name__ == "__main__":
    app.run(debug=True, port=5050)
    #MGR = InfoManager("preguntas.json")
    #MGR.add(1)
    #print(MGR.prueba_puntuaciones)
