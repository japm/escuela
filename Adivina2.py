# -*- coding: utf-8 -*-
import random
import time
import os
import sys

class Adivinanza:
	def __init__(self):
		self.osName = sys.platform
		self.secreto = random.randint(1,100)
		
	def imprimitTitulo(self):
		print "*******************************************************************************"
		print "************************   Adivina el Numero!!!   *****************************"
		print "*******************************************************************************"
		print ""
		
	def limpiarPantalla(self):
		if self.osName == "win32":
			os.system('cls')
		else: 
			os.system('clear')
	
	def pedirNumero(self):
		sel = raw_input("Ingrese el numero: ")
		nro = int(sel)
		return nro
	
	def pedirNumeroYLimpiarPantalla(self):
		nro = self.pedirNumero()
		self.limpiarPantalla()
		self.imprimitTitulo()
		return nro
	
	def comenzar(self):
		self.limpiarPantalla()
		self.imprimitTitulo()
	
	def jugar(self):
		self.comenzar()
		nro = self.pedirNumeroYLimpiarPantalla()
		while self.secreto != nro:
			if (nro > 100 or nro < 0):
				print "El numero debe ser entre 0 y 100"
			elif (nro < self.secreto):
				print "Ingrese un numero mas alto"
			else:
				print "Ingrese un numero mas bajo"
			nro = self.pedirNumeroYLimpiarPantalla()
			
		print "Lo encontraste !! era %i" % nro


juego = Adivinanza()
juego.jugar()