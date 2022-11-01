import tkinter as tk
from tkinter import StringVar
from tkinter import filedialog as fd
from verificar_cotacao import cotacao
from modulo_arquivo_tk import leitura_escrita_excell, xlsx_para_pdf, arquivo_texto, lista_string,string_lista
from datetime import datetime
from functools import partial
#Remover comentarios das linhas abaixo se executando no Windows
#Por algum motivo muito especifico, essas linhas causam erros apenas no Linux
#Mais especificadamente a linha contendo o metodo "iconbitmap"
#import base64
#from icone import imagem
#from os import remove
#imagem_icone = base64.b64decode(imagem())
#tmpfl = "icone.ico"
#iconfl = open(tmpfl,'wb')
#iconfl.write(imagem_icone)
#iconfl.close()
def botao_txt_func(ativos_txt):
  nome = fd.askopenfilename(title="Abrir txt contendo ativos a buscar")
  texto = arquivo_texto(nome)
  texto_formatado = lista_string(texto)
  texto_final = str(string_lista(texto_formatado))
  campo.delete(0,tk.END)
  campo.insert(0,texto_final)
def botao_func(ativos):
  main_func(ativos)
global campo_operacao
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
principal.geometry('500x270')
principal.title("StonksWare")
var = StringVar(principal)
entrada = var.get()
texto = "Codigos do Google Finance \n (separados por espaco)"
nome_botao = "Buscar cotacoes"
nome_campo = tk.Label(principal, text=texto, font="Arial 14", padx=10, pady=10)
campo = tk.Entry(principal, textvariable=var, font="Arial 14")
botao_txt = tk.Button(principal,text="Escolher arquivo",padx=10,pady=10,command=partial(botao_txt_func,entrada))
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
botao_txt.pack()
botao.pack()
resultado.pack()
principal.mainloop()
