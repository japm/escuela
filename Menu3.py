# -*- coding: utf-8 -*-
import os
import sys
import time

class Menues:
	def __init__(self):
		self.osName = sys.platform
		
		
	def restart_line(self):
		if self.osName == "win32":
			sys.stdout.write('\r')
		else: 
			sys.stdout.write('\r')
		sys.stdout.flush
		
	def limpiarPantalla(self):
		if self.osName == "win32":
			os.system('cls')
		else: 
			os.system('clear')
	
	def opcionMenu(self):
		return int(raw_input("Ingrese opcion de menu: "))
	
	def menuPPal(self):
		self.limpiarPantalla()
		print "Menu Principal:"
		print "	1  - Opcion 1"
		print "	2  - Opcion 2"
		print "	99 - Salir"
		
	def menuDos(self):
		self.limpiarPantalla()
		print "Menu Dos:"
		print "	1  - Menu Dos -- Opcion 1"
		print "	2  - Menu Dos -- Opcion 2"
		print "	99 - Volver"
		
	def comenzar(self):
		menu = 1
		while (menu != 99):
			if (menu == 1):
				self.menuPPal()
			else:
				self.menuDos()
			menuAux = self.opcionMenu()
			if (menu == 2 and menuAux == 99):
				menu = 1
			elif (menu == 2 and menuAux == 1):
				menu = 2
			else: 
				menu = menuAux
			
		print "Fin"

menues = Menues()
menues.comenzar()