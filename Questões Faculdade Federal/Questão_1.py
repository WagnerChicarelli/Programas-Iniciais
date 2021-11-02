import time
import os

def questao():
    limpar_tela()
    explicacao()
    time.sleep(5)
    remover_palavras = palavras_a_serem_removidas()
    time.sleep(5)
    arquivo = nome_arquivo()
    arquivo_lido_str = leitura_do_aquivo(arquivo)
    time.sleep(5)
    remocao_das_palavras(remover_palavras,arquivo_lido_str)
    time.sleep(10)
    limpar_tela()

def limpar_tela():
    os.system('cls') or None

def remocao_das_palavras(remover_palavras,arquivo_lido):
    arquivo = [str(arquivo_lido)]
    palavras = str(remover_palavras)
    palavras_a_remover = palavras.split()
    for palavra in arquivo:
        resultado = palavra;
        for remover in palavras_a_remover:
            resultado = remover_palavra(resultado, remover)
        print(resultado)

def remover_palavra(palavra, remover):
    remover_tamanho = len(remover)
    palavra_tamanho = len(palavra)
    while True:
        remover_posicao = palavra.find(remover)
        if remover_posicao != -1:
            palavra_inicio = palavra[0:remover_posicao]
            palavra_fim = palavra[remover_posicao+remover_tamanho:palavra_tamanho]
            palavra = palavra_inicio + palavra_fim
        else:
            break
    return palavra

def leitura_do_aquivo(arquivo):
    nome_arquivo = "Questões Faculdade Federal/" + str(arquivo) + ".txt"
    musica = open(nome_arquivo,"r", encoding="utf-8")
    arquivo_lido = musica.readlines()
    arquivo_lido_str = "".join(arquivo_lido)
    print(arquivo_lido_str)
    musica.close()
    print("*******************************************************************************************************************")
    return arquivo_lido_str

def palavras_a_serem_removidas():
    remover_palavras = input("Escreva as palavras que serão removidas:\n")
    print("*******************************************************************************************************************")
    return remover_palavras

def nome_arquivo():
    arquivo = input("Digite o arquivo que você deseja remover as palavras:\n")
    print("*******************************************************************************************************************")
    return arquivo
    
def explicacao():
    print("*******************************************************************************************************************")
    print("*************************************************Bem-Vindo!********************************************************")
    print("**Este programa ira remover algumas palavras de um arquivo txt de acordo com a definição com o que foi inserido..**")
    print("*******************************************************************************************************************")
    print("*******************************************************************************************************************")
    
if(__name__ == "__main__"):
    questao()