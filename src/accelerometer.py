import time
import spidev

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 100000
spi.mode = 3

device_id = spi.xfer2([0x80, 0x00])[1]
print("Device ID:", hex(device_id))

if device_id != 0xE5:
    print("ADXL345 not detected")
    spi.close()
    raise SystemExit

# Set data format to full resolution, ±2g
spi.xfer2([0x31, 0x08])

# Set power control to measurement mode
spi.xfer2([0x2D, 0x08])

start_time = time.time()

while time.time() - start_time < 30:

    # Read 6 bytes starting at DATAX0 (0x32)
    data = spi.xfer2([0xF2, 0, 0, 0, 0, 0, 0])

    x = (data[2] << 8) | data[1]
    y = (data[4] << 8) | data[3]
    z = (data[6] << 8) | data[5]

    if x > 32767:
        x -= 65536
    if y > 32767:
        y -= 65536
    if z > 32767:
        z -= 65536

    print("X:", x, "Y:", y, "Z:", z)

    time.sleep(0.5)

spi.close()
print("Finished")
