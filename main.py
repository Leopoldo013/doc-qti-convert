import zipfile
from string_xml import *
from function import *
import os
import shutil

#
#
#
#
#
#
#
# class _DeHTMLParser(HTMLParser):
#     def __init__(self):
#         HTMLParser.__init__(self)
#         self.__text = []
#
#     def handle_data(self, data):
#         text = data.strip()
#         if len(text) > 0:
#             text = sub('[ \t\r\n]+', ' ', text)
#             self.__text.append(text + ' ')
#
#     def handle_starttag(self, tag, attrs):
#         if tag == 'p':
#             self.__text.append('\n\n')
#         elif tag == 'br':
#             self.__text.append('\n')
#
#     def handle_startendtag(self, tag, attrs):
#         if tag == 'br':
#             self.__text.append('\n\n')
#
#     def text(self):
#         return ''.join(self.__text).strip()
#
#
# def dehtml(text):
#     try:
#         parser = _DeHTMLParser()
#         parser.feed(text)
#         parser.close()
#         return parser.text()
#     except:
#         print_exc(file=stderr)
#         return text
#
#
# def main():
#     text = "/home/leopoldo/PycharmProjects/xml-convert/sample.html"
#     print(dehtml(text))
#
#
# if __ == '__main__':
#     main()
#
# arquivo = 'sample.html'
#
# # import mammoth
#
#
# with open(arquivo, "rb") as docx_file:
#     result = mammoth.convert_to_html(docx_file)
# with open("sample.html", "w") as html_file:
#     linhas = html_file.write(result.value)
#     # soup = BeautifulSoup(linhas)
#     # print(soup.decode())
#     soup = BeautifulSoup(linhas)
#     print(soup.prettify())
#
# with open(arquivo, 'rb') as docx_file:
#     result = mammoth.extract_raw_text(docx_file)
#     print(result)
#     text = result.value
#     print(text)
#     with open('ouput.txt', 'w') as text_file:
#         text_file.write(text)


print('********************************************************')
print('*                                                      *')
print('*           Coversor de txt para QTI-2.1               *')
print('*   siga as instruções ou sair para sair do programa   *')
print('*                                                      *')
print('********************************************************')

decisao = input('Digite enter para continuar ou sair para sair: ')
while decisao != 'sair':
    arquivo = input('Digite o caminho do arquivo: ')
    with open(arquivo, 'r') as avaliativa:
        # content = list(avaliativa.read())
        # print(content)
        lines = [line for line in avaliativa.readlines() if line.strip()]
        #
        # lines = avaliativa.readlines()
        # print(lines)
        avaliativa.close()

    dificil = pergunta_por_linha(separa_questao(lines, 'Difícil'))
    facil = pergunta_por_linha(separa_questao(lines, 'Fácil'))
    intermediario = pergunta_por_linha(separa_questao(lines, 'Intermediario'))

    # print(len(dificil))
    # print(dificil)
    # print(len(intermediario))
    # print(medio)
    # print(len(facil))
    # print(facil)

    nivel = input('Digite o nivel de dificuldade: ').capitalize()
    if nivel == 'Facil':
        questions = perguntas(facil)
    if nivel == 'Intermediario':
        questions = perguntas(intermediario)
    if nivel == 'Dificil':
        questions = perguntas(dificil)
    quantidade = len(questions)
    qtd = 1
    identificador = 287771
    os.mkdir('qti21')
    caminho = 'qti21/'
    for question in questions:
        quest_tratada1 = " ".join(question[0])
        quest_tratada2 = " ".join(question[1])
        quest_tratada3 = " ".join(question[2])
        quest_tratada4 = " ".join(question[3])
        quest_tratada5 = " ".join(question[4])
        quest_tratada6 = " ".join(question[5])
        quest_tratada7 = " ".join(question[7])
        quest_tratada8 = " ".join(question[9])
        print(quest_tratada1)
        resposta = ''
        if quest_tratada2[0] == '*':
            resposta = 'answer_1'
            quest_tratada2 = quest_tratada2[1:]
        if quest_tratada3[0] == '*':
            resposta = 'answer_2'
            quest_tratada3 = quest_tratada3[1:]
        if quest_tratada4[0] == '*':
            resposta = 'answer_3'
            quest_tratada4 = quest_tratada4[1:]
        if quest_tratada5[0] == '*':
            resposta = 'answer_4'
            quest_tratada5 = quest_tratada5[1:]
        if quest_tratada6[0] == '*':
            resposta = 'answer_5'
            quest_tratada6 = quest_tratada6[1:]

        identificador = str(identificador)
        teste1 = manipula_xml_1(identificador, resposta, quest_tratada1, quest_tratada2,
                                quest_tratada3, quest_tratada4, quest_tratada5, quest_tratada6, quest_tratada7,
                                quest_tratada8)
        identificador = int(identificador) + 3
        # print(teste1)

        qtd = str(qtd)
        nome_arquivo = 'assessmentItem0000' + qtd + '.xml'
        with open(caminho + nome_arquivo, 'a') as manifest:
            manifest.write(teste1)
            manifest.close()
        qtd = int(qtd)
        qtd = qtd + 1

    nome = ''.join(lines[0])
    retorno1 = bancoManifest(quantidade, nome + '- ' + nivel)
    with open(caminho + 'question_bank00001.xml', 'a') as manifest:
        manifest.write(retorno1)
        manifest.close()

    retorno = imsManifest(quantidade)
    with open('imsmanifest.xml', 'a') as manifest:
        manifest.write(retorno)
        manifest.close()

    shutil.make_archive(nivel, 'zip', './', 'qti21')

    z = zipfile.ZipFile(nivel + '.zip', 'a', zipfile.ZIP_DEFLATED)
    z.write('imsmanifest.xml')
    z.close()
    path_dir = 'qti21'
    shutil.rmtree(path_dir)
    os.remove('imsmanifest.xml')

    decisao = input("Se desejar criar outro banco digite qq coisa caso queira sair digite sair: ")
