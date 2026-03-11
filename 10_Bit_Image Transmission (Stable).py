import cv2
import serial
import time
import numpy as np

SERIAL_PORT = "COM5"  # Change this based on your system
BAUD_RATE = 9600

arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)  # Wait for Arduino to initialize
arduino.flush()

def image_to_binary(image_path, threshold=128):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (10, 10), interpolation=cv2.INTER_NEAREST)
    _, binary_img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    binary_array = binary_img // 255  # Convert to 0s and 1s
    return binary_array.flatten()

binary_data = image_to_binary("transmitted.png")

# Print the binary array before transmission
print("Binary Array (Transmitter):")
print(binary_data.reshape(10, 10))

# Send Start Signal
start_sequence = "10101010"  # Ensures Pi detects transition from 1
arduino.write(b'S')
print("Sent: S (Start Signal)")
time.sleep(0.25)

# Send start sequence with index starting from 1
for index, bit in enumerate(start_sequence, start=1):  # Start index from 1
    arduino.write(bit.encode())
    print(f"Sent (Start Sequence) - Index {index}: {bit}")
    time.sleep(0.25)

# Send binary data with index starting from 1
for index, bit in enumerate(binary_data, start=1):  # Start index from 1
    arduino.write(str(bit).encode())  # Send '0' or '1'
    print(f"Sent (Data) - Index {index}: {bit}")  # Display index and bit
    time.sleep(0.25)  # Adjust delay as needed

# Send End Signal
arduino.write(b'E')
print("Sent: E (End Signal)")

arduino.close()
print("Image transmission complete.")

