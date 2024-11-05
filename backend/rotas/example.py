from flask import Blueprint, jsonify, request

from servicos.example import ExampleDatabase


example_blueprint = Blueprint("example", __name__)


@example_blueprint.route("/example_generico", methods=["GET"])
def get_generico():
    return (
        jsonify(ExampleDatabase().get_generico_com_algum_parametro()),
        200,
    )  # Get Genérico


@example_blueprint.route("/post-generico", methods=["POST"])
def post_generico():
    json = request.get_json()  # Json da request
    data = json.get("data")  # Parametro do Json
    isbn = json.get("isbn")  # Parametro do Json
    grafica_id = json.get("grafica")  # Parametro do Json
    nto_copias = json.get("copias")  # Parametro do Json
    registro = ExampleDatabase().insercao_generica(
        isbn, grafica_id, nto_copias, data
    )  # Chama Controller Para inserção

    if not registro:  # Falha ao Inserir no DB
        return jsonify("Não foi possível solicitar a impressão"), 400

    return jsonify("Impressao requisitada"), 200  # Sucesso ao inserir no DB


@example_blueprint.route("/filtro-generico", methods=["POST"])
def get_com_filtro():
    rg = request.args.get(
        "rg", ""
    )  # Pega Query Params, se não houver retorna string vazia
    editora = request.args.get("editora", "")
    livro = request.args.get("livro", "")
    return (
        jsonify(ExampleDatabase().get_com_filtro(rg, editora, livro)),
        200,
    )  # Assume-se que não existem erros e sempre retorna algo
