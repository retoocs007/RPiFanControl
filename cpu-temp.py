from gpiozero import CPUTemperature
from time import sleep
import time

cpu = CPUTemperature()

while True:

    currdate = (time.strftime("%d/%m/%Y"))
    currtime = (time.strftime("%H:%M:%S"))
    currtemp = int(cpu.temperature)

    print '{} {} Current CPU temperature: {} '.format(currdate, currtime, currtemp)

    # Wait before the next iteration
    sleep(10)