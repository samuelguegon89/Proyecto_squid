#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

accion = sys.argv[1]
tipo = sys.argv[2]
nombre = sys.argv[3]

if accion == "-a":
	if tipo == "-url":
		archivo = open('/etc/squid3/listanegra_url.acl','a')
		archivo.write(nombre)
		archivo.write('\n')
		archivo.close()
		print "La dirección %s ha sido añadida" % (nombre)
	elif tipo == "-dom":
		archivo = open('/etc/squid3/listanegra_dom.acl','a')
		archivo.write(nombre)
		archivo.write('\n')
		archivo.close()
		print "El dominio %s ha sido añadido" % (nombre)
	else:
		print "Los argumentos no son válidos."	
		print "Introduzca `-url` para añadir una dirección o `-dom` para añadir un dominio"
elif accion == "-d":
	if tipo == "-url":
		archivo = open('/etc/squid3/listanegra_url.acl','r')
		contenido = archivo.readlines()
		archivo.close()
		archivo = open('/etc/squid3/listanegra_url.acl','w')
		for i in contenido:
			if i != nombre+"\n":
				archivo.write(i)
		archivo.close()
		print "La dirección %s ha sido borrada" % (nombre)
	elif tipo == "-dom":
		archivo = open('/etc/squid3/listanegra_dom.acl','r')
		contenido = archivo.readlines()
		archivo.close()
		archivo = open('/etc/squid3/listanegra_dom.acl','w')
		for i in contenido:
			if i != nombre+"\n":
				archivo.write(i)
		archivo.close()	
		print "El dominio %s ha sido borrado" % (nombre)
	else:
		print "Los argumentos no son válidos."	
		print "Introduzca `-url` para añadir una dirección o `-dom` para añadir un dominio"
else:
	print "Los argumentos no son válidos."	
	print "Introduzca `-a` para añadir o `-d` para borrar"
	
