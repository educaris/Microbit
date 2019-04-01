# Write your code here :
from microbit import *

# er zitten 25 lampjes op de microbit
# vijf op de x-as
# vijf op de y-as
# de lampjes moeten afzonderlijk aangezet worden met een bepaalde sterkte
# we gebruiken hiervoor een for loop:
# elke keer gaan we een rijtje af:

# We maken gebruik van een zogenaamde for loop, hier staat eigenlijk:
# We hebben de variabele x en elke keer telt hij er eentje bij
# totdat x vijf wordt, dan houd ik op.
for x in range(5):
    # Met display.set_pixel kan je pixels aanzetten op een x / y coordinaat
    # De drie waardes die je kan invoeren zijn: x coordinaat, y coordinaat en helderheid (van 0 tot 9)
    display.set_pixel(x, 1, 9)
    sleep(1000) # We wachten een seconde voordat we doorgaan in het loopje

sleep(5000);
# Wat je merkt is dat elke seconde een lampje opschuift.
# Wat je ook merkt is dat niet de eerste rij lampjes maar de tweede rij lampjes aangaat
# Dit komt omdat je op computers altijd vanaf 0 tellen

display.clear();
sleep(5000);
# Deze for loop kunnen we nu kopieren en plakken en ook toepassen op de y waarde.
# Met twee for loops kunnen we dan alle lampjes aanzetten!
for x in range(5):
    for y in range(5):
        # Met display.set_pixel kan je pixels aanzetten op een x / y coordinaat
        # De drie waardes die je kan invoeren zijn: x coordinaat, y coordinaat en helderheid (van 0 tot 9)
        display.set_pixel(x, y, 9)
        sleep(1000) # We wachten een seconde voordat we doorgaan in het loopje


display.clear()
sleep(10000)
# En als je het echt goed doet... ;-)

c = -9  # De animatie kent 27 stappen. van -9 tot 17

while True:
    for x in range(5):
        for y in range(5):
            b = x+y +c
            if b > 9:
                b = 18 - b
            if b < 0:
                b = 0
            display.set_pixel(x, y, b)
    sleep(100)
    c = c + 1
    if c > 17:
        c = -9
