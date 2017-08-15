from gpiozero import OutputDevice, CPUTemperature
from time import sleep
import time

fanPin = 4 # Define pin
fan = OutputDevice(fanPin)
cpu = CPUTemperature()
logPath = "/home/pi/PythonProjects/FanControl/FanControl.log"

def GetCurrentData(): # Get date, time and CPU temperature as global variables
    global currdate
    global currtime
    global currtemp
    global newfanstate
    currdate = (time.strftime("%d.%m.%Y"))
    currtime = (time.strftime("%H:%M:%S"))
    currtemp = int(cpu.temperature)

def LogWrite(): # Write log
    with open(logPath, "a") as text_file:
        text_file.write("{} {} Current CPU temperature: {} Turning fan {} - GPIO {} previous state {}\n".format(currdate, currtime, currtemp, newfanstate, fanPin, fan.value))
        text_file.close()

def DebugPrint(): # For debugging
    print '{} {} Current CPU temperature: {} Turning fan {} - GPIO {} previous state {}'.format(currdate, currtime, currtemp, newfanstate, fanPin, fan.value)

while True:
    GetCurrentData()
    if cpu.temperature > 63 and fan.value == False: # Start cooling
        newfanstate = "on"
		#DebugPrint()
        LogWrite()
        fan.on()
    if cpu.temperature < 50 and fan.value == True: # Stop cooling
        newfanstate = "off"
		#DebugPrint()
        LogWrite()
        fan.off()
    sleep(30) # Wait before the next temperature check