#Flask eh a propria classe do flask 
#Response eh uma classe pra fazer retorno da api
#request eh pra pegar os dados da requisicao

from webscrapping import cotacao
from flask import Flask, Response, request, jsonify
import json 

app = Flask(__name__)

@app.route('/cotacao/de=<moeda_um>&para=<moeda_dois>', methods=["GET"])
def cotacao_moeda(moeda_um, moeda_dois):
    return jsonify(cotacao(de=moeda_um, para=moeda_dois))


if __name__ == "__main__":
    app.run(debug=true)
