# Denne kode bruges til og indikere en afstand samt give brugeren baade visuel og auditiv information omkring afstanden.
# Der er lagt en "Mute" knap ind til buzzeren. Dette er den lille knap ved navn "Button v1.2".
# Man kan se knappens status paa skaermen : True = Lyd ud af buzzer   False = Ingen lyd ud af buzzer
#
# Dette er en "Parking Sensor" som bruger foelgende komponenter
# 
# Raspberry Pi 3b
#   8gb microSD
# GrovePi+
#   Roed LED
#   Blaa LED
#   Ultrasonic Ranger
#   Button v1.2
#   Buzzer v1.2
#   Grove-LCD RGB Backlight v4.0
########################################################################################
#
# ________________$$$$__________________$$$$
# _______________$__$$_________________$$__$
# ______________$$___$_________________$___$$
# ______________$$___$_________________$___$$
# _____________$$___$$_________________$___$$
# ____________$$____$__________________$____$$
# __________$$$____$$__________________$$____$$$
# _________$$_____$$____________________$$_____$$
# ________$$______$$____________________$$______$$
# _______$$_______$_______________________$_______$$
# ______$$________$$$$$$$___________$$$$$$$________$$
# __$$$$$_______________$$$_______$$$_______________$$$$
# _$$$____________$$$$____$$_____$$____$$$$____________$$
# $$____________$$$__$$$___$_____$___$$$__$$$___________$
# $____________$$$________$$_____$$________$$$___________$
# $____________$$$$$$____$$_______$$____$$$$$$___________$
# $___________$$____$$$$$$$_______$$$$$$$____$$__________$
# $___________$$$$_______$$_______$$_______$$$$__________$
# $$_________$$__$$$$$$$$$_________$$$$$$$$$__$$________$
# _$$$$_____$$$$________$___________$________$$$$______$$
# __$$$$$____$$$$$$____$$___________$$____$$$$$$____$$$$
# ______$$__$$____$$$$$$_____________$$$$$$____$$__$$
# _______$$$_$$$_____$________________$_____$$$_$$$
# _________$$$$$$$$$$__________________$$$$$$$$$..
#
#
# Dette er inspireret af Axel fra programmering, som koerte ind i min bil uden og sige noget, og saa var jeg selv noedt til og finde ud af hvem bilen tilhoerte. Dette vil jeg gerne undgaa naeste gang
#                                                                                                                                                                   - Daniel B. Kjeldsen
#
#
# Authors : Daniel B. Kjeldsen  & Thomas Brilli
#

import time
from grovepi import *
from grove_rgb_lcd import *

# Hvilke porte, forskellige moduler er forbundet til
afstand = 4
buzzer = 8
led_red = 6
led_blue = 5
button = 7
#Beskriver hvordan forskellige sensor skal agere med enten INPUT eller OUTPUT
pinMode(button, "INPUT")
pinMode(buzzer, "OUTPUT")
pinMode(led_red, "OUTPUT")
pinMode(led_blue, "OUTPUT")
time. sleep (1) # Et sekunds ventetid foer koden fortsaetter

