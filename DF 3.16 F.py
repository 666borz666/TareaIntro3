#Creado por: Daniel Campos
#Fecha de cración: 24-08-2023 7:30pm
#última modificación: 24-08-2023 7:47pm
#Versión 3.10.6

#def funciones
def resSer(pserie,i):
    """Función: calcula la serie de n números la cual es sumando de manera: n**n
    Entradas:
        pserie: acumulador de los resultados
        i: control del ciclo 
    Salidas: 
        serie: todos los valores ya acumulados y sumados
    """
    while i<=n:
        serie=+i**i
        i+=1
    else:
        resSer=serie
    return resSer


#programa principal
serie=0
n=int(input("Digite el número de términos de la serie: "))
i=1
if n>0:
        print(str(resSer(serie,i)))
else: 
    print("Digite una cantidad mayor que 0")