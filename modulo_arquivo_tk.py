from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from openpyxl import Workbook, load_workbook
import openpyxl
import os
def leitura_escrita_excell(linhas):
    if os.path.exists("cotacao.xlsx"):
        planilha = load_workbook(filename="cotacao.xlsx")
        celula = planilha.active
        celula.column_dimensions['A'].widht = 20
        celula.column_dimensions['B'].widht = 20
        celula.column_dimensions['C'].widht = 60
        #print("Arquivo lido")
        for linha in linhas:
            planilha.active.append(linha)
        #print("Arquivo atualizado")
    else:
        #print("Arquivo inexistente")
        planilha = Workbook()
        celula = planilha.active
        celula.column_dimensions['A'].widht = 20
        celula.column_dimensions['B'].widht = 20
        celula.column_dimensions['C'].widht = 60
        celula.append(["Ativo","Valor","Data e hora da Consulta"])
        for linha in linhas:
            celula = planilha.active
            celula.append(linha)
        #print("Arquivo criado com sucesso")
    planilha.save("cotacao.xlsx")
def ler_para_lista():
    planilha = load_workbook("cotacao.xlsx")
    celula_ativa = planilha.active
    linhas = []
    for row in celula_ativa.iter_rows():
        linha = []
        for celula in row:
            linha.append(celula.value)
        linhas.append(linha)
    return linhas
def xlsx_para_pdf():
    if os.path.exists("cotacao.xlsx"):
        dados = ler_para_lista()
        documento = SimpleDocTemplate("cotacao.pdf", pagesize=letter)
        tabela = Table(dados)
        documento.build([tabela])