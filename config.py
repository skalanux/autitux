# -*- coding: latin-1 -*-
# $Id: config.py,v 1.2 2004/10/01 18:05:51 mbenedettini Exp $

""" 
Modulo para cargar el archivo de configuracion.
Donde queramos usarlo insertamos la siguiente linea:
    from sisalud.util.config import config
y ya tenemos disponible un diccionario config con los valores.
"""

import sys, os
import ConfigParser

config = {}

cfgParser = ConfigParser.SafeConfigParser()

#busco el archivo de configuracion en sys.path
#for path in sys.path:
#    file = path + os.sep + "sisalud" + os.sep + "sisalud.conf"
#    try:
#       fp = open(file)
#       cfgParser.readfp(fp)
#       fp.close()
#   except:
#       pass


fp = open("sisalud.conf")
cfgParser.readfp(fp)
fp.close()

# si no hay config
if not cfgParser.sections():
    raise Exception("No se pudo leer el archivo de configuracion o esta vacio, la ultima ubicacion intentada fue: %s" % file)
else:
    #construyo el diccionario config con los secciones y valores
    for section in cfgParser.sections():
        config[section] = {}
        for item, value in cfgParser.items(section):
            config[section][item] = value
    
