import time
import board
import adafruit_bmp3xx
import digitalio
import csv

# set up pins for communicationo
spi = board.SPI()
print(spi)
cs = digitalio.DigitalInOut(board.D18)
print(cs)

# set up BMP
bmp = adafruit_bmp3xx.BMP3XX_SPI(spi, cs)

print("Starting live readings...\n")

start = time.time()
 
file = open("bmp_results.csv", "w", newline="")
writer = csv.writer(file)

# Write header
writer.writerow(["pressure", "temp"])

while time.time() - start < 500:
    pressure = bmp.pressure
    temp = bmp.temperature

    print("Pressure:", pressure, "Temperature:", temp)

    writer.writerow([pressure, temp])
    file.flush()          # ensures data is written immediately

    time.sleep(1)

file.close()
	
print("Done!")




#print("Pressure: {:6.1f}".format(bmp.pressure))
#print("Temperature: {:5.2}".format(bmp.temperature))
