"""
Programa: classificador_de_numero
Descrição: Este programa classifica um número digitado, se ele for menor que 10, entre 10 e 20 ou se não é válido.
Autor: F
Data : 23/06/2023
Versão: 0.0.1
"""

#Atribuição de variáveis





#Entrada de dados

x = float(input("Qual o número? "))


#Processamento de dados

if x < 10:
    x = (x * 2)
    print(x)
    
elif 10 <= x <= 20:
    x = (x / 2)
    print(x)
    
else:
    print("O número não é valido")



#Saida de dadaos

