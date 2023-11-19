from flask import Flask, render_template, request, redirect, url_for, make_response
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
PIN = 23
GPIO.setup(PIN, GPIO.OUT)
GPIO.output(PIN, GPIO.HIGH)

app = Flask(__name__)  # Set up Flask server

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<changepin>', methods=['POST'])
def reroute(changepin):
    changePin = int(changepin)  # Cast changepin to an int
    if changePin == 1:
        print("UNLOCK")
        GPIO.output(PIN, GPIO.LOW)              
    elif changePin == 2:
        print("LOCK")
        GPIO.output(PIN, GPIO.HIGH)
    response = make_response(redirect(url_for('index')))
    return response

@app.route('/trigger-relay')
def trigger_relay():
    print("UNLOCK")
    GPIO.output(PIN, GPIO.LOW)   
    time.sleep(5)  # Wait for 5 seconds
    print("LOCK")
    GPIO.output(PIN, GPIO.HIGH)
    return "Relay triggered for 5 seconds"

app.run(debug=True, host='10.0.0.16', port=8000)  # Set up the server
