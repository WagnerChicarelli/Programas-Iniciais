import os
def questao():
    explicacao()
    remover_palavras = palavras_a_serem_removidas()
    leitura_do_aquivo()
    remocao_das_palavras(remover_palavras)

def remocao_das_palavras(remover_palavras):
    palavras = str(remover_palavras)
    musica = open("Questões Faculdade Federal/musica.txt","r", encoding="utf-8")
    for linha in musica:
        linha = linha.strip()
        linha = linha.replace(palavras,"")
        print(linha)

def leitura_do_aquivo():
    musica = open("Questões Faculdade Federal/musica.txt","r", encoding="utf-8")
    for linha in musica:
        linha = linha.strip()
        print(linha)
    print("*************************************************************************************************************")

def palavras_a_serem_removidas():
    remover_palavras = input("Escreva as palavras que serão removidas:\n")
    print(os.path.splitext(os.path.basename("musica.txt"))[0])
    print("*************************************************************************************************************")
    return remover_palavras
    
def explicacao():
    print("*************************************************************************************************************")
    print("*************************************************Bem-Vindo!**************************************************")
    print("**Este programa ira remover algumas palavras de um arquivo txt de acordo com a definição de outro arquivo..**")
    print("*************************************************************************************************************")
    print("*************************************************************************************************************")
    
if(__name__ == "__main__"):
    questao()