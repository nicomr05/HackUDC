from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)
app.secret_key = "clave_secreta"  # Necesario para guardar datos en sesión

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encuesta')
def encuesta():
    return render_template('encuesta.html')  # Página principal con la encuesta

@app.route('/guardar_respuestas', methods=['POST'])
def guardar_respuestas():
    data = request.json
    session['respuestas'] = data['respuestas']  # Guardar respuestas en sesión
    return jsonify({"status": "success"})

@app.route('/resultados')
def resultados():
    respuestas = session.get('respuestas', [])
    respuestas = list(enumerate(respuestas, start=1))  # Enumerar antes de enviarlo a la plantilla
    return render_template('resultados.html', respuestas=respuestas)


if __name__ == '__main__':
    app.run(debug=True)
