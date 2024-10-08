pip install pyserial

import tkinter as tk
from tkinter import ttk
import serial
import time

# Establish serial connection with Arduino (adjust the port to match your system)
ser = serial.Serial('COM3', 9600)  # Use the correct port where Arduino is connected (e.g., 'COM3', '/dev/ttyUSB0')

# Function to read data from Arduino
def read_arduino_data():
    if ser.in_waiting > 0:  # Check if there is data in the serial buffer
        try:
            # Read a line from the serial input and decode it to a string
            arduino_data = ser.readline().decode('utf-8').strip()
            
            # Split the potentiometer value and voltage from the Arduino output
            voltage = float(arduino_data)
            pot_value = round((voltage * 1023) / 5)
            
            # Update the GUI with the new values
            pot_label.config(text=f"Potentiometer Value: {pot_value}")
            voltage_label.config(text=f"Voltage: {voltage:.2f} V")
        except Exception as e:
            print(f"Error: {e}")
    
    # Schedule the function to be called after 100ms
    root.after(100, read_arduino_data)

# Initialize Tkinter window
root = tk.Tk()
root.title("Arduino Potentiometer and Voltage Reader")
root.geometry("300x200")

# Create and place labels for displaying potentiometer value and voltage
pot_label = ttk.Label(root, text="Potentiometer Value: 0", font=("Arial", 14))
pot_label.pack(pady=20)

voltage_label = ttk.Label(root, text="Voltage: 0.00 V", font=("Arial", 14))
voltage_label.pack(pady=20)

# Call the function to read Arduino data
root.after(100, read_arduino_data)

# Start the GUI loop
root.mainloop()
