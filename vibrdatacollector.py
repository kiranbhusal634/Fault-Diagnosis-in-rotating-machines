import serial
import csv
import time

# Configuration
PORT = 'COM3'         # ⚠️ Change this to match your Arduino port
BAUD_RATE = 9600
DURATION = 30         # Duration to collect data (in seconds)
CSV_FILE = 'vibration_data_normal_moter.csv'

# Connect to Arduino
try:
    ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
    print(f"Connected to {PORT} at {BAUD_RATE} baud.")
    time.sleep(2)  # Give time for Arduino to reset
except Exception as e:
    print(f"Error: {e}")
    exit()

# Prepare CSV file
with open(CSV_FILE, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Timestamp', 'X', 'Y', 'Z', 'Vibration'])

    print("Collecting data...")

    start_time = time.time()
    while time.time() - start_time < DURATION:
        try:
            line = ser.readline().decode('utf-8').strip()
            if line.startswith("X:"):
                # Example: X:-1.5756 Y:1.9929 Z:0.0429 Vibration:1.5409
                parts = line.split()
                x = float(parts[0].split(":")[1])
                y = float(parts[1].split(":")[1])
                z = float(parts[2].split(":")[1])
                vibration = float(parts[3].split(":")[1])
                timestamp = time.strftime('%H:%M:%S')
                writer.writerow([timestamp, x, y, z, vibration])
                print(f"[{timestamp}] X={x}, Y={y}, Z={z}, V={vibration}")
        except Exception as e:
            print(f"Error reading line: {e}")

ser.close()
print(f"\n✅ Data collection finished. File saved as: {CSV_FILE}")
