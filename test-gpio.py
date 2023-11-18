import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIN = 23

GPIO.setup(PIN, GPIO.OUT)

# Initially set the pin to LOW
GPIO.output(PIN, GPIO.LOW)
time.sleep(2)  # Wait 2 seconds

try:
    while True:
        # Explicitly set the pin to HIGH
        GPIO.output(PIN, GPIO.HIGH)
        print("GPIO pin 23 set to HIGH")
        time.sleep(2)

        # Explicitly set the pin to LOW
        GPIO.output(PIN, GPIO.LOW)
        print("GPIO pin 23 set to LOW")
        time.sleep(2)

except KeyboardInterrupt:
    print("Exiting loop.")

finally:
    # Clean up at the end
    GPIO.cleanup()
    print("GPIO cleaned up.")
