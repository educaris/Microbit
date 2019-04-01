from microbit import *
import random
while True:
    if button_a.is_pressed():
        display.scroll("Dobbelsteen")
        
    if accelerometer.was_gesture('shake'):
        display.clear()
        choice = random.randint(0, 5)
        if choice == 0:
            display.show("1")
        elif choice == 1:
            display.show("2")
        elif choice == 2:
            display.show("3")
        elif choice == 3:
            display.show("4")
        elif choice == 4:
            display.show("5")
        elif choice == 5:
            display.show("6")