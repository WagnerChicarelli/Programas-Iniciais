import time
import os
import math

def problema1036():
    limpar_tela()
    bem_vindo()
    tempo_pausa()
    limpar_tela()
    resposta =  ProcessarTarefa()
    tempo_pausa()
    limpar_tela()
    RetornoLogico(resposta)
    tempo_pausa()
    limpar_tela()

def RetornoLogico(resposta):
    resposta = str(resposta)
    print(resposta)

def ProcessarTarefa():
    numberA = float(input("Digite o valor de A:\n"))
    numberB = float(input("Digite o valor de B:\n"))
    numberC = float(input("Digite o valor de C:\n"))
    resposta = ProcessarTransacao(numberA, numberB, numberC)
    return resposta

def ProcessarTransacao(numberA, numberB, numberC):
    numberA = float(numberA)
    numberB = float(numberB)
    numberC = float(numberC)
    valorDelta = (numberB * numberB) - ((4 * numberA) * numberC)
    resposta = Bhaskara(numberA, numberB, numberC, valorDelta)
    return resposta

def Bhaskara(numberA, numberB, numberC, valorDelta):
    valorDelta = float(valorDelta)
    numberA = float(numberA)
    numberB = float(numberB)
    numberC = float(numberC)
    
    if ( valorDelta < 0 or numberA == 0):
        resposta = "Impossivel calcular"
        
    else:
        raiz = math.sqrt(valorDelta)
        calculo1 = (-numberB + raiz)/(2*numberA)
        calculo2 = (-numberB - raiz)/(2*numberA)
        resposta = "R1 = {:.5f}".format(calculo1) + "\n" + "R2 = {:.5f}".format(calculo2)
    return resposta

def tempo_pausa():
    time.sleep(5)

def bem_vindo():
    print("*******************************************************")
    print("*** Este programa ira calcular a formula de Baskara ***")
    print("*******************************************************")

def limpar_tela():
    os.system('cls') or None

if(__name__ == "__main__"):
    problema1036()