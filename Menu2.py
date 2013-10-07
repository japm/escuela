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
		print "	1-  Opcion 1"
		print "	2-  Opcion 2"
		print "	99- Salir"
		
	def comenzar(self):
		menu = 1
		while (menu != 99):
			self.menuPPal()
			menu = self.opcionMenu()
			print "Elegiste %i " % menu
			linea= "Empezando en %f"
			for x in range(30):
				sys.stdout.write(linea % ((30-x) * 0.1))
				time.sleep(0.1)
				self.restart_line()
				
		print "Fin"

menues = Menues()
menues.comenzar()