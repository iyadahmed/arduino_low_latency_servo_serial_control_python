import serial
from PySide6.QtWidgets import QApplication, QSlider

SERVO_WRITE_ANGLE_COMMAND = b"WRITE_ANGLE"
SERIAL_TIMEOUT_SECONDS = 10
SERIAL_BAUDRATE = 9600
SERIAL_PORT = 'COM3'  # Update this to the port your Arduino is connected to
GUI = True

arduino = serial.Serial(port=SERIAL_PORT, baudrate=SERIAL_BAUDRATE, timeout=SERIAL_TIMEOUT_SECONDS)


def send_servo_write_angle_command(angle: int):
    if angle < 0 or angle > 180:
        print("Servo position out of range (0-180), not sending command")
    else:
        arduino.write(SERVO_WRITE_ANGLE_COMMAND + bytes([angle]))


def gui():
    app = QApplication()
    dial = QSlider()
    dial.setRange(0, 180)
    dial.valueChanged.connect(lambda angle: send_servo_write_angle_command(angle))
    dial.show()
    app.exec()


def cli():
    while True:
        servo_pos_str = input("Enter servo position (0-180): ")
        send_servo_write_angle_command(int(servo_pos_str))


def main():
    if GUI:
        gui()
    else:
        cli()


if __name__ == "__main__":
    main()
