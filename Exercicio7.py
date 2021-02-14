#!/usr/bin/python3

import math

import random
import string


def password_generator():
    """
    Criar um programa que consiga gerar uma password aleatória, com os seguintes parâmetros:
        - Tamanho da password (entre 8 a 32 caracteres, deve pedir input ao utilizador)
        - Uppercase and Lowercase
        - Caracteres especiais
        - Digitos
    """
    
    letters = string.ascii_letters
    numbers = string.digits
    special_characters = string.punctuation
    
    #Pedir ao utilizador o tamanho da password
    length = int(input("Introduza o tamanho da password:\n"))
    #Verificar se a password é maior que 32 ou menor que 8 e se o input é vazio ou se não é um número
    if(length < 8 or length > 32 or length == "" or math.isnan(length) == True):
        print("Invalid lenght")
        password_generator()
    
    alphanumeric = f'{letters}{numbers}{special_characters}'
    
    #Converter alfanúmerico para lista
    alphanumeric = list(alphanumeric)
    #Baralhar a lista
    random.shuffle(alphanumeric)
    
    #Gerar a password
    password = random.choices(alphanumeric, k=length)#Escolhe caracteres aleatórios
    #Junta os caracteres escolhidos
    password = ''.join(password)
    print(password)
    
    
if __name__ == "__main__":
    password_generator()