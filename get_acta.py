#!/usr/bin/python3

import sys
import re
from lxml import etree 
import csv

#Archivo XML que cargar
file = "01/xml/spaignActa_1927_05675720150567572015.xml"
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
#    print (tags.keys())



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


#Bucle principal que recorre todo el XML imprimiendo la ruta y el contenido de cada elemento 
for element in root.iter():
    if element.text and not element.text.isspace():
        print("%s - %s" % (get_parents(element), element.text))
#Estoy obligado a filtrar MD_Metadata/characterSet/MD_CharacterSetCode/ porque contiene un texto (la cadena utf8) que es un código del lenguaje 
        if get_parents(element) != "MD_Metadata/characterSet/MD_CharacterSetCode/":
            (key, val) = (get_parents(element), element.text)
            data[str(key)] = val

print ("Inicio del print de data")
print (data)
print ("Fin del print de data")


#with open('output.csv', 'w') as csvfile:
    #print (data.keys()) 
#    fieldnames = [next(iter(data.keys()))]
#    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='raise',delimiter=';')
#    writer.writeheader()
#    writer.writerow(data)

