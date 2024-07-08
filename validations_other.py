from os import system
system("clear")

#VALIDAR NOMBRE
while True:
    cliente = input("Ingrese nombre(s) y apellido(s) del cliente: ").strip().title()
    nombres = cliente.split()
    if len(nombres) > 1 and all(nombre.isalpha() and len(nombre) >= 3 for nombre in nombres):
        print("\nNombre registrado correctamente\n")
        print(cliente)
        break
    else:
        print("Datos ingresados incorrectamente.")

#VALIDAR CALLE
import re
validacion_calle = r'^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ.\'`´\- ]+( \d+)( de la (Carrera|Calle|Avenida|Av\.) \w+)?$'
direccion=input("Ingrese dirección: ").strip().title()
while True:
        if re.match(validacion_calle, direccion):
            print("Dirección registrada correctamente")
            break
        else:
            print("Formato de dirección incorrecto. Por favor ingrese una dirección válida.")
            direccion=input("Ingrese dirección: ").strip().title()

#VALIDAR CORREO op1
while True:
    correo=input("Ingrese su correo electrónico: ")
    if "@" in correo:
        print("Correo ingresado correctamente")
        break
    else:
        print("Debe ingresar un correo válido")

#VALIDAR CORREO op2

correo=input("Ingrese correo: ")
if '@' in correo:
    partes=correo.split('@')
    print(partes) 
    usuario=partes[0]
    dominio=partes[1]
    if len(usuario)>0 and '.' in dominio and len(usuario.replace(" ", ""))!=0 :
        print("Correo válido") 
    else:
        print("Correo peeeeeenca!!!!")
else:
    print("Correo super peeeeeenca!!!!")