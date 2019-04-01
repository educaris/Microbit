# Welkom bij het eerste programma. Bij dit programma leer je een tekst
# te scrollen.

# Eerst importeren we de microbit bibliotheek. Op die manier kunnen we
# stukjes code van andere mensen gebruiken.

from microbit import *

# Nu maken we een ALS (oftewel IF in het Engels) statement
# Dit if-statement doet iets als we knop (button) a indrukken:
# while True geeft aan dat het if-statement gaat werken als wat er onder
# staat "waar" is. Dus als het waar is dat de knop is ingedrukt
# display.scroll is het commando om tekst over het display te laten
# lopen. De tekst die je wilt scrollen staat er achter tussen " " 

while True:
    if button_a.is_pressed():
        display.scroll("Hallo")
        