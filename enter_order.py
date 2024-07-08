from os import system
system("clear")

import re
import random

sectores=["Concepción", "Chiguayante", "Talcahuano", "Hualpén", "San Pedro"]
registros=[]
validacion_calle = r'^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ.\'`´\- ]+( \d+)( de la (Carrera|Calle|Avenida|Av\.) \w+)?$'



def registrar_pedido():
    system("clear")
    while True:
        while True:
            cliente = input("Ingrese nombre(s) y apellido(s) del cliente: ").strip().title()
            nombres = cliente.split()
            
            if len(nombres) > 1 and all(nombre.isalpha() and len(nombre) >= 3 for nombre in nombres):
                print("Nombre registrado correctamente")
                break
            else:
                print("Datos ingresados incorrectamente.")

        
        direccion=input("Ingrese dirección: ").strip().title()
        while True:
            if re.match(validacion_calle, direccion):
                print("Dirección registrada correctamente")
                break
            else:
                print("Formato de dirección incorrecto. Por favor ingrese una dirección válida.")
                direccion=input("Ingrese dirección: ").strip().title()
        
        comuna = input("Ingrese comuna: ").strip().title()
        while comuna not in sectores:
            print("Comuna no disponible")
            comuna = input("Ingrese comuna: ").strip().title()
            print("Comuna registrada correctamente")
        
        detalle=print("Ingrese la cantidad de dispensadore a solicitar:")
        
        dispensador_6_lts = 0
        dispensador_10_lts = 0
        dispensador_20_lts = 0

        while True:
            try:
                dispensador_6_lts = int(input("¿Cuántos dispensadores de 6 litros necesita?: "))
                dispensador_10_lts = int(input("¿Cuántos dispensadores de 10 litros necesita?: "))
                dispensador_20_lts = int(input("¿Cuántos dispensadores de 20 litros necesita?: "))
                
                if dispensador_6_lts != 0 or dispensador_10_lts != 0 or dispensador_20_lts != 0:
                    break
                else:
                    print("Debe solicitar al menos un dispensador. Intente de nuevo.")
            except ValueError:
                print("Cantidad inválida. Por favor, ingrese un número entero.")
                
        print(f"Ha solicitado: {dispensador_6_lts} dispensador(es) de 6 litros, {dispensador_10_lts} dispensador(es) de 10 litros y {dispensador_20_lts} dispensador(es) de 20 litros.")

        registro={
            "ID pedido":random.randint(1, 1000000),
            "Nombre":cliente,
            "Dirección":direccion,
            "Comuna":comuna,
            "Disp. 6 lts":dispensador_6_lts,
            "Disp. 10 lts":dispensador_10_lts,
            "Disp. 20 lts":dispensador_20_lts
        }

        registros.append(registro)


        resp = input("¿Desea ingresar otro pedido? (si/no): ").strip().lower()
        if resp != 'si':
            break
        system("clear")



def listar_pedidos():
    if not registros:
        print("No hay pedidos registrados")
        #return
    else:
        print(f"{'ID pedido':<15} {'Cliente':<20} {'Dirección':<20} {'Sector':<15} {'Disp. 6 lts':<15} {'Disp. 10 lts':<15} {'Disp. 20 lts':<15}\n")
        for registro in registros:
            print(f"{registro['ID pedido']:<15} {registro['Nombre'][:20]:<20} {registro['Dirección'][:20]:<20} {registro['Comuna']:<15} {registro['Disp. 6 lts']:<15} {registro['Disp. 10 lts']:<15} {registro['Disp. 20 lts']:<15}")
    
    input("\nPresione 'Enter' para continuar...")



