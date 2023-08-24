#Elaborado por: Daniel Campos
#Creación: 23-08-2023 10:00am
#última modificación: 23-08-2023 10:45am
#Versión 3.10.6

#definición de funciones
def costoT(pdiasI,ptipoE):
    """
    Funcionamiento: Calcula el costo total de los días de internación dependiendo de la enfermedad
    Entradas:
        pdias: dias internado
        ptipoE: tipo de enfermedad
    Salidas:
        costotT: costo total de internación
    """
    if tipoE==1:
        costoT=diasI*25
        return costoT
    elif tipoE==2:
        costoT=diasI*16
        return costoT
    elif tipoE==3:
        costoT=diasI*20
        return costoT
    else:
        costoT=diasI*32
        return costoT
    
#programa principal
tipoE=int(input("Tipo de enfermedad (1-4): "))
if 1<=tipoE<=4:
    edad=int(input("Digite su edad: "))
    diasI=int(input("Días de internación: "))
    if 14<=edad<=22:
        print("Costo total: "+str(costoT(diasI,tipoE)*1.10))
    else:
        print("Costo total: "+str(costoT(diasI,tipoE)))
else:
    print("Digite un tipo de enfermedad válido.")