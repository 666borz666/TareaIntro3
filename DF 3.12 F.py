#Elaborado por: Daniel Campos
#Creación: 24-08-2023 5:17pm
#última modificación: 24-08-2023 
#Versión 3.10.6

#def de funciones
def promPos(psumPos,pcuepos,pn):
    """Funciónn: Saca el promedio de los números positivos digitados por el usuario
    Entradas:
        psumPos: Suma de todos lo números positivos digitados
        pcuepos: Contador de los números positivos
    """
    return promPos(str(psumPos/pcuepos))

def promGen(psumPos,psumOtr,pn):
    """Función: Saca el promedio de todos los números digitados por el usuario
    Entradas:
        psumPos: Suma de todos los números positivos digitados
        psumOtr: Suma de los números que no son positivos
        pn: Cantidad de números a operar digitados por el usuario
    """
    return(str((psumPos+psumOtr)/pn))

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
        print("\n", "Números positivos: ", cuepos, "\n", "Promedio de números positivos: ", promPos, "\n", "Promedio general de todos los números: ", promGen)
else:
    print("La cantidad no puede ser 0")