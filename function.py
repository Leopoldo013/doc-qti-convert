def separa_questao(lista, dificuldade):
    nivel = []

    for line in range(len(lista)):
        if lista[line] == f'Grau de dificuldade: [{dificuldade}]\n':

            for i in range(11):
                # print(line[i])
                nivel.append(lista[line + i])

    return nivel


def pergunta_por_linha(lista):
    perguntas_por_linha = []
    for per in lista:
        pergunta = per.split('\n')
        perguntas_por_linha.append(pergunta)

    final_quest = len(perguntas_por_linha)
    return perguntas_por_linha


def perguntas(lista):
    if len(lista) == 11:
        pergunta1 = lista[1:11]
        # print(pergunta1)
        perguntas = [pergunta1]
        return perguntas


    elif len(lista) == 22:

        pergunta1 = lista[1:11]
        pergunta2 = lista[12:22]

        perguntas = [pergunta1, pergunta2]
        return perguntas

    elif len(lista) == 33:
        pergunta1 = lista[1:11]
        pergunta2 = lista[12:22]
        pergunta3 = lista[23:33]

        perguntas = [pergunta1, pergunta2, pergunta3]
        return perguntas

    elif len(lista) == 44:
        pergunta1 = lista[1:11]
        pergunta2 = lista[12:22]
        pergunta3 = lista[23:33]
        pergunta4 = lista[34:44]

        perguntas = [pergunta1, pergunta2, pergunta3, pergunta4]
        return perguntas

    elif len(lista) == 55:
        pergunta1 = lista[1:11]
        pergunta2 = lista[12:22]
        pergunta3 = lista[23:33]
        pergunta4 = lista[34:44]
        pergunta5 = lista[45:55]

        perguntas = [pergunta1, pergunta2, pergunta3, pergunta4, pergunta5]
        return perguntas

    elif len(lista) == 66:
        pergunta1 = lista[1:11]
        pergunta2 = lista[12:22]
        pergunta3 = lista[23:33]
        pergunta4 = lista[34:44]
        pergunta5 = lista[45:55]
        pergunta6 = lista[56:66]

        perguntas = [pergunta1, pergunta2, pergunta3, pergunta4, pergunta5, pergunta6]
        return perguntas

    elif len(lista) == 77:
        pergunta1 = lista[1:11]
        pergunta2 = lista[12:22]
        pergunta3 = lista[23:33]
        pergunta4 = lista[34:44]
        pergunta5 = lista[45:55]
        pergunta6 = lista[56:66]
        pergunta7 = lista[67:77]

        perguntas = [pergunta1, pergunta2, pergunta3, pergunta4, pergunta5, pergunta6, pergunta7]
        return perguntas

    elif len(lista) == 88:
        pergunta1 = lista[1:11]
        pergunta2 = lista[12:22]
        pergunta3 = lista[23:33]
        pergunta4 = lista[34:44]
        pergunta5 = lista[45:55]
        pergunta6 = lista[56:66]
        pergunta7 = lista[67:77]
        pergunta8 = lista[78:88]

        perguntas = [pergunta1, pergunta2,
                     pergunta3, pergunta4, pergunta5, pergunta6, pergunta7, pergunta8]
        return perguntas

    elif len(lista) == 99:
        pergunta1 = lista[1:11]
        pergunta2 = lista[12:22]
        pergunta3 = lista[23:33]
        pergunta4 = lista[34:44]
        pergunta5 = lista[45:55]
        pergunta6 = lista[56:66]
        pergunta7 = lista[67:77]
        pergunta8 = lista[78:88]
        pergunta9 = lista[89:99]

        perguntas = [pergunta1, pergunta2, pergunta3, pergunta4, pergunta5, pergunta6,
                     pergunta7, pergunta8, pergunta9]
        return perguntas

    elif len(lista) == 110:
        pergunta1 = lista[1:11]
        pergunta2 = lista[12:22]
        pergunta3 = lista[23:33]
        pergunta4 = lista[34:44]
        pergunta5 = lista[45:55]
        pergunta6 = lista[56:66]
        pergunta7 = lista[67:77]
        pergunta8 = lista[78:88]
        pergunta9 = lista[89:99]
        pergunta10 = lista[100:110]

        perguntas = [pergunta1, pergunta2, pergunta3, pergunta4, pergunta5, pergunta6,
                     pergunta7, pergunta8, pergunta9, pergunta10]
        return perguntas
    else:
        print('NÃO POSSUE QUESTÕES PARA ESSE NIVEL DE DIFICULDADE')
