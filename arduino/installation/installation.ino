int incomingByte;

void setup() {
  Serial.begin(9600);
  for (int i = 2; i <= 17; i++) {
    pinMode(i, OUTPUT);
    digitalWrite(i, LOW);
  }
}

void selectSpeaker(int x) {
  for (int i = 2; i <= 17; i++) {
    if (i == x) {
      digitalWrite(i, HIGH);
    }
    else {
      digitalWrite(i, LOW);
    }
  }
}

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    if (incomingByte == 'A') {
      selectSpeaker(17);
    }
    if (incomingByte == 'B') {
      selectSpeaker(2);
    }
    if (incomingByte == 'C') {
      selectSpeaker(3);
    }
    if (incomingByte == 'D') {
      selectSpeaker(4);
    }
    if (incomingByte == 'E') {
      selectSpeaker(5);
    }
    if (incomingByte == 'F') {
      selectSpeaker(6);
    }
    if (incomingByte == 'G') {
      selectSpeaker(7);
    }
    if (incomingByte == 'H') {
      selectSpeaker(8);
    }
    if (incomingByte == 'I') {
      selectSpeaker(9);
    }
    if (incomingByte == 'J') {
      selectSpeaker(10);
    }
    if (incomingByte == 'K') {
      selectSpeaker(11);
    }
    if (incomingByte == 'L') {
      selectSpeaker(12);
    }
    if (incomingByte == 'M') {
      selectSpeaker(13);
    }
    if (incomingByte == 'N') {
      selectSpeaker(14);
    }
    if (incomingByte == 'O') {
      selectSpeaker(15);
    }
    if (incomingByte == 'P') {
      selectSpeaker(16);
    }
  }
}
