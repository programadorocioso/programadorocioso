import tkinter as tk
from tkinter import StringVar
from verificar_cotacao import cotacao
from modulo_arquivo_tk import leitura_escrita_excell, xlsx_para_pdf
from datetime import datetime
from functools import partial
import base64
from icone import imagem
from os import remove
imagem_icone = base64.b64decode(imagem())
tmpfl = "icon.ico"
iconfl = open(tmpfl,'wb')
iconfl.write(imagem_icone)
iconfl.close()
def main_func(ativos):
    ativos = var.get()
    ativos = ativos.split()
    dados_planilha = []
    data_hora = datetime.now().strftime("%d/%m/%Y / %H:%M:%S")
    for ativo in ativos:
        dados_planilha.append([ativo.upper(),cotacao(ativo),data_hora])
    leitura_escrita_excell(dados_planilha)
    xlsx_para_pdf()
principal = tk.Tk()
principal.iconbitmap(tmpfl)
remove(tmpfl)
principal.geometry('350x100')
principal.title("StonksWare")
var = StringVar(principal)
entrada = var.get()
texto = "Códigos do Google Finance (separados por espaço)"
nome_botao = "Buscar cotações"
nome_campo = tk.Label(principal,text=texto).grid(row=0,column=0)
campo = tk.Entry(principal,textvariable=var).grid(row=1,column=0)
botao = tk.Button(principal,text=nome_botao,command=partial(main_func,entrada)).grid(row=2,column=0)
principal.mainloop()