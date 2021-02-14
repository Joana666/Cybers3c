#!/usr/bin/python3
def find_even_number():
    #Pedir ao utilizador quatro números
    first_number = int(input("Introduza um número por favor: "))
    second_number = int(input("Introduza um número por favor: "))
    third_number = int(input("Introduza um número por favor: "))
    forth_number = int(input("Introduza um número por favor: "))
    
    #Colocar números numa lista e iterar a lista
    even_list = [first_number,second_number,third_number,forth_number]
    
    #Percorrer a lista
    for i in even_list:
        if(i%2 == 0):
            print("Números pares: ", i)
        if(i%2 != 0):
            print("Números ímpares: ", i)
    
    #Verificar números que são diferentes
    for j in range(len(even_list)):
        if(even_list[j] > even_list[j-1] or even_list[j] < even_list[j+1]):
            print("Números diferentes", even_list[j])

if __name__ == "__main__":
     find_even_number()            