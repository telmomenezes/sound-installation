int incomingByte;

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 16; i++) {
    pinMode(i, OUTPUT);
    digitalWrite(i, LOW);
  }
}

void selectSpeaker(int x) {
  for (int i = 0; i < 16; i++) {
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
      selectSpeaker(0);
    }
    if (incomingByte == 'B') {
      selectSpeaker(1);
    }
    if (incomingByte == 'C') {
      selectSpeaker(2);
    }
    if (incomingByte == 'D') {
      selectSpeaker(3);
    }
    if (incomingByte == 'E') {
      selectSpeaker(4);
    }
    if (incomingByte == 'F') {
      selectSpeaker(5);
    }
    if (incomingByte == 'G') {
      selectSpeaker(6);
    }
    if (incomingByte == 'H') {
      selectSpeaker(7);
    }
    if (incomingByte == 'I') {
      selectSpeaker(8);
    }
    if (incomingByte == 'J') {
      selectSpeaker(9);
    }
    if (incomingByte == 'K') {
      selectSpeaker(10);
    }
    if (incomingByte == 'L') {
      selectSpeaker(11);
    }
    if (incomingByte == 'M') {
      selectSpeaker(12);
    }
    if (incomingByte == 'N') {
      selectSpeaker(13);
    }
    if (incomingByte == 'O') {
      selectSpeaker(14);
    }
    if (incomingByte == 'P') {
      selectSpeaker(15);
    }
  }
}
