from gpiozero import LED, Button
from signal import pause

led = LED(27) #PIN 13 GPIO 27
button = Button(22, pull_up=False) #PIN15 GPIO 22

button.when_pressed = led.on
button.when_released = led.off

pause()