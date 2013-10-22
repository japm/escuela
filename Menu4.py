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
    return raw_input("Ingrese opcion: ")

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
        if (opcion == "99"):
            menu = 1
    elif (menu == 3):
        if (opcion == "99"):
            menu = 1
    return menu
    
def menuUno():
    limpiarPantalla()
    print "Menu Principal:"
    print "	1  - Menu aritmetico"
    print "	2  - Menu geometrico"
    print "	99 - Salir"

def menuArit():
    limpiarPantalla()
    print "Menu Aritmetico:"
    print "	1  - Suma"
    print "	2  - Multiplicacion"
    print "	99 - Menu principal"    

def menuGeom():
    limpiarPantalla()
    print "Menu Geométrico:"
    print "	1  - Area rectangulo"
    print "	2  - Area circulo"
    print "	99 - Menu principal"    

menu = 1
terminar = False    
inicio()
while(not terminar):
    opcion   = mostrarMenus(menu)
    menu     = ejecutarAccion(menu, opcion)
    terminar = (menu == 0)

limpiarPantalla()
print "Hasta luego !!!! "

