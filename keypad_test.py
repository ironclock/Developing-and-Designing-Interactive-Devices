# # Make sure to have everything set up
# # https://github.com/sparkfun/Qwiic_Keypad_Py 
# # `pip install sparkfun-qwiic-keypad`

# # From https://github.com/sparkfun/Qwiic_Keypad_Py/blob/main/examples/qwiic_keypad_ex2.py


# from __future__ import print_function
# import qwiic_keypad
# import time
# import sys

# def runExample():

# 	print("\nSparkFun qwiic Keypad   Example 1\n")
# 	myKeypad = qwiic_keypad.QwiicKeypad()

# 	if myKeypad.connected == False:
# 		print("The Qwiic Keypad device isn't connected to the system. Please check your connection", \
# 			file=sys.stderr)
# 		return

# 	myKeypad.begin()

# 	print("Initialized. Firmware Version: %s" % myKeypad.version)
# 	print("Press a button: * to do a space. # to go to next line.")

# 	button = 0
# 	while True:

# 		# necessary for keypad to pull button from stack to readable register
# 		myKeypad.update_fifo()  
# 		button = myKeypad.get_button()

# 		if button == -1:
# 			print("No keypad detected")
# 			time.sleep(1)

# 		elif button != 0:

# 			# Get the character version of this char
# 			charButton = chr(button)
# 			if charButton == '#':
# 				print()
# 			elif charButton == '*':
# 				print(" ", end="")
# 			else: 
# 				print(charButton, end="")

# 			# Flush the stdout buffer to give immediate user feedback
# 			sys.stdout.flush()

# 		time.sleep(.25)

# if __name__ == '__main__':
# 	try:
# 		runExample()
# 	except (KeyboardInterrupt, SystemExit) as exErr:
# 		print("\nEnding Example 1")
# 		sys.exit(0)

import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
from adafruit_rgb_display import ili9341
import qwiic_keypad
import time
import sys

# Screen setup
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D27)
BAUDRATE = 24000000
spi = board.SPI()
disp = ili9341.ILI9341(
    spi, cs=cs_pin, dc=dc_pin, rst=reset_pin, baudrate=BAUDRATE, width=240, height=320
)

# Keypad setup
print("\nSparkFun qwiic Keypad Example\n")
myKeypad = qwiic_keypad.QwiicKeypad()
if myKeypad.connected == False:
    print("The Qwiic Keypad device isn't connected to the system. Please check your connection", file=sys.stderr)
    sys.exit(1)
myKeypad.begin()
print("Initialized. Firmware Version: %s" % myKeypad.version)

# Function to update the screen
def update_screen(display, text):
    width, height = display.width, display.height
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.text((0, 0), text, font=font, fill="#FFFFFF")
    display.image(image)

# Main loop
text = ""
while True:
    myKeypad.update_fifo()
    button = myKeypad.get_button()

    if button == -1:
        print("No keypad detected")
        time.sleep(1)

    elif button != 0:
        charButton = chr(button)
        if charButton == '#':
            text += '\n'
        elif charButton == '*':
            text += ' '
        else: 
            text += charButton

        update_screen(disp, text)

    time.sleep(.25)

