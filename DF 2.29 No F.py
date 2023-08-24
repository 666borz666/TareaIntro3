#Elaborado por: Daniel Campos
#Creación: 23-08-2023 9:30am
#última modificación: 23-08-2023 9:56am
#Versión 3.10.6

#programa principal
tipoE=int(input("Tipo de enfermedad (1-4): "))
edad=int(input("Digite su edad: "))
diasI=int(input("Días de internación: "))

if 1<=tipoE<=4:
    if tipoE == 1:
        costoT=diasI*25
    elif tipoE == 2:
        costoT=diasI*16
    elif tipoE == 3:
        costoT=diasI*20
    else:
        costoT=diasI*32
    if 14<=edad<=24:
        costoT*=1.10
        print("Costo total: ", costoT)
    else:
        print("Costo total: ", costoT)
else:
    print("Digite un tipo de enfermedad válido.")