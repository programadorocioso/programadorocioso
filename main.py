import os
from verificar_cotacao import cotacao
from modulo_arquivo import leitura_escrita_excell, ler_para_lista, xlsx_para_pdf
from datetime import datetime
def leitor():
    ativos = input("Nome do(s) ativo(s) no Google Finance: ").split()
    dados_planilha = []
    data_hora = datetime.now().strftime("%d/%m/%Y / %H:%M:%S")
    for ativo in ativos:
        dados_planilha.append([ativo.upper(),cotacao(ativo),data_hora])
    return dados_planilha
def main ():
    leitura_escrita_excell(leitor())
    xlsx_para_pdf()
main()