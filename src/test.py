#This will be getting the 2nd column of a text space delimited file
adresfile=open("adresfile.txt","r")
linelist=(adresfile.readlines())

for i in range(0, len(linelist)):
    liststring=linelist[i].split(',')
    print (liststring[1])
    
adresfile.close()

    
