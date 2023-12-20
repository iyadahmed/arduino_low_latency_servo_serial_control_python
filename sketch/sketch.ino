#include <Servo.h>

#define SERVO_PIN 9
#define SERVO_INIT_POS 0
#define SERIAL_BAUD_RATE 9600
#define SERVO_WRITE_ANGLE_COMMAND "WRITE_ANGLE"

#define STRLEN(str) (sizeof(str) - 1)

bool isWriteAngleCommandFound = false;
uint8_t servoPos = 0;
Servo servo;

void setup() {
  servo.attach(SERVO_PIN);
  servo.write(SERVO_INIT_POS);
  Serial.begin(SERIAL_BAUD_RATE);
  while (!Serial) {
    ;  // wait for serial port to connect. Needed for native USB port only
  }
}

void loop() {
  if (Serial.available() >= 4) {
    // isWriteAngleCommandFound = true;
    isWriteAngleCommandFound = Serial.find("FOO", 3);
    if (isWriteAngleCommandFound) {
      char b[4] = { 'a', 'b', 'c', 0 };
      Serial.readBytes(b, 3);
      b[3] = 0;
      Serial.print(b);
      // servoPos = Serial.read();
      // servo.write(servoPos);
      // delay(15);
    }
  }
}
