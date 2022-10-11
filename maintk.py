import os
import tkinter as tk
from tkinter import StringVar
from verificar_cotacao import cotacao
from modulo_arquivo_tk import leitura_escrita_excell, ler_para_lista, xlsx_para_pdf
from datetime import datetime
from functools import partial
def main_func(ativos):
    ativos = var.get()
    ativos = ativos.split()
    #print(ativos)
    dados_planilha = []
    data_hora = datetime.now().strftime("%d/%m/%Y / %H:%M:%S")
    for ativo in ativos:
        dados_planilha.append([ativo.upper(),cotacao(ativo),data_hora])
    leitura_escrita_excell(dados_planilha)
    xlsx_para_pdf()
principal = tk.Tk()
principal.geometry('350x100')
principal.title("StonksWare")
var = StringVar(principal)
entrada = var.get()
texto = "Códigos do Google Finance (separados por espaço)"
nome_botao = "Buscar cotações"
#print("Entrada: ",entrada)
nome_campo = tk.Label(principal,text=texto).grid(row=0,column=0)
campo = tk.Entry(principal,textvariable=var).grid(row=1,column=0)
botao = tk.Button(principal,text=nome_botao,command=partial(main_func,entrada)).grid(row=2,column=0)
principal.mainloop()