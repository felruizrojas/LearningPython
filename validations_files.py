#from math import ceil #ceil() = aproximar
from os import system
system("clear")
from random import randint
import re
import csv
from sys import exit

validacion_correo = r'[^@]+@[^@]+\.[^@]+' #EXPRESION REGULAR=import re

diccionarios=[]

def datos():
    while True:
        id = randint(1, 100)
        nombre=input("Ingrese nombre: ").capitalize()
        while True:#NOMBRE
            if nombre.isalpha() and len(nombre)>=3:
                print("Ingreso correcto")
                break
            else:
                print("Ingreso incorrecto")
                nombre=input("Ingrese nombre: ").capitalize()

        apellido=input("Ingrese apellido: ").capitalize()
        while True:#APELLIDO
            if apellido.isalpha() and len(apellido)>=3:
                print("Ingreso correcto")
                break
            else:
                print("Ingreso incorrecto")
                apellido=input("Ingrese apellido: ").capitalize()

        rut=input("Ingrese rut: ")
        while True:#RUT
            if len(rut)==9 or len(rut)==10 and rut[8]=="-":
                print("Ingreso correcto")
                break
            else:
                print("Ingreso incorrecto")
                rut=input("Ingrese rut: ")

        nac=input("Ingrese fecha de nacimiento: ")
        while True:#FECHA DE NACIMIENTO
            if len(nac)==10 and nac[2]=="-" and nac[5]=="-":
                print("Ingreso correcto")
                break
            else:
                print("Ingresada incorrecto")
                nac=input("Ingrese fecha de nacimiento: ")

        while True:#EDAD
            try:
                edad=int(input("Ingrese edad: "))
                if edad>=18:
                    print("Ingreso correcto")
                    break
                else:
                    print("Edad debe ser igual o mayor a 18")
            except ValueError:
                print("Debe ser un número entero")

        while True:#ESTADO CIVIL
            ec=input("Ingrese estado civil (C=Casado | S=Soltero | V=Viudo): ").lower()
            if ec=="c":
                estado_civil="casado"
                break
            elif ec=="s":
                estado_civil="soltero"
                break
            elif ec=="v":
                estado_civil="viudo"
                break
            else:
                print("Ingreso incorrecto")
                continue
        
        while True:#TELÉFONO
            telefono = input("Ingrese teléfono: ")
            if telefono.isdigit() and len(telefono) == 9:
                print("Ingreso correcto")
                break
            else:
                print("Ingreso incorrecto")
        
        correo=input("Ingrese correo electrónico: ")
        while not re.match(validacion_correo, correo):
            print("Ingreso incorrecto")
            correo=input("Ingrese correo electrónico: ")
        print("Ingreso correcto")

        diccionario={
            "ID":id,
            "Nombre":nombre,
            "Apellido":apellido,
            "RUT":rut,
            "Fecha de nacimiento":nac,
            "Edad": edad,
            "Estado civil":estado_civil,
            "Teléfono":telefono,
            "Correo electrónico":correo
        }
        diccionarios.append(diccionario)

        resp=input("¿Desea realizar otro ingreso? Si/No: ").lower()
        if resp!="si":
            system("clear")
            break
        else:
            system("clear")

def listar():
    if not diccionarios:
        print("Sin datos")
    else:
        print(f"{'ID':<15} {'Nombre':<20}\n")
        for listar in diccionarios:
            print(f"{listar['ID']:<15} {listar['Nombre'][:20]:<20}")
        input("\nPresione 'Enter' para continuar...")

'''def listar_por_ID():
    while True:
        buscar_id=input("Ingrese ID: ")
        if buscar_id not in diccionarios:
            print("Sin datos")
        else:
            with open(f"ID_{buscar_id}.txt", "w") as archivo:
                archivo.write(f"{'ID':<15} {'Nombre':<20}\n")
                for listarID in diccionarios:
                    if listarID["ID"] == buscar_id:
                        archivo.write(f"{listarID['ID']:<15} {listarID['Nombre'][:20]:<20}\n")
                print(f"Documento generado para {buscar_id} como 'ID_{buscar_id}.txt'.\n")
        resp=input("¿Desea realizar otro ingreso? Si/No: ").lower()
        if resp!="si":
            system("clear")
            break
        else:
            system("clear")'''

def listar_por_ID():
    while True:
        buscar_id = input("Ingrese ID: ")
        encontrado = False
        for listarID in diccionarios:
            if str(listarID["ID"]) == buscar_id:
                with open(f"ID_{buscar_id}.txt", "w") as archivo:
                    archivo.write(f"{'ID':<15} {'Nombre':<20}\n")
                    archivo.write(f"{listarID['ID']:<15} {listarID['Nombre'][:20]}\n")
                print(f"Documento generado para {buscar_id} como 'ID_{buscar_id}.txt'.\n")
                encontrado = True
                break
        if not encontrado:
            print("Sin datos")
        
        resp = input("¿Desea realizar otra búsqueda? Si/No: ").lower()
        if resp != "si":
            system("clear")
            break
        else:
            system("clear")

def archivo_txt():
    if not diccionarios:
        print("Sin datos")
    else:
        with open("archivo_txt.txt", "w") as archivo:
            archivo.write(f"{'ID':<15} {'Nombre':<20}\n")
            for archivotxt in diccionarios:
                archivo.write(f"{archivotxt['ID']:<15} {archivotxt['Nombre'][:20]:<20}\n")
            print("Documento generado como 'archivo_txt.txt'.\n")
            input("Presione 'Enter' para continuar...")

'''def archivo_csv():
    if not diccionarios:
        print("Sin datos")
    else:
        with open("archivo_csv.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            file.write(f"{"ID"[:15]:<15}{"Nombre"[:15]:<15}")
            for archivocsv in diccionarios:
                print(f"{archivocsv["ID"][:15]:<15}{archivocsv["Nombre"][:15]:<15}")
                file.close()'''

def archivo_csv():
    if not diccionarios:
        print("Sin datos")
    else:
        with open("archivo_csv.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Nombre"])
            for archivocsv in diccionarios:
                writer.writerow([archivocsv["ID"], archivocsv["Nombre"]])
            print("Documento generado como 'archivo_csv.csv'.\n")
            input("Presione 'Enter' para continuar...")

def salir():
    print("Programa finalizado")
    exit()

def menu_principal():
    while True:
        print('''
MENÚ PRINCIPAL\n
1. Ingresar datos
2. Listar elementos
3. Buscar por ID
4. Generar archivo txt
5. Generar archivo csv
6. Salir
''')
        op=input("Ingrese una opción: ")
        if op=="1":
            datos()
        elif op=="2":
            listar()
        elif op=="3":
            listar_por_ID()
        elif op=="4":
            archivo_txt()
        elif op=="5":
            archivo_csv()
        elif op=="6":
            salir()
        else:
            input("Opción incorrecta. 'Enter' para continuar")

menu_principal()