def imprimir_hojas_ruta():
    while True:
        system("clear")
        print('''
Menú Hojas de Ruta:\n
1. Imprimir todas las hojas de rura
2. Imprimir filtrando por sector
3. Regresar al Menú principal
''')
        
        op2=input("\nIngrese una opción: ")

        if op2=="1":#Todas las hojas de ruta
            if not registros:
                print("No hay pedidos registrados")
            else:
                with open("hoja_rutas.txt", "w") as archivo:
                    archivo.write(f"{'ID pedido':<15} {'Cliente':<20} {'Dirección':<20} {'Sector':<15} {'Disp. 6 lts':<15} {'Disp. 10 lts':<15} {'Disp. 20 lts':<15}\n")
                    for registro in registros:
                        archivo.write(f"{registro['ID pedido']:<15} {registro['Nombre'][:20]:<20} {registro['Dirección'][:20]:<20} {registro['Comuna']:<15} {registro['Disp. 6 lts']:<15} {registro['Disp. 10 lts']:<15} {registro['Disp. 20 lts']:<15}\n")
                print("Hoja de rutas generado como 'hoja_rutas.txt'.\n")
            
            input("Presione 'Enter' para continuar...")
        
        elif op2 == "2":#Hojas de rutas filtradas por sector
            while True:
                system("clear")
                print("Sectores disponibles: ", sectores)
                comuna = input("Ingrese el sector a filtrar ('Enter' para volver a 'Menú Hoja de Rutas'): ").strip().title()

                if comuna == " ":
                    break

                if comuna not in sectores:
                    input("Sector no válido. Presione 'Enter' para intertar nuevamente.\n")
                else:
                    with open(f"hoja_ruta_{comuna}.txt", "w") as archivo:
                        archivo.write(f"{'ID pedido':<15} {'Cliente':<20} {'Dirección':<20} {'Sector':<15} {'Disp. 6 lts':<15} {'Disp. 10 lts':<15} {'Disp. 20 lts':<15}\n")
                        for registro in registros:
                            if registro["Comuna"] == comuna:
                                archivo.write(f"{registro['ID pedido']:<15} {registro['Nombre'][:20]:<20} {registro['Dirección'][:20]:<20} {registro['Comuna']:<15} {registro['Disp. 6 lts']:<15} {registro['Disp. 10 lts']:<15} {registro['Disp. 20 lts']:<15}\n")
                        print(f"Hoja de ruta generada para {comuna} como 'hoja_ruta_{comuna}.txt'.\n")
                    input("Presione 'Enter' para continuar...")
                    break

        elif op2 == "3":
            break

        else:
            print("Opción no válida. Por favor, ingrese una opción correcta.")
            input("Presione 'Enter' para continuar...")



def buscar_pedido_id():
    system("clear")
    while True:
        id_buscado = input("Ingrese el ID del pedido a buscar: ")
        encontrado = False
        for registro in registros:
            if str(registro['ID pedido']) == id_buscado:
                print(f"Pedido encontrado:\n")
                print(f"{'ID pedido':<15} {'Cliente':<20} {'Dirección':<20} {'Sector':<15} {'Disp. 6 lts':<15} {'Disp. 10 lts':<15} {'Disp. 20 lts':<15}")
                print(f"{registro['ID pedido']:<15} {registro['Nombre'][:20]:<20} {registro['Dirección'][:20]:<20} {registro['Comuna']:<15} {registro['Disp. 6 lts']:<15} {registro['Disp. 10 lts']:<15} {registro['Disp. 20 lts']:<15}")
                encontrado = True
                break
        
        if not encontrado:
            print(f"No se encontró ningún pedido con el ID {id_buscado}")
            resp=input("Presione 'Enter' para intertar nuevamente o '0' para regresar a 'Menú Hoja de Rutas': ")

            if resp == "0":
                break
        else:
            input("Presione 'Enter' para continuar...")



def menu_principal():
    while True:
        system("clear")
        print('''
Menú principal:\n
1. Registrar pedido
2. Listar los todos los pedidos
3. Imprimir hoja de ruta
4. Buscar un pedido por ID
5. Salir del programa
''')
        op1 = input("\nIngrese una opción: ")
        if op1 == "1":
            registrar_pedido()
        elif op1 == "2":
            listar_pedidos()
        elif op1 == "3":
            imprimir_hojas_ruta()
        elif op1 == "4":
            buscar_pedido_id()
        elif op1 == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Su opción ingresada es incorrecta")
            input("Presione 'Enter' para continuar")

menu_principal()

#if __name__ == "__main__":
    #menu_principal()
