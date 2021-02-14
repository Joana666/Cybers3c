#!/usr/bin/python3

import math


def ex3():
    """
    2520 é o número mais pequeno que pode ser dividido por todos os números de 1 até 10 sem resto de divisão. Qual é o
    número positivo mais pequeno que é uniformamente divisivel por todos os números de 1 até 20?
    
    Requisitos Exercício 3:
        * O programa deve correr, efetuar os cálculos e imprimir o resultado na consola.
    """
    
    #Iterate through all numbers in the range from 1 to 20
    div_list = []
    for i in range(1,20):
        #Preenche a lista com números de 1 a 20
        div_list.append(i)
    
    ans = 1
    for i in range(1, 20):
        #Calcula o máximo divisor comum
        ans = int((ans * i)/math.gcd(ans, i))          
    
    print(ans) 

if __name__ == "__main__":    
    ex3()