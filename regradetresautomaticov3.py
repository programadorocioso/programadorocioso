def regra_de_tres_proporcional(linhas):
    linhaum,linhadois = linhas[0],linhas[1]
    a,b,c,d = linhaum[0],linhaum[1],linhadois[0],linhadois[1]
    try:
        if str(b) == 'x' or 'X':
            conta = (float(a) * float(d)) / float(c)
            return conta
    except:
        try:
            if str(d) == 'x' or 'X':
                conta = (float(c) * float(b)) / float(a)
                return conta
        except:
            try:
                if str(a) == 'x' or 'X':
                    conta = (float(c) * float(b)) / float(d)
                    return conta
            except:
                try:
                    if str(c) == 'x' or 'X':
                        conta = (float(a) * float(d)) / float(b)
                        return conta
                except:
                    return 'Não foi possível efetuar o cálculo. Por favor, verifique os números.'
def regra_de_tres_inversa(linhas):
    linhaum,linhadois = linhas[0],linhas[1]
    a,b,c,d = linhaum[0],linhaum[1],linhadois[0],linhadois[1]
    try:
        if str(b) == 'x' or 'X':
            conta = (float(c) * float(d)) / float(a)
            return conta
    except:
        try:
            if str(d) == 'x' or 'X':
                conta = (float(a) * float(b)) / float(c)
                return conta
        except:
            try:
                if str(a) == 'x' or 'X':
                    conta = (float(c) * float(d)) / float(b)
                    return conta
            except:
                try:
                    if str(c) == 'x' or 'X':
                        conta = (float(a) * float(b)) / float(d)
                        return conta
                except:
                    return 'Não foi possível efetuar o cálculo. Por favor, verifique os números.'
def entrada_aux():
    linha = input()
    valores = linha.split()
    a,b = valores[0],valores[1]
    return a,b
def entrada():
    valores = []
    for i in range(2):
        valores.append(entrada_aux())
    return tuple(valores)
def filtro_inteiro(numero):
    try:
        if numero == int(numero):
            return int(numero)
        else:
            return numero
    except:
        return numero
print('Bem vindo(a), esse programa faz o cálculo de regra de três simples.\nÉ possível selecionar entre regra de três diretamente proporcional ou inversamente proporcional.')
print('O formato deve ser o seguinte:\n A   B\n C   D\nOnde:\n A,B,C ou D deve ser o "X" e os outros valores devem ser números')
print('Após inserir A e B separadados por um espaço, tecle "ENTER" e insira C e D da mesma forma e pressione "ENTER"')
print('Exemplo:\n10 100\n5 X')
while True:
    print('Para regra de três diretamente porporcional, tecle 1 e dê "ENTER"')
    print('Para regra de três inversamente proporcional, tecle 2 e dê "ENTER"')
    print('Para fechar o programa, tecle 3 e dê "ENTER"\n')
    escolha = input()
    try:
        if int(escolha) == 1:
            print('\nO valor de X é:\n',filtro_inteiro(regra_de_tres_proporcional(entrada())),'\n')
            continue
        elif int(escolha) == 2:
            print('\nO valor de X é:\n',filtro_inteiro(regra_de_tres_inversa(entrada())),'\n')
            continue
        elif int(escolha) == 3:
            break
        else:
            print('Insira um valor entre 1 e 3!')
            continue
    except:
        print('Erro inesperado')
        continue