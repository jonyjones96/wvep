# This code allows the following:
# - Sending signals from one microbit to another
# - If one of the microbits is connected to two servo motors, the other microbit will allow you to control it

# Add your Python code here. E.g.
# A micro:bit Firefly.
# By Nicholas H.Tollervey. Released to the public domain.
import radio
import random
from microbit import *

display.show(Image.ASLEEP)
# The radio won't work unless it's switched on.
radio.on()
pin1.set_analog_period(20)
pin2.set_analog_period(20)

# Event loop.
while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(Image.HEART)
        radio.send('0')
    elif button_b.is_pressed():
        display.show(Image.HAPPY)
        radio.send('1')
    elif button_b.was_pressed():
        display.show(Image.ANGRY)
        radio.send('2')
    elif button_a.is_pressed():
        display.show(Image.SMILE)
        radio.send('3')
    elif button_a.was_pressed():
        display.show(Image.SAD)
        radio.send('4')
    elif (button_b.was_pressed() and button_a.was_pressed()):
        display.show(Image.SILLY)
        radio.send('5')
        
    # Read any incoming messages.
    incoming = radio.receive()
    if incoming == '0':
        display.show(Image.HEART)
        pin1.write_analog(90)
        pin2.write_analog(180)
    elif incoming == '1':
        display.show(Image.HAPPY)
        pin2.write_analog(180)
    elif incoming == '2':
        display.show(Image.ANGRY)
        pin2.write_analog(0)
    elif incoming == '3':
        display.show(Image.SMILE) 
        pin1.write_analog(90)
    elif incoming == '4':
        display.show(Image.SAD)
        pin1.write_analog(0)
    elif incoming == '5':
        display.show(Image.SILLY)
        pin1.write_analog(0)
        pin2.write_analog(0)
    sleep(100)
