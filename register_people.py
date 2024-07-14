from os import system
system("clear")
from sys import exit

import re
validacion_correo = r'[^@]+@[^@]+\.[^@]+'

ec_dic = {
    "c": "casado",
    "s": "soltero",
    "v": "viudo"
}

registros=[]

def guardar():
    system("clear")
    while True:
        rut=input("Ingrese su rut: ")
        while True:
            if len(rut)==9:
                print("Rut ingresado correctamente")
                break
            else:
                print("Rut ingresado incorrectamente")
                rut=input("Ingrese su rut: ")
        nombre=input("Ingrese nombre: ").capitalize()
        while True:
            if nombre.isalpha() and len(nombre)>0:
                print("Nombre ingresado correctamente")
                break
            else:
                print("Nombre ingresado incorrectamente")
                nombre=input("Ingrese nombre: ").capitalize()
        apellido=input("Ingrese apellido: ").capitalize()
        while True:
            if apellido.isalpha() and len(apellido)>0:
                print("Apellido ingresado correctamente")
                break
            else:
                print("Apellido ingresado incorrectamente")
                apellido=input("Ingrese apellido: ").capitalize()
        while True:
            try:
                edad = int(input("Ingrese edad: "))
                if edad >= 18:
                    print("Edad ingresada correctamente")
                    break
                else:
                    print("Debe ser mayor o igual a 18 años")
            except ValueError:
                print("Edad ingresada incorrectamente, debe ser un número entero")
        estado_civil=input("Ingrese estado civil. C=Casado | S=Soltero | V=Viudo: ").lower()
        while True:
            if estado_civil in ["c", "s", "v"]:
                print("Estado civil ingresado correctamente")
                break
            else:
                print("Estado civil ingresado incorrectamente")
                estado_civil=input("Ingrese estado civil. C=Casado | S=Soltero | V=Viudo: ").lower()
        fecha=input("Ingrese fecha de afiliación: dd-mm-aaaa: ")
        while True:
            if len(fecha)==10 and fecha[2]=="-" and fecha[5]=="-":
                print("Fecha ingresada correctamente")
                break
            else:
                print("Fecha ingresada incorrectamente")
                fecha=input("Ingrese fecha de afiliación: dd-mm-aaaa: ")
        correo=input("Ingrese correo electrónico: ")
        while True:
            if re.match(validacion_correo, correo):
                print("Correo electrónico ingresado correctamente")
                break
            else:
                print("Correo electrónico ingresado incorrectamente")
                correo=input("Ingrese correo electrónico: ")
        registro={
            "RUT":rut,
            "Nombre":nombre,
            "Apellido":apellido,
            "Edad":edad,
            "Estado Civil":estado_civil,
            "Fecha de afiliación":fecha,
            "Correo Electrónico":correo
        }
        registros.append(registro)

        resp=input("Desea ingresar otro usuario. Si/No: ").lower()
        if resp!="si":
            system("clear")
            break
        else:
            system("clear")

def buscar():
    system("clear")
    while True:
        buscar_ec=input("Ingrese estado civil a buscar: ")
        encontrar=False
        for registro in registros:
            if registro["Estado Civil"]==buscar_ec:
                print(f"Persona encontrada\n{registro}")
                encontrar=True
                break
        if not encontrar:
            print("Sin registros")
        resp=input("Desea ingresar otro usuario. Si/No: ").lower()
        if resp!="si":
            system("clear")
            break
        else:
            system("clear")

def imprimir():
    system("clear")
    while True:
        rut_buscado=input("Ingrese rut: ")
        encontrar=False
        for registro in registros:
            if registro["RUT"]==rut_buscado:
                print("Rut encontrado\n")
                print(f'''
            CERTIFICADO AFILIACIÓN ISAPRE VIDA Y SALUD
                      
        Se otorga el presente certificado de afiliación a:
                      
{registro["Nombre"]} {registro["Apellido"]}, RUT {registro["RUT"]}, edad {registro["Edad"]} años,
estado civil {ec_dic[registro["Estado Civil"]]},
afiliado en esta institución desde el {registro["Fecha de afiliación"]}.

Se otorga este certificado de afiliación para los fines que estime conveniente.

Sin otro particular.

                    ISAPRE VIDA Y SALUD
''')
                encontrar=True
                break
        if not encontrar:
            print("Sin registros")
        resp=input("Desea ingresar otro rut. Si/No: ").lower()
        if resp!="si":
            break

def salir():
    system("clear")
    print('''
Saliendo del programa...
Felipe Andrés
v. 1.0
''')
    exit()

def menu_principal():
    system("clear")
    while True:
        print('''
MENÚ PRINCIPAL:
1. Guardar Datos Persona
2. Buscar por Estado Civil
3. Imprimir Certificado Afiliación
4. Salir
''')
        op=input("Ingrese una opción: ")
        if op=="1":
            guardar()
        elif op=="2":
            buscar()
        elif op=="3":
            imprimir()
        elif op=="4":
            salir()
        else:
            input("Opción incorrecta. Presione 'Enter' para continuar")

menu_principal()

