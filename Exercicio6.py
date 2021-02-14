#!/usr/bin/python3

import math


def ex6():
    """
    Se apresentarmos todos os numeros naturais abaixo de 10 que são multiplos de 3 ou 5, obtemos os numeros 3,5,6 e 9. A soma deles é 23. 
    Criar um programa que apresente a soma de todos os multiplos de 3 e 5 abaixo de 1000
    
    Requisitos:
        * O programa deve correr, efetuar os calculos e imprimir o resultado na consola.
    """
    
    multiplos = []
    for i in range(0,1000):
        #Se um número entre 0 e 100 for múltiplo de 3 ou 5
        if(i % 3 == 0 or i % 5 == 0):
            multiplos.append(i)
    
    #Soma dos multiplos
    soma_total = sum(multiplos)
    print(soma_total)
    
if __name__ == "__main__":   
    ex6()