#!/usr/bin/python3

import math
import datetime
import random
import string
import zipfile

def ex5():
    """
    Criar um programa que solicita duas letras ao utilizador e indica a letra cuja ordem alfabética está no meio das duas.
    Apresente a letra imediatamente anterior se o número de letras entre as duas não for ímpar.
    
    Requisitos:
        * O programa deve pedir a primeira letra ao utilizador e guardar em uma variável
        * O programa deve pedir a segunda letra ao utilizador e guardar em uma variável
        * O programa então calcular a letra que fica entre as duas (mesma distância de ambas as letras)
        * O programa deve imprimir o resultado na consola.
    """
    
    #Pedir as letras ao utilizador
    first_letter = input("Introduza a primeira letra:\n")
    second_letter = input("Introduza a segunda letra:\n")
    
    alphabet = []
    for i in string.ascii_uppercase:
        #Armazena cada uma das letras como uma posição da lista
        alphabet.append(i)

    #Define índices das letras
    first_letter_index = alphabet.index(first_letter)
    second_letter_index = alphabet.index(second_letter)
    print(first_letter_index,second_letter_index)
    
    #Verifica se as letras existem na lista
    if(first_letter in alphabet and second_letter in alphabet):
        print("Letters exist")
    
    #Atribui o índice de cada letra introduzida a uma variável
    index_to_return_1 = first_letter_index + 1
    index_to_return_2 = second_letter_index - 1
    
    #Verifica se as letras estão espaçadas em duas letras
    if(index_to_return_1 == index_to_return_2):
        letter = index_to_return_1
        print(alphabet[letter])
    else:
        exit(-1)

if __name__ == "__main__": 
    ex5()        