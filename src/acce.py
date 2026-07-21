import time 
import spidev

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 100000
spi.mode = 3


for _ in range(100):
	result = spi.xfer2([0x80, 0x00])
	print(result, (result[1]))
	time.sleep(0.5)
	
spi.close()
