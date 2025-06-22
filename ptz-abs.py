import serial

def calculate_checksum(address, command1, command2, data1, data2):
    return (address + command1 + command2 + data1 + data2) % 256

def send_pelco_d_command(serial_port, address, command1, command2, data1, data2):
    checksum = calculate_checksum(address, command1, command2, data1, data2)
    command = bytes([0xFF, address, command1, command2, data1, data2, checksum])
    serial_port.write(command)
    print(f"Sent: {[hex(b) for b in command]}")

def send_absolute_pan(serial_port, address, pan_value):
    # Clamp and convert pan_value (0-36000)
    pan_value = max(0, min(36000, pan_value))
    dataH = (pan_value >> 8) & 0xFF
    dataL = pan_value & 0xFF
    send_pelco_d_command(serial_port, address, 0x00, 0x4B, dataH, dataL)

def send_absolute_tilt(serial_port, address, tilt_value):
    # Clamp and convert tilt_value (0-9000)
    tilt_value = max(0, min(9000, tilt_value))
    dataH = (tilt_value >> 8) & 0xFF
    dataL = tilt_value & 0xFF
    send_pelco_d_command(serial_port, address, 0x00, 0x4D, dataH, dataL)

# Example usage
if __name__ == "__main__":
    # Open serial port (adjust 'COM3' or '/dev/ttyUSB0' and settings as needed)
    ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=1)

    camera_address = 0x01  # Replace with your camera's actual address

    # Example: Pan to 180 degrees (18000), Tilt to 45 degrees (4500)
    send_absolute_pan(ser, camera_address, 36000)
    send_absolute_tilt(ser, camera_address, 5005)

    ser.close()
