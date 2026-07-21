#!/usr/bin/env python3

import smbus2
import time
import struct

# Registers
ADXL345 = 0x53
ADXL375 = 0x00
BMP390 = 0x00
