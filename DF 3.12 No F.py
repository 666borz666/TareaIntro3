#Elaborado por: Daniel Campos
#Creación: 23-08-2023 11:20am
#última modificación: 23-08-2023 11:47am 
#Versión 3.10.6

#programa principal
sumPos=sumOtr=cuepos=0
n=int(input("Indique la cantidad de números para operar: "))
i=1
if n>0:
    while i<=n:
        num=int(input("Digite un número: "))
        if num>0:
            sumPos+=num
            cuepos+=1
            i+=1
        else: 
            sumOtr+=num
            i+=1
    else:
        proGen=(sumPos+sumOtr)/n
        proPos=(sumPos/cuepos)
        print("\n", "Números positivos: ", cuepos, "\n", "Promedio de números positivos: ", proPos, "\n", "Promedio general de todos los números: ", proGen)
else:
    print("La cantidad no puede ser 0")
    #evita un error cuando n<=0