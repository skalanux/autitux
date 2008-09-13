import os
import sys
import optparse

def main():
    options, status = get_options_status()
    print options.commandName 
 
def get_options_status():
    usage = "usage: %prog [options]"
    description = "Mover el autitux segun un patron de comandos o con un comando preestablecido."
    status = True
    version = "1.0"
    parser = optparse.OptionParser(usage=usage, version=version,
                                      description=description)
    parser.add_option("-c", "--command", dest="commandName",
                      help="Nombre del comando a ejecutar")
    
    parser.add_option("-p", "--parameters", dest="parametersList",
                      help="Lista de parametros separados por ; ej: n:20;s:10;e:1")

    
    parser.add_option("-n", "--no-gui", dest="noGui",
                      action="store_true",
                      help="No arrancar la interfaz grafica")

    (options, args) = parser.parse_args()
    
    if not options.parametersList:
        if len(args) > 0:
            options.commandName = args[0]
    
	return options, status

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
