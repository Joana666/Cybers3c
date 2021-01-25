#!/usr/bin/python
	

	#Criar listas para ip e port
    iplist = []
    portlist = []


	
    # Criar ficheiros iplist.txt
    # Criar ficheiro portlist.txt
    # Escrever lista de ips no ficheiro iplist.txt
    # Escrever lista de ports no ficheiro portlist.txt
    iplistFile= open("ipList.txt", "w")
	portlistFile = open("portList.txt", "w")


	

	for ip in range(1, 256):
	    print(ip)
	    iplistFile.write(str(ip) + "\n")
	

	for port in range(1, 1025):
	    print(port)
	    portlistFile.write(str(port) + "\n")
	
    # Fechar ficheiro iplist.txt
    # Fechar ficheiro portlist.txt
	File1.close()
	File2.close()
