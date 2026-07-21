#!/usr/bin/env python3

import smbus2
import time
import struct

# Registers
DEVICE = 0x53

POWER_CTL = 0x2D
DATA_FORMAT = 0x31
BW_RATE = 0x2C
DATAX0 = 0x32

bus = smbus2.SMBus(1)

def initialize():
    # 100 Hz output data rate
    bus.write_byte_data(DEVICE, BW_RATE, 0x0A)

    # Full resolution, ±2g
    bus.write_byte_data(DEVICE, DATA_FORMAT, 0x08)

    # Measurement mode
    bus.write_byte_data(DEVICE, POWER_CTL, 0x08)


def read_xyz():
    data = bus.read_i2c_block_data(DEVICE, DATAX0, 6)

    x, y, z = struct.unpack('<hhh', bytes(data))

    # Full resolution scale factor
    scale = 0.0039
    #  good shit
    xg = x * scale
    yg = y * scale
    zg = z * scale

    return xg, yg, zg


initialize()

print("Reading ADXL345...")

try:
    while True:
        x, y, z = read_xyz()

        print(f"X = {x:7.3f} g   "
              f"Y = {y:7.3f} g   "
              f"Z = {z:7.3f} g")

        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nFinished.")
