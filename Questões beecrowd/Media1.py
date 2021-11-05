import time
import os
def problema1005():
    limpar_tela()
    bem_vindo()
    tempo_pausa()
    limpar_tela()
    resposta = ProcessarTarefa()
    tempo_pausa()
    limpar_tela()
    RetornoLogico(resposta)
    tempo_pausa()
    limpar_tela()

def tempo_pausa():
    time.sleep(5)

def RetornoLogico(resposta):
    resposta  = float(resposta) 
    print("MEDIA = {:.5f}".format(resposta))

def ProcessarTarefa():
    primeiro_numero = float(input("Digite o primeiro numero:\n"))
    segundo_numero = float(input("Digite o segundo numero:\n"))
    resposta = Contrato(primeiro_numero, segundo_numero)
    return resposta

def Contrato(primeiro_numero, segundo_numero):
    primeiro_numero = float(primeiro_numero)
    segundo_numero = float(segundo_numero)
    primeiro_numero = primeiro_numero  * 3.5
    segundo_numero = segundo_numero * 7.5
    resposta = (primeiro_numero + segundo_numero) / (3.5+7.5)
    return resposta


def bem_vindo():
    print("******************************************************************")
    print("*** Este programa ira fazer uma conta para tirar media simples ***")
    print("******************************************************************")

def limpar_tela():
    os.system('cls') or None

if(__name__ == "__main__"):
    problema1005()