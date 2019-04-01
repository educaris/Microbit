# Nog meer lol! Laten we eens een lampje laten knipperen.
# Sluit een draadje aan op de GND en een tweede draadje op 
# pin0, Daartussen een lampje. De lange poot gaat aan de pin0
# De korte poot gaat aan het draadje van de GND. 

from microbit import *

while True:
    pin0.write_digital(1)
    sleep(1000)
    pin0.write_digital(0)
    sleep(1000)
    
# pin0.write_digital is het commando om pin0 aan te zetten.
# 1 = aan
# 0 = uit
# sleep is een wacht commando (in milliseconden)