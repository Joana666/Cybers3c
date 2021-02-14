#!/usr/bin/python3
import math
import datetime


def convert_from_second_to_hours():
    
    segundos = int(input("Número de segundos:\n"))
    #Verifica se o input é vazio ou se não é um número
    if(segundos == "" or math.isnan(segundos) == True):
        print("Valor inválido!\n")
        #Volta para a execução da função
        convert_from_second_to_hours()
    
    #Converter segundos em horas, minutos e segundos
    h_m_s = datetime.timedelta(seconds=segundos)
    print("Horas, minutos e segundos: ", h_m_s)
    


if __name__ == "__main__":    
    convert_from_second_to_hours()
       