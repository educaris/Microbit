from microbit import *

boot1 = Image("05050:"
              "05050:"              #Dit is een programma voor een zinkende boot. Er zijn 5 plaatjes
              "05050:"              # gemaakt (boot1 t/m boot5). Als laatste roepen we alle plaatjes op.
              "99999:"
              "09990")

boot2 = Image("00000:"
              "05050:"
              "05050:"
              "05050:"
              "99999")

boot3 = Image("00000:"
              "00000:"
              "05050:"
              "05050:"
              "05050")

boot4 = Image("00000:"
              "00000:"
              "00000:"
              "05050:"
              "05050")

boot5 = Image("00000:"
              "00000:"                              # Hier roepen we dus alle plaatjes op. Eerst maken we 
              "00000:"                              # een variabele voor alle plaatjes. Daarna roepen we 
              "00000:"                              # die variabele op. De delay is zodat de plaatjes niet 
              "05050")                              # te snel gaan.

alle_boten = [boot1, boot2, boot3, boot4, boot5]    # Kun je er voor zorgen dat de boot pas gaat zinken als
display.show(alle_boten, delay=200)                 # we de knop indrukken?