import time
import os
def problema1007():
    limpar_tela()
    bem_vindo()
    tempo_pausa()
    limpar_tela()
    resposta = envioLogico()
    tempo_pausa()
    limpar_tela()
    retornoLogico(resposta)
    tempo_pausa()
    limpar_tela()

def retornoLogico(resposta):
    resposta = str(resposta)
    print("DIFERENCA = " + resposta)

def envioLogico():
    numeroA = int(input("Digite o primeiro numero do primeiro grupo: \n"))
    numeroB = int(input("Digite o segundo numero do primeiro grupo: \n"))
    numeroC = int(input("Digite o primeiro numero do segundo grupo: \n"))
    numeroD = int(input("Digite o segundo numero do segundo grupo: \n"))
    resposta = ProcessarTransacao(numeroA, numeroB, numeroC, numeroD)
    return resposta

def ProcessarTransacao(numeroA, numeroB, numeroC, numeroD):
    numeroA = int(numeroA)
    numeroB = int(numeroB)
    numeroC = int(numeroC)
    numeroD = int(numeroD)
    resposta = (numeroA * numeroB) - (numeroC * numeroD)
    return resposta

def tempo_pausa():
    time.sleep(5)

def bem_vindo():
    print("***************************************************************************")
    print("*** Este programa ira calcular a diferença entre dois grupos de numeros ***")
    print("***************************************************************************")

def limpar_tela():
    os.system('cls') or None

if(__name__ == "__main__"):
    problema1007()