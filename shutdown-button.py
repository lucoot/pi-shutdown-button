#Shutdown and Reboot Button and LED for Raspberry Pi
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

#Pin Assignments for Pi Shield 1.0
led = [13, 6, 19, 21, 26]
button = [7, 22, 27, 17, 25, 8]
switch = [24, 18, 23]

#Pin Assignment for Reboot/Shutdown Function
power_led = led[4]
power_button = button[5]

#Set GPIO
GPIO.setwarnings(False);
GPIO.setup(power_button , GPIO.IN)
GPIO.setup(power_led , GPIO.OUT)

#Turn ON Power LED
GPIO.output(power_led, True)

# Functions
def Shutdown ():
    os.system("sudo shutdown now")
    os.system("echo user shutdown requested | wall")
def Reboot ():
    os.system("sudo reboot now")
    os.system("echo user reboot requested | wall")

def BlinkWait(loops):
    for i in range(loops):
        GPIO.output(power_led, False)
        time.sleep(0.2)
        GPIO.output(power_led, True);
        time.sleep(0.2)

def PowerButton(channel):
    GPIO.remove_event_detect(power_button)
    BlinkWait(10)
    if GPIO.input(power_button):
        Shutdown()
    else:
        Reboot()

#Trigger
GPIO.add_event_detect(power_button, GPIO.RISING, callback = PowerButton, bouncetime = 200)

while True:
    time.sleep(1)

