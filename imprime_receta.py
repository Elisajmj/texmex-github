#!/usr/bin/python3

import sys
import argparse

#Funcion para mostrar el contenido del fichero que se recibe como argumeto
def mostrar_contenido(fichero):
	#contenido = fichero.read()
	contenido = open(fichero, 'r')
	print(contenido.read())
	
	return contenido  

#Descripcion de lo que hace el script
parser = argparse.ArgumentParser(description='Mostrar contenido de Fichero pasado como argumento')
parser.add_argument('fichero', metavar='F', type=argparse.FileType('r'), help='Fichero cuyo contenido quiero imprimir')
args = parser.parse_args()

#Mostramos el resultado  de la lectura del fichero
mostrar_contenido(sys.argv[1])

sys.exit()


