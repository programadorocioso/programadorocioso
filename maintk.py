import tkinter as tk
from tkinter import StringVar
from verificar_cotacao import cotacao
from modulo_arquivo_tk import leitura_escrita_excell, xlsx_para_pdf
from datetime import datetime
from functools import partial


#import base64
#from icone import imagem
#from os import remove
#imagem_icone = base64.b64decode(imagem())
#Remover comentarios das linhas abaixo se executando no Windows
#Por algum motivo muito especifico, essas linhas causam erros apenas no Linux
#Mais especificadamente a linha contendo o metodo "iconbitmap"
#tmpfl = "icone.ico"
#iconfl = open(tmpfl,'wb')
#iconfl.write(imagem_icone)
#iconfl.close()
def botao_func(ativos):
  resultado.pack_forget()
  resultado["text"] = "Buscando..."
  main_func(ativos)
  resultado["text"] = "Pronto para a próxima execução"


def main_func(ativos):
  ativos = var.get()
  ativos = ativos.split()
  dados_planilha = []
  data_hora = datetime.now().strftime("%d/%m/%Y / %H:%M:%S")
  for ativo in ativos:
    dados_planilha.append([ativo.upper(), cotacao(ativo), data_hora])
  leitura_escrita_excell(dados_planilha)
  xlsx_para_pdf()
  campo_operacao = tk.Label(principal,
                            text="Pronto",
                            font="Arial 14",
                            padx=10,
                            pady=10)
  campo_operacao.pack()


principal = tk.Tk()
#principal.iconbitmap(tmpfl)
#remove(tmpfl)
principal.geometry('500x200')
principal.title("StonksWare")
var = StringVar(principal)
entrada = var.get()
texto = "Codigos do Google Finance \n (separados por espaco)"
nome_botao = "Buscar cotacoes"
nome_campo = tk.Label(principal, text=texto, font="Arial 14", padx=10, pady=10)
campo = tk.Entry(principal, textvariable=var, font="Arial 14")
botao = tk.Button(principal,
                  text=nome_botao,
                  command=partial(main_func, entrada),
                  padx=10,
                  pady=10,
                  font="Arial 12")
global resultado
resultado = tk.Label(text="Aguardando primeira execução",
                     font="Arial 14",
                     padx=10,
                     pady=10)
nome_campo.pack()
campo.pack()
botao.pack()
resultado.pack()
principal.mainloop()
