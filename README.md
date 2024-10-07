# CPU-Temperature-Monitor-using-Arduino
This Project shows the temperature data extracted from OpenHardwareMonitor and shows the temperature on a LCD display using arduino making it easy to monitor CPU temperature without leaving any application window.
# Dependencies
  ## Software
  Any python interpreter, Arduino IDE and [OpenHardwareMonitor](https://openhardwaremonitor.org/).
  ## Python
  1. pythonnet package: This package is used to access the OpenHardwareMonitorLib.dll and extract data from it. This package is imported as clr. To install this package run ```pip install pythonnet``` in the terminal.
  2. pyserial package: This package is used for serial communication using python. For this project this package was used to sned the temperature data to arduino. To install this package run ```pip install pyserial``` in the terminal.
  3. Administrator privilages must be given when running the code so that OpenHardwareMonitor can access temperature data.
  ## Arduino
  1. ```LiquidCrystal_I2C``` and ```SoftwareSerial``` libraries must be installed on the Arduino IDE.
  2. Make sure that i2c address matches the i2c modules address. 
     
