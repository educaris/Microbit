# We gaan eens lol maken met de GPIO pins. Er zitten er 3
# op de microbit: 0, 1 en 2. We gebruiken onszelf als geleider!

from microbit import *

while True:
    if pin0.is_touched():
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)

# Als het goed is zie je nu een sip gezicht. Laten we hem eens
# aan het lachen maken. Raak met je ene hand de GND aan en 
# en met je andere pin0. Als het goed is gaat je Microbit
# nu lachen!

# Kun je aangeven hoe dit werkt?