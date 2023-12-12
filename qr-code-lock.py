from flask import Flask, render_template, request, redirect, url_for, make_response
import RPi.GPIO as GPIO
import time
from rpi_ws281x import PixelStrip, Color

# LED strip configuration
LED_COUNT = 30         # Number of LED pixels
LED_PIN = 21           # GPIO pin connected to the pixels
LED_FREQ_HZ = 800000   # LED signal frequency in hertz
LED_DMA = 10           # DMA channel to use for generating signal
LED_BRIGHTNESS = 255   # Set brightness (0 to 255)
LED_INVERT = False     # True to invert the signal

# Create PixelStrip object
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()

# Function to control the light strip
def colorWipe(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

# Function to pulse blue light
def pulseBlue(strip, wait_ms=500, iterations=10):
    for j in range(iterations):
        # Fade in
        for i in range(0, 256, 5):
            colorWipe(strip, Color(0, 0, i), wait_ms)
        # Fade out
        for i in range(255, 0, -5):
            colorWipe(strip, Color(0, 0, i), wait_ms)

# Door lock setup
GPIO.setmode(GPIO.BCM)
PIN = 23
GPIO.setup(PIN, GPIO.OUT)
GPIO.output(PIN, GPIO.HIGH)

# Set up Flask server
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<changepin>', methods=['POST'])
def reroute(changepin):
    changePin = int(changepin)
    if changePin == 1:
        print("UNLOCK")
        GPIO.output(PIN, GPIO.LOW)
        pulseBlue(strip)  # Pulse blue when unlocked
    elif changePin == 2:
        print("LOCK")
        GPIO.output(PIN, GPIO.HIGH)
        colorWipe(strip, Color(255, 0, 0), 10)  # Turn red when locked
    response = make_response(redirect(url_for('index')))
    return response

@app.route('/trigger-relay')
def trigger_relay():
    print("UNLOCK")
    GPIO.output(PIN, GPIO.LOW)
    pulseBlue(strip)  # Pulse blue
    time.sleep(5)
    print("LOCK")
    GPIO.output(PIN, GPIO.HIGH)
    colorWipe(strip, Color(255, 0, 0), 10)  # Turn red
    return "Relay triggered for 5 seconds"

try:
    app.run(debug=True, host='0.0.0.0', port=8000)

except KeyboardInterrupt:
    colorWipe(strip, Color(0, 0, 0), 10)
    GPIO.cleanup()
    print("Server and LED strip turned off.")