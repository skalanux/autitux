import parallel
import sys

class relayCommand:
	def toggle(self, relay, state):
	
	    # convert "on" and "off" to binary:
	    if state == "on": state = 1
	    if state == "off": state = 0
	
	    # The commandline passes strings, so convert to integers
	    relay = int(relay)
	    state = int(state)
	
	    print `relay` + "," + `state`
	
	    status_file = "status.txt"
	
	    # See if the text file exists. If it doesn't, make it blank.
	    # No need to create it now, it'll be created later.
	    try:
	        p = open(status_file).read()
	    except:
	        p = "00000000"
	   
	    relay1 = p[7]
	    relay2 = p[6]
	    relay3 = p[5]
	    relay4 = p[4]
	    relay5 = p[3]
	    relay6 = p[2]
	    relay7 = p[1]
	    relay8 = p[0]
	
	    t = [relay8, relay7, relay6, relay5, relay4, relay3, relay2, relay1]   
	
	    # Sloppy way to adust the state of the relay based on new input:
	    if relay == 1 and state == 1: t[7] = "1"
	    if relay == 1 and state == 0: t[7] = "0"   
	
	    if relay == 2 and state == 1: t[6] = "1"
	    if relay == 2 and state == 0: t[6] = "0"   
	
	    if relay == 3 and state == 1: t[5] = "1"
	    if relay == 3 and state == 0: t[5] = "0"   
	
	    if relay == 4 and state == 1: t[4] = "1"
	    if relay == 4 and state == 0: t[4] = "0"   
	
	    if relay == 5 and state == 1: t[3] = "1"
	    if relay == 5 and state == 0: t[3] = "0"   
	
	    if relay == 6 and state == 1: t[2] = "1"
	    if relay == 6 and state == 0: t[2] = "0"   
	
	    if relay == 7 and state == 1: t[1] = "1"
	    if relay == 7 and state == 0: t[1] = "0"   
	
	    if relay == 8 and state == 1: t[0] = "1"
	    if relay == 8 and state == 0: t[0] = "0"   
	
	    #print t
	
	    # if relay = 0, override everything to be whatever state was passed:
	    if relay == 0 and state == 0:
	        t = "00000000"
	
	    if relay == 0 and state == 1:
	        t = "11111111"
	
	    # Build our binary number:
	    status_raw = ""
	    for l in t:
	        status_raw = status_raw + l
	
	    #print status_raw
	
	    text_file = open(status_file, "w")
	    text_file.write(status_raw)
	    text_file.close()
	       
	    # Officially convert it to binary:
	    x = int(status_raw, 2)
	
	    #print x
	
	    # Write to the parallel port:
	    port = parallel.Parallel()
	    port.setData(x)




