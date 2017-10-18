# -*- coding: utf-8 -*-

import os
import sys

#Limpia la terminal de todos los caracteres
def limpiarPantalla():
    if sys.platform == "win32":
        os.system('cls')
    else: 
        os.system('clear')
    
#Funcion de inicio de la calculadora
def inicio():
    limpiarPantalla()

#Funcion encargada de decidir que menu se muestra
#retorna la opcion escogida del menu    
def mostrarMenus(menu):
    if (menu == 1):
        menuUno()
    elif (menu == 2):
        menuArit()
    elif (menu == 3):
        menuGeom()
    return input("Ingrese opcion: ")

#Ve el menu y opcion elegidos y ejecuta la accion deseada.
#Esta puede ser un cambio de menu o una accion puntual como una suma
#o el calculo de un area
def ejecutarAccion(menu, opcion):
    if (menu == 1):
        if (opcion == "1"):
            menu = 2 #Cambiamos al menu aritmetico
        elif (opcion == "2"):
            menu = 3 #Cambiamos al menu geometrico
        elif (opcion == "99"):
            menu = 0 #Ponemos menu en 0 para terminar el programa
    elif (menu == 2):
        if (opcion == "1"):
            suma() #Suma
        elif (opcion == "2"):
            multiplicacion()
        elif (opcion == "99"):
            menu = 1
    elif (menu == 3):
        if (opcion == "1"):
            areaRect() #Suma
        elif (opcion == "2"):
            areaCirc()
        elif (opcion == "99"):
            menu = 1
    return menu


################### Menues #############################################

def menuUno():
    limpiarPantalla()
    print ("Menu Principal:")
    print ("	1  - Menu aritmetico")
    print ("	2  - Menu geometrico")
    print ("	99 - Salir")

def menuArit():
    limpiarPantalla()
    print ("Menu Aritmetico:")
    print ("	1  - Suma")
    print ("	2  - Multiplicacion")
    print ("	99 - Menu principal")    

def menuGeom():
    limpiarPantalla()
    print ("Menu Geometrico:")
    print ("	1  - Area rectangulo")
    print ("	2  - Area circulo")
    print ("	99 - Menu principal")

#################### Acciones ########################################### 

def suma():
    limpiarPantalla()
    try:
        v1 = float(input("Ingrese primer valor: "))
        v2 = float(input("Ingrese segundo valor: "))
        print("%f + %f = %f" % (v1, v2, v1 + v2))
    except ValueError:
        print ("No ingresaste un numero!")
    input("Presione cualquier tecla y enter para seguir....")

def multiplicacion():
    limpiarPantalla()
    try:
        v1 = float(input("Ingrese primer valor: "))
        v2 = float(input("Ingrese segundo valor: "))
        print("%f * %f = %f" % (v1, v2, v1 * v2))
    except ValueError:
        print ("No ingresaste un numero!")
    input("Presione cualquier tecla y enter para seguir....")

def areaCirc():
    limpiarPantalla()
    try:
        v1 = float(input("Ingrese el radio: "))
        print("%f * %f * Pi  = %f" % (v1, v1 ,v1 * v1 * 3.1416))
    except ValueError:
        print ("No ingresaste un numero!")
    input("Presione cualquier tecla y enter para seguir....")

def areaRect():
    limpiarPantalla()
    try:
        v1 = float(input("Ingrese el largo: "))
        v2 = float(input("Ingrese el ancho: "))
        print("%f * %f = %f" % (v1, v2 , v1 * v2))
    except ValueError:
        print ("No ingresaste un numero!")
    input("Presione cualquier tecla y enter para seguir....")

    
################## Programa principal ###########################################

    
menu = 1
terminar = False    
inicio()
while(not terminar):
    opcion   = mostrarMenus(menu)
    menu     = ejecutarAccion(menu, opcion)
    terminar = (menu == 0)

limpiarPantalla()
print ("Hasta luego !!!! ")

