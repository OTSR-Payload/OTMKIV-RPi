import time
from gpiozero import OutputDevice

led = OutputDevice(21)

for i in range(0, 10):
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