buzz = True # Saetter knappen(buzzer) til at vaere True
while True: # Koerer et "while try/loop" med afstandsmaaler 
    try:
        distant = ultrasonicRead(afstand)
        print (distant, 'cm')
        dist = int (distant)
        
        # Dette statement fortaeller at : Hvis "buzz" er True, er "buzz" False
        # Dette bruges til og kunne lave et toggle med knappen til vores buzzer saa man kan "mute" buzzeren
        if digitalRead(button):
            if buzz:
                buzz = False
            else:
                buzz = True
            print (buzz) # Dette viser om knappen er True eller False i Terminalen
    
        if distant > 100 : #Et "if loop" som koerer naar distancen er over 100cm
            digitalWrite (led_blue, 0) #led_blue er sat til og vaere slukket = 0
            digitalWrite (led_red, 0) #led_red er sat til at vaere slukket = 0
            setText ( "Distance = " + str ( dist ) + "\n " + str (buzz)) #Skriver text ud til LCD med afstand og om knappen er True eller False
            time. sleep ( .3 )
        
        elif distant > 40: #Et "if loop" som koerer naar distancen er mellem 40cm og 100cm
            digitalWrite (led_blue, 1) #led_blue er sat til og vaere taendt = 1
            digitalWrite (led_red, 0) #led_red er sat til at vaere slukket = 0
            setText ( "Distance = " + str ( dist ) + "\n " + str (buzz))
            time. sleep ( .3 )
        
        elif distant > 35: #Et "if loop" som koerer naar distancen er mellem 35cm og 40cm
            digitalWrite (led_blue, 0) #led_blue er sat til og vaere slukket = 0
            digitalWrite (led_red, 1) #led_red er sat til og vaere taendt = 1
            if buzz == False: #Et "if loop" som kontrollerer om knappen(buzz) er False(ikke trykket paa)
                digitalWrite (buzzer , 0 ) # Hvis vaerdien ER False vil Buzzeren (buzzer) ikke blive aktiveret (buzzer , 0 )
            else: #Hvis knappen (buzz) IKKE er False vil Buzzeren (buzzer) blive aktiveret (buzzer , 1 )
                digitalWrite (buzzer , 1 )
            setText ( "Distance = " + str ( dist ) + "\n " + str (buzz)) #Skriver text ud til LCD med afstand og om knappen er True eller False
            time. sleep ( .3 ) #Denne "time. sleep" bliver brugt til hvis Buzzeren (buzzer) bliver aktiveret, at den saa holder tonen i 3 sekunder foer den gaar videre
            digitalWrite (buzzer , 0 ) #Dette slukker Buzzeren (buzzer), for derefter og ramme en "time. sleep". Dette faar buzzeren (buzzer) til og taende og slukker med intervallet : 0,3 sekunder taendt. 0,6 sekunder slukket
            time. sleep ( .6 )
        
        elif distant > 30: #Et "if loop" som koerer naar distancen er mellem 30cm og 35cm
            digitalWrite (led_blue, 0) #led_blue er sat til og vaere slukket = 0
            digitalWrite (led_red, 1) #led_red er sat til og vaere taendt = 1
            if buzz == False: #Et "if loop" som kontrollerer om knappen(buzz) er False(ikke trykket paa)
                digitalWrite (buzzer , 0 ) # Hvis vaerdien ER False vil Buzzeren (buzzer) ikke blive aktiveret (buzzer , 0 )
            else: #Hvis knappen (buzz) IKKE er False vil Buzzeren (buzzer) blive aktiveret (buzzer , 1 )
                digitalWrite (buzzer , 1 )
            setText ( "Distance =" + str ( dist ) + "\n " + str (buzz)) #Skriver text ud til LCD med afstand og om knappen er True eller False
            time. sleep ( .25 ) #Denne "time. sleep" bliver brugt til hvis Buzzeren (buzzer) bliver aktiveret, at den saa holder tonen i 0.25 sekunder foer den gaar videre
            digitalWrite (buzzer , 0 ) #Dette slukker Buzzeren (buzzer), for derefter og ramme en "time. sleep". Dette faar buzzeren (buzzer) til og taende og slukker med intervallet : 0,25 sekunder taendt. 0,4 sekunder slukket
            time. sleep ( .4 )
        
        elif distant > 25: #Et "if loop" som koerer naar distancen er mellem 25cm og 30cm
            digitalWrite (led_blue, 0) #led_blue er sat til og vaere slukket = 0
            digitalWrite (led_red, 1) #led_red er sat til og vaere taendt = 1
            if buzz == False: #Et "if loop" som kontrollerer om knappen(buzz) er False(ikke trykket paa)
                digitalWrite (buzzer , 0 ) # Hvis vaerdien ER False vil Buzzeren (buzzer) ikke blive aktiveret (buzzer , 0 )
            else: #Hvis knappen (buzz) IKKE er False vil Buzzeren (buzzer) blive aktiveret (buzzer , 1 )
                digitalWrite (buzzer , 1 )
            setText ( "Distance =" + str ( dist ) + "\n " + str (buzz)) #Skriver text ud til LCD med afstand og om knappen er True eller False
            time. sleep ( .1 ) #Denne "time. sleep" bliver brugt til hvis Buzzeren (buzzer) bliver aktiveret, at den saa holder tonen i 0,1 sekunder foer den gaar videre
            digitalWrite (buzzer , 0 ) #Dette slukker Buzzeren (buzzer), for derefter og ramme en "time. sleep". Dette faar buzzeren (buzzer) til og taende og slukker med intervallet : 0,1 sekunder taendt. 0,2 sekunder slukket
            time. sleep ( .2 )
        
        elif distant > 20: #Et "if loop" som koerer naar distancen er mellem 20cm og 25cm
            digitalWrite (led_blue, 0) #led_blue er sat til og vaere slukket = 0
            digitalWrite (led_red, 1) #led_red er sat til og vaere taendt = 1
            if buzz == False: #Et "if loop" som kontrollerer om knappen(buzz) er False(ikke trykket paa)
                digitalWrite (buzzer , 0 ) # Hvis vaerdien ER False vil Buzzeren (buzzer) ikke blive aktiveret (buzzer , 0 )
            else: #Hvis knappen (buzz) IKKE er False vil Buzzeren (buzzer) blive aktiveret (buzzer , 1 )
                digitalWrite (buzzer , 1 )
            setText ( "Distance =" + str ( dist ) + "\n " + str (buzz)) #Skriver text ud til LCD med afstand og om knappen er True eller False
            time. sleep ( .1 ) #Denne "time. sleep" bliver brugt til hvis Buzzeren (buzzer) bliver aktiveret, at den saa holder tonen i 0,1 sekunder foer den gaar videre
            digitalWrite (buzzer , 0 ) #Dette slukker Buzzeren (buzzer), for derefter og ramme en "time. sleep". Dette faar buzzeren (buzzer) til og taende og slukker med intervallet : 0,1 sekunder taendt. 0,2 sekunder slukket
            time. sleep ( .2 )
            
        elif distant > 15: #Et "if loop" som koerer naar distancen er mellem 15cm og 20cm
            digitalWrite (led_blue, 0) #led_blue er sat til og vaere slukket = 0
            digitalWrite (led_red, 1) #led_red er sat til og vaere taendt = 1
            if buzz == False: #Et "if loop" som kontrollerer om knappen(buzz) er False(ikke trykket paa)
                digitalWrite (buzzer , 0 ) # Hvis vaerdien ER False vil Buzzeren (buzzer) ikke blive aktiveret (buzzer , 0 )
            else: #Hvis knappen (buzz) IKKE er False vil Buzzeren (buzzer) blive aktiveret (buzzer , 1 )
                digitalWrite (buzzer , 1 )
            setText ( "Distance =" + str ( dist ) + "\n " + str (buzz)) #Skriver text ud til LCD med afstand og om knappen er True eller False
            time. sleep ( .05 ) #Denne "time. sleep" bliver brugt til hvis Buzzeren (buzzer) bliver aktiveret, at den saa holder tonen i 0,05 sekunder foer den gaar videre
            
            #Herefter vil baade buzzer og den roede LED slukke. Saa vil vores "if loop" starte forfra og igen taende Buzzeren ( buzzer ) og den roede LED
            digitalWrite (buzzer , 0 )
            digitalWrite (led_red, 0)
        
        elif distant > 10: #Et "if loop" som koerer naar distancen er mellem 10cm og 15cm
            digitalWrite (led_blue, 0) #led_blue er sat til og vaere slukket = 0
            digitalWrite (led_red, 1) #led_red er sat til og vaere taendt = 1
            if buzz == False: #Et "if loop" som kontrollerer om knappen(buzz) er False(ikke trykket paa)
                digitalWrite (buzzer , 0 ) # Hvis vaerdien ER False vil Buzzeren (buzzer) ikke blive aktiveret (buzzer , 0 )
            else: #Hvis knappen (buzz) IKKE er False vil Buzzeren (buzzer) blive aktiveret (buzzer , 1 )
                digitalWrite (buzzer , 1 )
            setText ( "Distance =" + str ( dist ) + "\n " + str (buzz)) #Skriver text ud til LCD med afstand og om knappen er True eller False
            time. sleep ( .005 ) #Denne "time. sleep" bliver brugt til hvis Buzzeren (buzzer) bliver aktiveret, at den saa holder tonen i 0,05 sekunder foer den gaar videre
            
