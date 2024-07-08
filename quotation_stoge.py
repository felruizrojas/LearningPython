from math import ceil
from os import system
system("clear")

while True:
    
    while True:
        correo=input("Ingrese su correo electrónico: ")
        if "@" in correo:
            print("Correo ingresado correctamente")
            break
        else:
            print("Debe ingresar un correo válido")
            
    while True:
        telefono=input("Ingrese teléfono de contacto: ")
        if telefono.isnumeric():
            if len(telefono)>=8 and len(telefono)<=9:
                print("Teléfono válido")
                break
            elif telefono!=telefono.isnumeric():
                print("Debe ingresar un teléfono de 8 a 9 dígitos")
        else:
            print("Debe ingresar un teléfono de 8 a 9 dígitos")
            
    while True:
        cantidad=input("Ingrese cantidad de cajas: ")
        if cantidad.isnumeric():
            cantidad=int(cantidad)
            if cantidad>0 and cantidad!="":
                print("Cantidad ingresada correctamente")
                break
        else:
            print("Debe escribir número de cajas a ingresar")
            
    while True:
        largo=input("Ingrese largo (en cm) de sus cajas: ")
        if largo.isnumeric():
            largo=int(largo)
            if largo>0 and largo!="":
                print("Medida ingresada correctamente")
                break
        else:
            print("Debe ingresar su medida en cm")
            
    while True:
        alto=input("Ingrese alto (en cm) de sus cajas: ")
        if alto.isnumeric():
            alto=int(alto)
            if alto>0 and alto!="":
                print("Medida ingresada correctamente")
                break
        else:
            print("Debe ingresar su medida en cm")
            
    while True:
        ancho=input("Ingrese ancho (en cm) de sus cajas: ")
        if ancho.isnumeric():
            ancho=int(ancho)
            if ancho>0 and ancho!="":
                print("Medida ingresada correctamente")
                break
        else:
            print("Debe ingresar su medida en cm")
            
    m_largo=largo/100 #0.5
    m_alto=alto/100 #0.1
    m_ancho=ancho/100 #0.1
    m3_caja=m_largo*m_alto*m_ancho #0.005
    
    bodega=(cantidad*m3_caja)/20 #4000*0.005=20/20=1
    
    print(f'''
    Correo: {correo}
    Teléfono: {telefono}
    Cantidad de cajas a almacenar: {cantidad} de {largo} x {alto} x {ancho} cm - Cajas por bodega 4000
    Bodega: {ceil(bodega)}
    Valor total: ${150000*(ceil(bodega))}''')
    
    while True:
        seguir=input("Desea continuar: 1:Si 2:No: ")
        if seguir.isnumeric():
            seguir=int(seguir)
            if seguir==1:
                break
            elif seguir==2:
                exit()
            else:
                print("Debe ingresar 1 para si y 2 para no")
        else:
            print("Debe ingresar 1 para si y 2 para no")
