#include <Servo.h>

#define SERVO_PIN 9
#define SERVO_INIT_POS 0
#define SERIAL_BAUD_RATE 9600
#define SERVO_WRITE_ANGLE_COMMAND "WRITE_ANGLE"
#define SERVO_DELAY_MS 15

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
  if (Serial.available() >= (STRLEN(SERVO_WRITE_ANGLE_COMMAND) + 1)) {
    isWriteAngleCommandFound = Serial.find(SERVO_WRITE_ANGLE_COMMAND, STRLEN(SERVO_WRITE_ANGLE_COMMAND));
    if (isWriteAngleCommandFound) {
      servoPos = Serial.read(); // We do not need to handle timeout, if we already check that enough bytes are available via Serial.available()
      servo.write(servoPos);
      delay(SERVO_DELAY_MS);
    }
  }
}