#Herefter vil baade buzzer og den roede LED slukke. Saa vil vores "if loop" starte forfra og igen taende Buzzeren ( buzzer ) og den roede LED
            digitalWrite (buzzer , 0 )
            digitalWrite (led_red, 0)
             
#Hvis ingen af vores "if" eller "elif" statements bliver moedt (distancen er under 10cm) vil dette "else loop" begynde
        else:
            digitalWrite (led_blue, 1) #led_blue er sat til og vaere taendt = 1
            digitalWrite (led_red, 1) #led_red er sat til og vaere taendt = 1
            if buzz == False: #Et "if loop" som kontrollerer om knappen(buzz) er False(ikke trykket paa)
                digitalWrite (buzzer , 0 ) # Hvis vaerdien ER False vil Buzzeren (buzzer) ikke blive aktiveret (buzzer , 0 )
            else: #Hvis knappen (buzz) IKKE er False vil Buzzeren (buzzer) blive aktiveret (buzzer , 1 )
                digitalWrite (buzzer , 1 )
            setText ( "STOP FOR FANDEN!" + "\n " + str (buzz)) #Skriver text ud til LCD med en besked paa foerste linje og om knappen er True eller False paa anden linje
            
#Dette er til og give LCD skaermen sin valgte baggrundsfarve (dette tilfaelde er det hvid)
            setRGB ( 255, 255, 255)
            
# Dette er til hvis man gerne vil have Buzzeren (buzzer) til og bippe istedet for og holde en konstant tone
            #time. sleep ( .0039 )
            #digitalWrite (buzzer , 0 )        
    except TypeError : #Fanger evt. fejl, og skriver en fejlkode "Error" ud til terminalen
        print ("Error")
    except IOError : #Fanger evt. fejl, og skriver en fejlkode "Error" ud til terminalen
        print ("Error")