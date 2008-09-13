import autituxhelper
import time
import gobject
import threading
import thread
import gtk
def parseCommands(instruction):
    """
    This is for parsing instructions like 8:10;4:5
    """
    return instruction.split(";")


def splitLogoCommand(logoCommand):
    return logoCommand.split(":");


def executeLogoCommands(logoCommands):
    """
    n: north
    w: west
    s: south
    e: east
    nw: northwest
    nw: nothwest
    sw: southwest
    se: southeast
    """
    
    commandsArray = parseCommands(logoCommands)
    
    for singleInstruction in commandsArray:
        singleLogoCommand = splitLogoCommand(singleInstruction)
       
        print singleLogoCommand[1]
 
        if singleLogoCommand[0] == "n":
            #thread.start_new( goNorth, ( singleLogoCommand[1], ) )
            goNorth(singleLogoCommand[1])

    	if singleLogoCommand[0] == "s":
            goSouth(singleLogoCommand[1])

     	if singleLogoCommand[0] == "e":
	        goEast(singleLogoCommand[1])

    	if singleLogoCommand[0] == "w":
	        goWest(singleLogoCommand[1])

    
def goSouth(lapse=-1):
    """
    This function takes care of going north 
    """
    comma = autituxhelper.relayCommand()
 
    comma.toggle(8, 0)
    comma.toggle(4, 1)

    if lapse != -1:
        time.sleep(0.1* int(lapse))
        comma.toggle(4,0)

            
def goNorth(lapse=-1):
    """
    This function takes care of going north 
    """
    comma = autituxhelper.relayCommand()
 
    comma.toggle(4, 0)
    comma.toggle(8, 1)

    if lapse != -1:
        time.sleep(0.1* int(lapse))
        comma.toggle(8,0)

def goEast(lapse=-1):
    """
    This function takes care of going north 
    """
    comma = autituxhelper.relayCommand()
 
    comma.toggle(7, 0)
    comma.toggle(5, 1)

    if lapse != -1:
        time.sleep(0.1* int(lapse))
        comma.toggle(5,0)
          
def goWest(lapse=-1):
    """
    This function takes care of going north 
    """
    comma = autituxhelper.relayCommand()
 
    comma.toggle(5, 0)
    comma.toggle(7, 1)

    if lapse != -1:
        time.sleep(0.1* int(lapse))
        comma.toggle(7,0)
