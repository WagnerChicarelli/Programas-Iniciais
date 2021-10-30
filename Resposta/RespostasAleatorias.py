import random
import os

def resposta_aleatoria():
    pergunta = input("Faça sua pergunta\n")           
    os.system('cls') or None 
    respota_aleatoria = carrega_resposta()   
    print(pergunta)
    print(respota_aleatoria)

    
def carrega_resposta():
    arquivo = open("Resposta/respostas.txt", "r", encoding="utf-8")
    resposta = []
    for linha in arquivo:
        linha = linha.strip()
        resposta.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(resposta))

    respota_aleatoria = resposta[numero].lower()

    return respota_aleatoria

if(__name__ == "__main__"):
    resposta_aleatoria()