from bs4 import BeautifulSoup, BeautifulStoneSoup
import requests

def cotacao(de, para):
    html = requests.get(f"https://www.google.com/finance/quote/{de}-{para}")
    soup = BeautifulSoup(html.text, 'html.parser')
    valor = soup.select('[class="YMlKec fxKbKc"]')
    if type(valor) != list:
        return "Moeda nao encontrada" 
    valor = float(valor[0].text)
    result = {"O valor de 1": de, "Para":para, "Valor": round(valor, 2)}
    return result
