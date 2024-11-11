from flask import Flask, jsonify
from flask_cors import CORS
from rotas.livros import livros_blueprint
from rotas.impressao import impressao_blueprint
from rotas.grafica import grafica_blueprint

app = Flask(__name__)

CORS(app, origins="*")


@app.route("/", methods=["GET"])
def get_autor():
    return jsonify("It's alive"), 200


app.register_blueprint(livros_blueprint)
app.register_blueprint(impressao_blueprint)
app.register_blueprint(grafica_blueprint)

app.run("0.0.0.0", port=8000, debug=False)
