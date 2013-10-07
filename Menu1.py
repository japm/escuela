# -*- coding: utf-8 -*-
import random
import os
import sys

class Menues:
	def __init__(self):
		self.osName = sys.platform
		
	def limpiarPantalla(self):
		if self.osName == "win32":
			os.system('cls')
		else: 
			os.system('clear')
	
	def opcionMenu(self):
		return raw_input("Ingrese opcion de menu: ")
	
	def menuPPal(self):
		self.limpiarPantalla()
		print "Menu Principal:"
		print "	1-  Opcion 1"
		print "	2-  Opcion 2"
		print "	99- Salir"
	

menues= Menues()
menues.menuPPal()
menues.menuPPal()