# -*- coding: utf-8 -*-
import random
import time
import os
import sys

osName = sys.platform

def imprimitTitulo():
	print "*******************************************************************************"
	print "************************   Adivina el Numero!!!   *****************************"
	print "*******************************************************************************"
	print ""

def limpiarPantalla():
	if osName == "win32":
		os.system('cls')
	else: 
		os.system('clear')
	imprimitTitulo()

limpiarPantalla()

secreto = random.randint(1,100)
sel = raw_input("Ingrese el numero: ")
nro = int(sel)
limpiarPantalla()
while secreto != nro:
	if (nro > 100 or nro < 0):
		print "El numero debe ser entre 0 y 100"
	elif (nro < secreto):
		print "Ingrese un numero mas alto"
	else:
		print "Ingrese un numero mas bajo"
	sel = raw_input("Ingrese el numero: ")
	limpiarPantalla()
	nro = int(sel)

print "Lo encontraste !! era %i" % nro

