
from webscrapping import cotacao
from flask import Flask, Response, request, jsonify

app = Flask(__name__)

@app.route('/cotacao/de=<moeda_um>&para=<moeda_dois>', methods=["GET"])
def cotacao_moeda(moeda_um, moeda_dois):
    return jsonify(cotacao(de=moeda_um, para=moeda_dois))


if __name__ == "__main__":
    app.run(debug=True)