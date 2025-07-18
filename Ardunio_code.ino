#include <Wire.h>

#define ADXL345_ADDRESS 0x53  // I2C address for ADXL345

void setup() {
  Serial.begin(9600);
  Wire.begin();

  // Set ADXL345 to measurement mode
  Wire.beginTransmission(ADXL345_ADDRESS);
  Wire.write(0x2D);  // POWER_CTL register
  Wire.write(0x08);  // Set measurement mode
  Wire.endTransmission();

  // Set range to ±2g (optional, default)
  Wire.beginTransmission(ADXL345_ADDRESS);
  Wire.write(0x31);  // DATA_FORMAT register
  Wire.write(0x00);  // ±2g range
  Wire.endTransmission();

  delay(500);
  Serial.println("ADXL345 Initialized");
}

void loop() {
  int16_t x, y, z;

  // Read 6 bytes starting from data register 0x32
  Wire.beginTransmission(ADXL345_ADDRESS);
  Wire.write(0x32);
  Wire.endTransmission(false);
  Wire.requestFrom(ADXL345_ADDRESS, 6);

  if (Wire.available() == 6) {
    x = Wire.read() | (Wire.read() << 8);
    y = Wire.read() | (Wire.read() << 8);
    z = Wire.read() | (Wire.read() << 8);

    // Convert raw values to g
    float gX = x * 0.0039;
    float gY = y * 0.0039;
    float gZ = z * 0.0039;

    // Compute vibration magnitude (remove constant gravity)
    float vibration = sqrt(gX * gX + gY * gY + gZ * gZ) - 1.0;
    vibration = abs(vibration);  // Keep it positive

    // ✅ Serial Plotter format: label1:value1 label2:value2 ...
    Serial.print("X:"); Serial.print(gX, 4);
    Serial.print(" Y:"); Serial.print(gY, 4);
    Serial.print(" Z:"); Serial.print(gZ, 4);
    Serial.print(" Vibration:"); Serial.println(vibration, 4);
  }

  delay(20);  // Fast sampling for better resolution
}
