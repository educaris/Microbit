# Nu gaan we zelf plaatjes maken. Uiteraard beginnen we bij het begin:

from microbit import *

# Nu maken we zelf een plaatje. Er zijn verschillende opties voor de
# LEDS. Je kunt de helderheid zelf aanpassen. 0 is uit. 9 is fel.
# Je maakt eerste je plaatje. Daarna roep je je plaatje op.
# een voorbeeld. Ik teken eerst een plaatje: 

plaatje = Image("01234:"
                "12345:"
                "23456:"
                "34567:"
                "45678:")

# Nu roep ik het plaatje op met display.show:

display.show(plaatje)