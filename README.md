Low Latency Servo Control via Serial

### Circuit:  
* Arduino Nano
* SG90 Servo Motor (Connected to pin 9)

### How to run:  
1. Upload the sketch to the Arduino
2. Install dependencies: `pip install --user pyserial pyside6`
3. Run the script: `python arduino_low_latency_servo_serial_control.py`

### Output:  
`Enter servo position (0-180):`  
an infinite loop with the above message, entering an angle moves the servo accordingly

### Video:
CLI (set the "GUI" constant in the script to False)

https://github.com/iyadahmed/arduino_low_latency_servo_serial_control_python/assets/25552173/ddbada33-213b-4f00-947c-6a2e97e7058d

GUI

https://github.com/iyadahmed/arduino_low_latency_servo_serial_control_python/assets/25552173/f5428dc2-210b-46af-8dda-88187c0cbeb4

