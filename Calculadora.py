# -*- coding: utf-8 -*-
import random
import os
import sys

class Calculadora:
	def __init__(self):
		self.osName = sys.platform
		
	def imprimitTitulo(self):
		print "*******************************************************************************"
		print "****************************  Calculadora   ***********************************"
		print "*******************************************************************************"
		print ""
		
	def limpiarPantalla(self):
		if self.osName == "win32":
			os.system('cls')
		else: 
			os.system('clear')
	
	def cabecera(self):
		self.limpiarPantalla()
		self.imprimitTitulo()
		
	def opcionMenu(self):
		return raw_input("Ingrese opcion de menu: ")
		
	def pause(self):
		raw_input("Presiona Enter para continuar")
	
	def suma(self):
		try:
			self.cabecera()
			print "Suma"
			nro1 = float(raw_input("Ingrese 1er nro: "))
			nro2 = float(raw_input("Ingrese 2do nro: "))
			print "%f + %f = %f" % ( nro1, nro2, nro1 + nro2)
		except Exception as e:
			print "Error en suma"
		self.pause()

	def resta(self):
		try:
			self.cabecera()
			print "Resta"
			nro1 = float(raw_input("Ingrese 1er nro: "))
			nro2 = float(raw_input("Ingrese 2do nro: "))
			print "%f - %f = %f" % ( nro1, nro2, nro1 - nro2)
		except Exception as e:
			print "Error en resta"
		self.pause()
	
	def areaCirc(self):
		try:
			self.cabecera()
			print "Area circulo"
			pi = 2.1416
			radio = float(raw_input("Ingrese el radio: "))
			print "Area circulo = %f x Pi x Pi = %f" % ( radio, radio * pi * pi)
		except Exception as e:
			print "Error en area circulo"
		self.pause()
	
	def areaRect(self):
		try:
			self.cabecera()
			print "Area rectangulo"
			nro1 = float(raw_input("Ingrese largo: "))
			nro2 = float(raw_input("Ingrese ancho: "))
			print "Area rectangulo = %f x %f = %f" % ( nro1, nro2, nro1 * nro2)
		except Exception as e:
			print "Error en area rectanculo"
		self.pause()
		
	def menuPPal(self):
		self.cabecera()
		print "Menu Principal:"
		print "	1-  Calculadora aritmetica"
		print "	2-  Calculadora geometrica"
		print "	99- Salir"
	
	
	def menuArit(self):
		self.cabecera()
		print "Menu Aritmetico:"
		print "	1-  Suma"
		print "	2-  Resta"
		print "	99- Menu principal"
	
	
	def menuGeo(self):
		self.cabecera()
		print "Menu Geometria:"
		print "	1-  Area circulo"
		print "	2-  Area rectangulo"
		print "	99- Menu principal"
	
	def accionMenuPPal(self, val):
		if (val == "99"):
			return 0
		elif (val == "1"):
			return 2
		elif (val == "2"):
			return 3
		return 1
	
	
	def accionMenuArit(self, val):
		if (val == "99"):
			return 1
		elif val == "1":
			self.suma()
		else: 
			self.resta()
		return 2
	
	def accionMenuGeo(self, val):
		if (val == "99"):
			return 1
		elif val == "1":
			self.areaCirc()
		else: 
			self.areaRect()
		return 3
		
	def menues(self, menu):
		if (menu == 1):
			self.menuPPal()
		elif (menu == 2):
			self.menuArit()
		elif (menu == 3):
			self.menuGeo()
	
	def acciones(self, menu, sel):
		if (menu == 1):
			menu = self.accionMenuPPal(sel)
		elif (menu == 2):
			menu = self.accionMenuArit(sel)
		elif (menu == 3):
			menu = self.accionMenuGeo(sel)
		return menu
		
	def comenzar(self):
		menu = 1
		while (menu != 0):
			self.menues(menu)
			sel = self.opcionMenu()
			menu = self.acciones(menu, sel)
		

calc = Calculadora()
calc.comenzar()