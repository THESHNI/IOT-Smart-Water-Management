import random
import time

# Simulated water level sensor
def water_level_sensor():
    return random.uniform(0, 100)  # Simulated water level between 0-100%

# Function to send alert if water level is low
def check_water_level():
    water_level = water_level_sensor()
    print(f"Current Water Level: {water_level}%")
    
    if water_level < 20:
        print("ALERT: Water level is low! Consider refilling the tank.")
    elif water_level > 80:
        print("ALERT: Water level is too high! Overflow risk.")
    else:
        print("Water level is within normal range.")

# Main loop to monitor water levels
while True:
    check_water_level()
    time.sleep(5)  # Monitor every 5 seconds

