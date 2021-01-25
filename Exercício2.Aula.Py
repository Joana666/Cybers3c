#Output para abrir um ficheiro:
file = open ("Exercicio2.txt", "w")
#FOR
print("\n ciclo for\n")
x = ["windows", "macos", "linux", "solaris", "ios"]
for item in x:
    if item != "solaris":
      print(item)
      file.write(str(item) + "\n") 

#WHILE
      file.write ("\n ciclo while\n")  
print("\n ciclo while\n") 
    y = 0  
while y < len (x):
    if x[y] !="solaris":
        print(x[y])
        file.write(str(x[y])+ "\n")
    y+= 1
file.close()   
