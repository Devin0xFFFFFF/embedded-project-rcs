# import Adafruit_BBIO.UART as UART
import serial

# UART.setup("UART1")

ser = serial.Serial(port="/dev/ttyUSB0", baudrate=38400)
ser.close()
ser.open()
# while (True):
if (ser.isOpen()):
    print("Serial Open.")
    tempresult = ser.read_all()
    print(tempresult)
    # ser.write("Hello World!")

ser.close()
