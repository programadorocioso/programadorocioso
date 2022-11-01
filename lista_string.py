def arquivo_texto(local):
    texto = open(local,"r").readlines()
    return texto
def lista_string(lista):
    palavras = []
    for linha in lista:
        if linha.__contains__(" "):
            temp = linha.replace("\n","").split()
            for i in temp:
                palavras.append(i)
        else:
            palavras.append(linha)
    return palavras
print(lista_string(arquivo_texto("ativos.txt")))