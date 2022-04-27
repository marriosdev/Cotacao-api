from bs4 import BeautifulSoup, BeautifulStoneSoup
import requests

def cotacao(de, para):
    html = requests.get(f"https://www.google.com/finance/quote/{de}-{para}")
    soup = BeautifulSoup(html.text, 'html.parser')
    valor = soup.select('[class="YMlKec fxKbKc"]')
    try:
        valor = float(valor[0].text)
        result = {"Valor": valor}
        return result
    except:
        return "Ocorreu um erro"
