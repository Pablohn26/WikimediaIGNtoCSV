#!/usr/bin/python3

import sys
import re
from lxml import etree 
import csv

#Archivo XML que cargar
file = "../datos/ftppriv.cnig.es/17/xml/spaignActa_1923_05918020150591802015.xml"
#file = "../datos/ftppriv.cnig.es/01/xml/spaignActa_1927_05675720150567572015.xml"
#file = "./18/xml/spaignActa_1990_1042142015071042142015.xml"
#file = sys.argv[1]
root = etree.parse(file)

#Ruta del archivo con las definiciones de cada ruta (etiquetas)
tags_file="./acta_tags_list.txt"

#Objeto con un diccionario con clave la ruta y valor el nombre de la etiqueta
tags ={}

#Objeto con un diccionario con clave la ruta y valor el texto del elemento
data = {}


def load_tags(tags_file,tags):
    with open (tags_file) as f:
        for line in f:
            both_tags = line.split(':')
            tags[both_tags[0].replace(" ", "")]=both_tags[1]
    #print (tags.keys())


#Obtiene la ruta completa a cada elemento    
def get_parents(element):
    text = ""
    while element != None:
        text = sanitize_tag(element)+"/"+text
        #print (element.tag)
        element = element.getparent()
    return text


#Sanitiza el texto de salida eliminando la cadena de los namespaces del XML. 
def sanitize_tag(element):
   text = element.tag
   sanitized2 = text.replace("{http://www.isotc211.org/2005/gmd}","") 
   sanitized = sanitized2.replace("{http://www.isotc211.org/2005/gco}","") 
   return sanitized



#Carga de las etiquetas
load_tags(tags_file,tags)

#Diccionario para la gestión de etiquetas duplicadas
dup_tags = {}


#Gestiona las etiquetas duplicadas añadiendo un número al final de la etiqueta en caso de coincidencia
def update_key(dicct,kkey):
    if kkey in dup_tags:
        dup_tags[str(kkey)] = dup_tags[str(kkey)]+1
    else:
        dup_tags[str(kkey)] = 1
    return str(kkey)+str(dup_tags[str(kkey)])


#Bucle principal que recorre todo el XML imprimiendo la ruta y el contenido de cada elemento 
for element in root.iter():
    if element.text and not element.text.isspace():
#Imprimir etiqueta y contenido del XML
#        print("%s - %s" % (get_parents(element), element.text))
#Imprimir etiqueta del XML
#        print("%s" % (get_parents(element)))
        (key, val) = (get_parents(element), element.text)
        if key in data:
            data[str(update_key(data,key))] = val
        else: data[str(key)] = val

outputname = file + ".csv"

with open("prueba1.csv",'w') as f:
    w = csv.DictWriter(f, data.keys(),'raise')
    w.writeheader()
    w.writerow(data)



