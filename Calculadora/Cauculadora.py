def cauculadora():
    bem_vindo()
    tipo_de_conta = input("Qual tipo de calculo você quer fazer?(Multiplicacao/Divisao/Soma/Adicao)\n").upper()
    iniciar_contas(tipo_de_conta)

def bem_vindo():
    print("**************************")
    print("***Calculadora Simples!***")
    print("**************************")

def iniciar_contas(tipo_de_conta):
    if(tipo_de_conta == "MULTIPLICACAO"):
        primeiro_numero = int(input("Primeiro numero:\n"))
        segundo_numero = int(input("Segundo numero:\n"))
        resposta = primeiro_numero * segundo_numero
        print(resposta)
        
    if(tipo_de_conta == "DIVISAO"):
        primeiro_numero = int(input("Primeiro numero:\n"))
        segundo_numero = int(input("Segundo numero:\n"))
        resposta = primeiro_numero / segundo_numero
        print(resposta)
        
    if(tipo_de_conta == "SOMA"):
        primeiro_numero = int(input("Primeiro numero:\n"))
        segundo_numero = int(input("Segundo numero:\n"))
        resposta = primeiro_numero + segundo_numero
        print(resposta)
        
    if(tipo_de_conta == "ADICAO"):
        primeiro_numero = int(input("Primeiro numero:\n"))
        segundo_numero = int(input("Segundo numero:\n"))
        resposta = primeiro_numero - segundo_numero
        print(resposta)
    else:
        print("Opcao invalida")



if(__name__ == "__main__"):
    cauculadora()