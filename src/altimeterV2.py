import time
import board
import adafruit_bmp3xx
import digitalio
import csv
import matplotlib.pyplot as plt

# set up pins for communication
spi = board.SPI()
print(spi)

cs = digitalio.DigitalInOut(board.D18)
print(cs)

# set up BMP
bmp = adafruit_bmp3xx.BMP3XX_SPI(spi, cs)

print("Starting live readings...\n")

start = time.time()

# Lists for graphing
times = []
pressures = []
temperatures = []

file = open("bmp_results.csv", "w", newline="")
writer = csv.writer(file)

# Write header
writer.writerow(["time", "pressure", "temp"])

while time.time() - start < 10:   # Change this number to change total run time

    pressure = bmp.pressure
    temp = bmp.temperature
    elapsed = time.time() - start

    print("Pressure:", pressure, "Temperature:", temp)

    # Save data for graph
    times.append(elapsed)
    pressures.append(pressure)
    temperatures.append(temp)

    # Save data to CSV
    writer.writerow([elapsed, pressure, temp])
    file.flush()

    time.sleep(1)   # Change this number to change reading frequency

file.close()

print("Done!")

# -------- Create Graph --------

fig, ax1 = plt.subplots(figsize=(10, 5))

# Pressure graph
ax1.plot(times, pressures, color="blue", label="Pressure")
ax1.set_xlabel("Time (seconds)")
ax1.set_ylabel("Pressure (hPa)", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")

# Temperature graph (second axis)
ax2 = ax1.twinx()
ax2.plot(times, temperatures, color="red", label="Temperature")
ax2.set_ylabel("Temperature (°C)", color="red")
ax2.tick_params(axis="y", labelcolor="red")

plt.title("BMP390 Pressure and Temperature Readings")
plt.grid(True)

plt.tight_layout()
plt.show()
