import os
from lista_doble import Lista_Doblemente
import webbrowser

CONTACTOS=Lista_Doblemente()
def OP1():
    global CONTACTOS
    os.system('cls')
    print("------------------ Ingresar Nuevo Contacto ------------------")
    print ("")
    
    condicion=True
    while condicion:
        nombre=""
        apellido=""
        telefono=""
        print("\n-Ingrese Nombre\n")
        nombre=input("   >>  ")
        print("\n-Ingrese Apellido\n")
        apellido=input("   >>  ")
        print("\n-Ingrese Teléfono\n")
        telefono=input("   >>  ")

        if nombre!="" and apellido!="" and telefono!="":
            if CONTACTOS.verificando_contacto(nombre)==False:
                print("El usuario ya existe")
            else:
                CONTACTOS.Insertar_Nodo(nombre,apellido,telefono)
                print("Se agregó correctamente")
            condicion=False
        else:
            input("Debe llenar todos los campos...")
            os.system('cls')
            print("------------------ Ingresar Nuevo Contacto ------------------")
            print ("")
    
    
        

def OP2():
    os.system('cls')
    print("------------------ Buscar contacto ------------------")
    print ("")
    print("-Ingrese Número\n")
    numero=input("   >>  ")
    condicion2=True
    while condicion2:
        if numero!="":
            if CONTACTOS.buscar(numero)==False:
                print("")
            else:
                print("El numero de teléfono no existe ¿ Desea agregarlo ?")
                print("\n1-SI")
                print("2-NO\n")
                opcion=input("              >>  ")
                if opcion=="1":
                    print ("")
                    OP1()
                elif opcion=="2":
                    MENU()
                else:
                    print ("***ERROR****")
                    os.system('cls')
                    input("No has pulsado ninguna opción correcta...\npulsa enter para volver...")
            condicion2=False
        else:
            input("Debe llenar todos los campos...")
            os.system('cls')
            print("------------------ Buscar contacto ------------------")
            print ("")
            print("-Ingrese Número\n")
            numero=input("   >>  ")
        

def OP3():
    global CONTACTOS
    os.system('cls')
    print("------------------ Visualizar Agenda ------------------")
    print ("")
    CONTACTOS.recorrer_lista()
    CONTACTOS.visualizar()
    webbrowser.open_new_tab('AGENDA.png')

def OP4():
    os.system('cls')
    print("------------------ Primer Contacto ------------------")
    print ("")
    CONTACTOS.obtener_primero()

def OP5():
    os.system('cls')
    print("------------------ Ultimo Contacto ------------------")
    print ("")
    CONTACTOS.obtener_ultimo()

def OP6():
    os.system('cls')
    print("------------------  Modificar Contacto ------------------")
    print ("")
    print("-Ingrese Número de Contacto\n")
    numero=input("   >>  ")

    condicion2=True
    while condicion2:
        if numero!="":
            if CONTACTOS.buscar2(numero)==False:
                print("")
                print("----Ingrese los nuevos datos----")
                print("Nombre:")
                nombre=input("              >>  ")
                print("Apellido:")
                apellido=input("              >>  ")
                print("Numero:")
                numero_nuevo=input("              >>  ")
                if nombre!="" and apellido!="" and numero_nuevo!="":
                    CONTACTOS.Modificar(nombre,apellido,numero,numero_nuevo)
                    print("Se modificó correctamente")
                else:
                    print("*Debe de llenar todos los campos")
                    OP6() 

            else:
                print("El numero de teléfono no existe ¿ Desea agregarlo ?")
                print("\n1-SI")
                print("2-NO\n")
                opcion=input("              >>  ")
                if opcion=="1":
                    print ("")
                    OP1()
                elif opcion=="2":
                    MENU()
                else:
                    print ("***ERROR****")
                    os.system('cls')
                    input("No has pulsado ninguna opción correcta...\npulsa enter para volver...")
            condicion2=False
        else:
            print("*Debe de llenar todos los campos")
            OP6() 

def OP7():
    os.system('cls')
    print("------------------ Eliminar contacto ------------------")
    print ("")
    print("-Ingrese Número\n")
    numero=input("   >>  ")

    condicion2=True
    while condicion2:
        if numero!="":
            if CONTACTOS.buscar2(numero)==False:
                if numero!="":
                    if CONTACTOS.size==1:
                        CONTACTOS.eliminar_inicio()
                        print("Se eliminó correctamente")
                    else:
                        CONTACTOS.eliminar(numero)
                        print("Se eliminó correctamente")
                else:
                    print("*Debe de llenar todos los campos")
                    OP7() 

            else:
                print("El numero de teléfono no existe ¿ Desea agregarlo ?")
                print("\n1-SI")
                print("2-NO\n")
                opcion=input("              >>  ")
                if opcion=="1":
                    print ("")
                    OP1()
                elif opcion=="2":
                    MENU()
                else:
                    print ("***ERROR****")
                    os.system('cls')
                    input("No has pulsado ninguna opción correcta...\npulsa enter para volver...")
            condicion2=False
        else:
            print("*Debe de llenar todos los campos")
            OP7() 

def MENU():	
    os.system('cls')
    print("___________________________________________________________________________________")
    print("                                                                                              ")
    print ("        \t              1 - Ingresar Nuevo Contacto          ")
    print ("        \t              2 - Buscar Contacto          ")
    print ("        \t              3 - Visualizar Agenda          ")
    print ("        \t              4 - Visualizar Primer Contacto          ")
    print ("        \t              5 - Visualizar Ultimo Contacto          ")
    print ("        \t              6 - Modificar Contacto          ")
    print ("        \t              7 - Eliminar Contacto          ")
    print ("        \t              8 - Salir")
    print("___________________________________________________________________________________")

while True:
    MENU()
    print("\n          -------------Seleccione una Opción-------------\n")
    op=input("              >>  ")
    if op=="1":
        print ("")
        OP1()
        input("\npulsa enter para volver...")
    elif op=="2":
        print ("")
        os.system('cls')
        OP2()
        input("\npulsa enter para volver...")
    elif op=="3":
        print ("")
        os.system('cls')
        OP3()
        input("\npulsa enter para volver...")
    elif op=="4":
        print ("")
        os.system('cls')
        OP4()
        input("\npulsa enter para volver...")
    elif op=="5":
        print ("")
        os.system('cls')
        OP5()
        input("\npulsa enter para volver...")
    elif op=="6":
        print ("")
        os.system('cls')
        OP6()
        input("\npulsa enter para volver...")
    elif op=="7":
        print ("")
        os.system('cls')
        OP7()
        input("\npulsa enter para volver...")    
    elif op=="8":
        os.system('cls')
        break
    else:
        print ("***ERROR****")
        os.system('cls')
        input("No has pulsado ninguna opción correcta...\npulsa enter para volver...")
        MENU()

