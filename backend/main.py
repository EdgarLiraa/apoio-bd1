from flask import Flask, jsonify
from flask_cors import CORS
from rotas.example import example_blueprint

app = Flask(__name__)

CORS(app, origins="*")


@app.route("/", methods=["GET"])
def get_autor():
    """ Rota genérica """
    return jsonify("It's alive"), 200


app.register_blueprint(example_blueprint)

app.run("0.0.0.0", port=8000, debug=False)
