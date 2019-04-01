# We kunnen ook plaatjes laten zien op de Microbit
# We importeren weer de bibliotheken van de microbit

from microbit import *

# Nu geven we het commando om een plaatje te laten zien.
# Dit doe je met het commando display.show(Image.PLAATJE)

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    if button_b.is_pressed():
        display.show(Image.SAD)

