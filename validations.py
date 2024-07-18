#VALIDACIONES

from os import system
system("clear")
from random import randint
import re


validacion_correo = r'[^@]+@[^@]+\.[^@]+' #EXPRESION REGULAR=import re


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
