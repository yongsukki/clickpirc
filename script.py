# Imports
import webiopi
import time

# Enable debug output
webiopi.setDebug()

# Retrieve GPIO lib
GPIO = webiopi.GPIO

# Two LB1630
IC1A = 24
IC1B = 25
IC2A = 8
IC2B = 7

# Called by WebIOPi at script loading
def setup():
    webiopi.debug("Script with macros - Setup")
    # Setup GPIOs
    GPIO.setFunction(IC1A, GPIO.OUT)
    GPIO.setFunction(IC1B, GPIO.OUT)
    GPIO.setFunction(IC2A, GPIO.OUT)
    GPIO.setFunction(IC2B, GPIO.OUT)

    GPIO.digitalWrite(IC1A, GPIO.LOW)
    GPIO.digitalWrite(IC1B, GPIO.LOW)
    GPIO.digitalWrite(IC2A, GPIO.LOW)
    GPIO.digitalWrite(IC2B, GPIO.LOW)

# Looped by WebIOPi
def loop():
    # Toggle LED each 5 seconds
    webiopi.sleep(5)

# Called by WebIOPi at server shutdown
def destroy():
    webiopi.debug("Script with macros - Destroy")
    # Reset GPIO functions
    GPIO.setFunction(IC1A, GPIO.IN)
    GPIO.setFunction(IC1B, GPIO.IN)
    GPIO.setFunction(IC2A, GPIO.IN)
    GPIO.setFunction(IC2B, GPIO.IN)

# A macro without args which return nothing
@webiopi.macro
def MoveLeft():
    GPIO.digitalWrite(IC1A, GPIO.HIGH)
    GPIO.digitalWrite(IC1B, GPIO.LOW)

@webiopi.macro
def MoveRight():
    GPIO.digitalWrite(IC1A, GPIO.LOW)
    GPIO.digitalWrite(IC1B, GPIO.HIGH)

@webiopi.macro
def MoveForward():
    GPIO.digitalWrite(IC2A, GPIO.HIGH)
    GPIO.digitalWrite(IC2B, GPIO.LOW)

@webiopi.macro
def MoveBackward():
    GPIO.digitalWrite(IC2A, GPIO.LOW)
    GPIO.digitalWrite(IC2B, GPIO.HIGH)

@webiopi.macro
def Stop():
    GPIO.digitalWrite(IC1A, GPIO.LOW)
    GPIO.digitalWrite(IC1B, GPIO.LOW)
    GPIO.digitalWrite(IC2A, GPIO.LOW)
    GPIO.digitalWrite(IC2B, GPIO.LOW)
