#Creado por: Daniel Campos
#Fecha de cración: 24-08-2023 6:40pm
#última modificación: 24-08-2023 6:57pm
#Versión 3.10.6

serie=0
n=int(input("Digite el número de términos de la serie: "))
i=1
if n>0:
    while i<n:
        serie+=i**i
        i+=1
    else:
        print(serie)
else: 
    print("Digite una cantidad mayor que 0")