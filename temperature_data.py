import time
import serial
import clr  # the pythonnet module.

clr.AddReference(r'E:\test_ann\compile_program\LibreHardwareMonitor\LibreHardwareMonitorLib')
# e.g. clr.AddReference(r'LibreHardwareMonitor\LibreHardwareMonitorLib'), without .dll
arduinoData = serial.Serial('com4', 115200)
# change 'com4' to your comport for arduino and make sure to match baud-rate

from LibreHardwareMonitor import Hardware

device = Hardware.Computer()
device.IsCpuEnabled = True
device.Open()


while True:
    temps = []
    core_number = 4 # change this to the number of cores present in CPU.
    for d in device.Hardware:
        d.Update()

        if d.HardwareType == Hardware.HardwareType.Cpu:
            for sensor in d.Sensors:
                if sensor.SensorType == Hardware.SensorType.Temperature:
                    temps.append(sensor.Value)
        data = str(temps[core_number])
        print(data, ' ->', type(data))
        data = data + '\r'
        arduinoData.write(data.encode())
        time.sleep(2)
