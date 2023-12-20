import serial

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=10)

while True:
    servo_pos_str = input("Enter servo position (0-180): ")
    servo_pos = int(servo_pos_str)
    arduino.write("WRITE_ANGLE".encode())
    foo = arduino.read(len("WRITE_ANGLE"))
    print(foo)
    # arduino.write(servo_pos.to_bytes(1, 'big', signed=False))
