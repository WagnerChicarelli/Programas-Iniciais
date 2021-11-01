def questao():
    explicacao()
    funcao_programa()
    remover_palavras()

def remover_palavras():
    arquivo1 = open("Questões Faculdade Federal/palavras_a_serem_removidas.txt", "r",encoding="utf-8")
    arquivo2 = open("Questões Faculdade Federal/musica.txt", "r",encoding="utf-8")
    with open('Questões Faculdade Federal/palavras_a_serem_removidas.txt', 'r',encoding="utf-8") as f:
        results = [[str(entry) for entry in line.split()] for line in f.readlines()]
   
    for linha in arquivo2:
        linha = linha.split()
        result = [palavra for palavra in linha if palavra.lower() not in results]
        retorno = ' '.join(result)
        print(retorno)
    print("-------------------------------------------------------------------------------------------------------------")
    #print(results)
    arquivo1.close()
    arquivo2.close()
    

def funcao_programa():
    arquivo2 = open("Questões Faculdade Federal/musica.txt", "r+",encoding="utf-8")
    for linha in arquivo2:
        linha =linha.strip()
        print(linha)
    print("-------------------------------------------------------------------------------------------------------------")
    arquivo2.close()
    
    

    
def explicacao():
    print("*************************************************************************************************************")
    print("*************************************************Bem-Vindo!**************************************************")
    print("**Este programa ira remover algumas palavras de um arquivo txt de acordo com a definição de outro arquivo..**")
    print("*************************************************************************************************************")
    print("*************************************************************************************************************")
    
if(__name__ == "__main__"):
    questao()