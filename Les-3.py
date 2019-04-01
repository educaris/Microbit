# Nu een dobbelsteen maken. Het begin weet je ondertussen wel. We hebben
# alleen een extra bibliotheek nodig: random, oftewel willekeurig

from microbit import *
import random

while True:   
    if button_a.is_pressed():
        display.clear()
        keuze = random.randint(0, 5)   #Dit is waar random plaats vindt. 
        if keuze == 0:                 #We maken een variabele "keuze" en 
            display.show("1")          #stoppen daar een willekeurig getal in  
        elif keuze == 1:               #Let op! Het eerste getal in een reeks
            display.show("2")          #met programmeren is 0 
        elif keuze == 2:
            display.show("3")
        elif keuze == 3:
            display.show("4")
        elif keuze == 4:
            display.show("5")
        elif keuze == 5:
            display.show("6")