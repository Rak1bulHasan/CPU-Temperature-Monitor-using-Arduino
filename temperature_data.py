import time
import serial
import clr  # the pythonnet module.

clr.AddReference(r'E:\TEMP_Project\OpenHardwareMonitor\OpenHardwareMonitorLib')
# e.g. clr.AddReference(r'OpenHardwareMonitor/OpenHardwareMonitorLib'), without .dll
arduinoData = serial.Serial('com4', 115200)
# change 'port:' to your comport for arduino and make sure to match baud-rate

from OpenHardwareMonitor.Hardware import Computer

c = Computer()
c.CPUEnabled = True  # get the Info about CPU
c.GPUEnabled = True  # get the Info about GPU
c.Open()
while True:
    if "/temperature" in str(c.Hardware[0].Sensors[9].Identifier):
        print('cpu temp: ', c.Hardware[0].Sensors[9].get_Value())
        c.Hardware[0].Update()
        print(type(c.Hardware[0].Sensors[9].get_Value()))
        data = str(c.Hardware[0].Sensors[9].get_Value())
        print(data, ' ->', type(data))
        data = data + '\r'
        arduinoData.write(data.encode())
        time.sleep(2)
