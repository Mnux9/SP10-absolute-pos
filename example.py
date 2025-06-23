from pelcoSP10 import pelcoSP10

ser, address = pelcoSP10.connect("/dev/ttyUSB0", 9600, 0x01)
pelcoSP10.send_absolute_pan(ser, address, 12000)
pelcoSP10.send_absolute_tilt(ser, address, 1022)
