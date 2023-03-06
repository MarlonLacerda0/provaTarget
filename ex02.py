#####################################
# Autor: Marlon Lacerda de Oliveira
# Data Criação: 05/03/2023
# EX 02: Prova TARGET
#####################################
def main():

    # Entrada de dados
    num = int(input("Insira um numero para saber a sequencia de fibonacci e se pertence a sequencia: "))
    u = 1
    p = 1
    cont = 0
    lista = [0, 1, 1]

    #Processamento
    for i in range(0, num):
        cont = u + p
        u = cont
        p = (cont - p)
        lista.append(cont)
    #Saida de Dados
    print(lista)

    if num in lista:
        print("Pertence a sequencia de fibonacci")
    else:
        print("Não Pertence a sequencia de fibonacci")

if __name__ == "__main__":
    main()