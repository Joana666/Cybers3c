from pathlib import Path
p = Path('.')
import os, sys

#Criar diretorios
def makeDir():
    print("Criar diretorio")
    nome1 = input ("Introduza o nome para o diretorio: ")
    if os.path.exists(nome1):
        print("ERRO: Este nome já existe. Atribua outro.")
    else:
        print("Diretorio criado com sucesso!\n")
        os.mkdir(nome1)
        main()

#Renomear diretorios
def renameDir():
    print("Renomear o diretorio")
    new_n = input ("Introduza o nome do diretorio que pretende renomear: ")
    if os.path.exists(path):
        novonome = input ("Introduza o novo nome:") 
        os.rename(new_n, novonome)
        print("O nome foi alterado com sucesso!")
        main()
    else:
        print("O nome indicado não existe.")
    
# Remover diretorios
def remDir():
    print ("Eliminar diretorio")
    nome = input ("Introduza o nome do diretorio que pretende eliminar: ")
    if os.path.exists(nome):
        os.rmdir(nome)
        print("Diretorio eliminado com sucesso!")
        main()   
    else:
        print("O nome indicado não existe.")  
        main ()
 
#Listar diretorios
def listDir():
    print (os.listdir())
    main()

def main():
    print("\nOPÇÕES: \n[C] Criar um diretorio \n[R] Remover um diretorio \n[L] Listar aos diretorios existentes \n[N] Renomear um diretorio\n[S] Sair\n")
    resposta = input("\nIntroduza a letra maiúscula da opção que pretende: ")
    if resposta == "C":
        makeDir()

    if resposta == "R":
        remDir()

    if resposta == "L":
        listDir()

    if resposta == "N":
        renameDir()

    if resposta == "S":
        sys.exit()
    else:
        print("Escolha uma opção válida")
        main()
main()
