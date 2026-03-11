const int ledPin = 9;  // LED connected to pin 9

void setup() {
    pinMode(ledPin, OUTPUT);
    Serial.begin(9600);  // Start serial communication
}

void loop() {
    if (Serial.available()) {
        char bit = Serial.read();  

        if (bit == 'S') {  // Start transmission signal
            Serial.println("S");  // Send start signal
        } 
        else if (bit == 'E') {  // End transmission signal
            Serial.println("E");  // Send end signal
        } 
        else if (bit == '1') {
            digitalWrite(ledPin, HIGH);
            delay(250);
        } 
        else if (bit == '0') {
            digitalWrite(ledPin, LOW);
            delay(250);
        }
    }
}




