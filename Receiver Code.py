import RPi.GPIO as GPIO
import time
import numpy as np
import cv2
# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
def receive_binary():
binary_stream = ""
receiving = False
detected_sequence = ""
start_sequence = "10101010" # Start signal pattern
print("Waiting for Start Signal...")
while True:
voltage = GPIO.input(17)
bit = "1" if voltage == 1 else "0"
print(f"Detected bit: {bit}")
if not receiving:
detected_sequence += bit
detected_sequence = detected_sequence[-len(start_sequence):]
print(f"Detected Sequence: {detected_sequence}")
if detected_sequence == start_sequence:
print("Start Sequence Detected! Beginning Image Reception.")
receiving = True
binary_stream = "" # Reset binary stream
continue
if receiving:
binary_stream += bit
print(f"Received bit: {bit}")
time.sleep(0.5)
if receiving and len(binary_stream) >= 100: # For a 10x10 image
print("Image reception complete.")
break
return binary_stream
def binary_to_image(binary_string, output_path="received_image.png"):
binary_array = np.array([int(bit) for bit in binary_string], dtype=np.uint8).reshape((print("Binary Array (Receiver):")
print(binary_array)
grayscale_image = binary_array * 255
cv2.imwrite(output_path, grayscale_image)
print(f"Received image saved as {output_path}")
binary_data = receive_binary()
binary_to_image(binary_data)
GPIO.cleanup()
