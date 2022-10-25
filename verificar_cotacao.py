from requests_html import HTMLSession
from bs4 import BeautifulSoup
classe_cotacao = 'YMlKec fxKbKc'
def cotacao(ativo):
    try:
        dollar = "usd-brl"
        acesso = HTMLSession()
        link = acesso.get('https://www.google.com/finance/quote/'+ativo)
        link_dollar = acesso.get('https://www.google.com/finance/quote/'+dollar)
        html = BeautifulSoup(link.text,'lxml')
        html_dollar = BeautifulSoup(link_dollar.text, 'lxml')
        valor = html.find(class_ = classe_cotacao).text
        valor_dollar = html_dollar.find(class_ = classe_cotacao).text
        if ativo == dollar.lower():
            valor = float(valor)
            retorno ='R$ '+str(f'{valor:.2f}')
            return retorno
        elif ativo == dollar.upper():
            valor = float(valor)
            retorno ='R$ '+str(f'{valor:.2f}')
            return retorno
        elif valor[0] == '$':
            valor = float(str(valor).replace('$','').replace('.', '').replace(',', '.'))
            retorno = 'USD ' + str(f'{valor:.2f}')
            return retorno
        else:
            valor = float(valor[2:])/float(valor_dollar)
            retorno = 'USD ' + str(f'{valor:.2f}')
            return retorno
    except:
        return "Código inválido"