def fibonacci():
    print("*******************************************************")
    print("***Este programa irá fazer a sequencia de Fibonacci!***")
    print("*******************************************************")

    print("Você gostaria que o programa inicie a sequencia de Fibonacci?")
    resposta = input("S/N:    ").upper()

    if(resposta == "S"):
        limite_de_numeros = int(input("Qual o limite de numeros?  "))
        contador = 1
        primeiro = 0
        segundo = 1
        for contador in range(1, limite_de_numeros+1):
            terceiro = primeiro + segundo
            print(primeiro)
            primeiro = segundo
            segundo = terceiro
            contador += 1  
    
    else:
        print("Ok então")

if(__name__ == "__main__"):
    fibonacci()