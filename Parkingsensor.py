#import sys
#sys . path . append ( "/home/pi/Grovepi/Software/Python/grove_rgb_lcd.py" )

import time
from grovepi import *
from grove_rgb_lcd import *

# Hvad for porte at div. sensorer er sat til
afstand = 4
buzzer = 8
led_red = 6
led_blue = 5
button = 7
#Beskriver hvad for sensor der er står for INPUT eller OUTPUT
pinMode(button, "INPUT")
pinMode(buzzer, "OUTPUT")
pinMode(led_red, "OUTPUT")
pinMode(led_blue, "OUTPUT")
time. sleep (1) # Venter 1 sec før den køre videre med resten af koden.

buzz = True # Sætter knappen(buzzer) til at være True
while True: # Køre en while try/loop med afstandmåler 
    try:
        distant = ultrasonicRead(afstand)
        print (distant, 'cm')
        dist = int (distant)
        
        if digitalRead(button):
            if buzz:
                buzz = False
            else:
                buzz = True
            print (buzz) #Printer ud til LDC om knappen er True eller False
    
        if distant > 100 : #If loop som køre på alt over 100cm
            digitalWrite (led_blue, 0) #LED er sat til at være slukket = 0
            digitalWrite (led_red, 0) #LED er sat til at være slukket = 0
            setText ( "Distance =" + str ( dist ) + "\n " + str (buzz)) #Skriver text ud til LCD med afstand og om knappen er Ture eller False
            time. sleep ( .3 )
        
        elif distant > 40: #If loop som køre på alt under 40cm
            digitalWrite (led_blue, 1) #LED er sat til at være tændt = 1
            digitalWrite (led_red, 0) #LED er sat til at være slukket = 0
            setText ( "Distance =" + str ( dist ) + "\n " + str (buzz))
            time. sleep ( .3 )
        
        elif distant > 35: #If loop som køre på alt under 35cm
            digitalWrite (led_blue, 0) #LED er sat til at være slukket = 0
            digitalWrite (led_red, 1) #LED er sat til at være tændt = 1
            if buzz == False: #If loop der kigger efter om knappen(buzz) er False(ikke trykket på)
                digitalWrite (buzzer , 0 )
            else:
                digitalWrite (buzzer , 1 )
            setText ( "Distance =" + str ( dist ) + "\n " + str (buzz))
            time. sleep ( .3 )
            digitalWrite (buzzer , 0 )
            time. sleep ( .6 )
        
        elif distant > 30: #If loop som køre på alt under 30cm
            digitalWrite (led_blue, 0) #LED er sat til at være slukket = 0
            digitalWrite (led_red, 1) #LED er sat til at være tændt = 1
            if buzz == False: #If loop der kigger efter om knappen(buzz) er False(ikke trykket på)
                digitalWrite (buzzer , 0 )
            else:
                digitalWrite (buzzer , 1 )
            setText ( "Distance =" + str ( dist ) + "\n " + str (buzz))
            time. sleep ( .25 )
            digitalWrite (buzzer , 0 )
            time. sleep ( .4 )
        
        elif distant > 25: #If loop som køre på alt under 25cm
            digitalWrite (led_blue, 0)#LED er sat til at være slukket = 0
            digitalWrite (led_red, 1) #LED er sat til at være tændt = 1
            if buzz == False: #If loop der kigger efter om knappen(buzz) er False(ikke trykket på)
                digitalWrite (buzzer , 0 )
            else:
                digitalWrite (buzzer , 1 )
            setText ( "Distance =" + str ( dist ) + "\n " + str (buzz))
            time. sleep ( .1 )
            digitalWrite (buzzer , 0 )
            time. sleep ( .2 )
        
        elif distant > 20: #If loop som køre på alt under 20cm
            digitalWrite (led_blue, 0)#LED er sat til at være slukket = 0
            digitalWrite (led_red, 1) #LED er sat til at være tændt = 1
            if buzz == False: #If loop der kigger efter om knappen(buzz) er False(ikke trykket på)
                digitalWrite (buzzer , 0 )
            else:
                digitalWrite (buzzer , 1 )
            setText ( "Distance =" + str ( dist ) + "\n " + str (buzz))
            time. sleep ( .1 )
            digitalWrite (buzzer , 0 )
            time. sleep ( .2 )
            
        elif distant > 15: #If loop som køre på alt under 15cm
            digitalWrite (led_blue, 0)
            digitalWrite (led_red, 1)
            if buzz == False:
                digitalWrite (buzzer , 0 )
            else:
                digitalWrite (buzzer , 1 )
            setText ( "Distance =" + str ( dist ) + "\n " + str (buzz))
            time. sleep ( .05 )
            digitalWrite (buzzer , 0 )
            digitalWrite (led_red, 0)
        
        elif distant > 10: #If loop som køre på alt under 10cm
            digitalWrite (led_blue, 0)
            digitalWrite (led_red, 1)
            if buzz == False:
                digitalWrite (buzzer , 0 )
            else:
                digitalWrite (buzzer , 1 )
            setText ( "Distance =" + str ( dist ) + "\n " + str (buzz))
            time. sleep ( .005 )
            digitalWrite (buzzer , 0 )
            digitalWrite (led_red, 0)
        else:
            digitalWrite (led_blue, 1)
            digitalWrite (led_red, 1)
            if buzz == False:
                digitalWrite (buzzer , 0 )
            else:
                digitalWrite (buzzer , 1 )
            setText ( "Distance =" + str ( dist ) + "\n " + str (buzz))
            for c in range (0, 20 ):
                setRGB ( 255 - c, 255 - c, 255 - c )
            #time. sleep ( .0039 )
            #digitalWrite (buzzer , 0 )        
    except TypeError : #Fanger evt. fejl er skriver en fejl kode "Error" ud til shell
        print ("Error")
    except IOError : #Fanger evt. fejl er skriver en fejl kode "Error" ud til shell
        print ("Error")