import serial

SERVO_WRITE_ANGLE_COMMAND = b"WRITE_ANGLE"
SERIAL_TIMEOUT_SECONDS = 10
SERIAL_BAUDRATE = 9600
SERIAL_PORT = 'COM3'  # Update this to the port your Arduino is connected to

arduino = serial.Serial(port=SERIAL_PORT, baudrate=SERIAL_BAUDRATE, timeout=SERIAL_TIMEOUT_SECONDS)

while True:
    servo_pos_str = input("Enter servo position (0-180): ")
    servo_pos = int(servo_pos_str)
    if servo_pos < 0 or servo_pos > 180:
        print("Invalid servo position")
        continue
    arduino.write(SERVO_WRITE_ANGLE_COMMAND)
    arduino.write(servo_pos.to_bytes(1, 'big', signed=False))
