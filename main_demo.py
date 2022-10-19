from machine import UART
import time
import uos

uos.dupterm(None, 1)

uart = UART(0, baudrate=115200,timeout=5)

# walk
def walk(time_ms):
    print("walk\n")
    uart.write("kwkF")      # walk cmd
    time.sleep_ms(time_ms)  # keep time
    uart.write("d")         # stop
    
# backward
def back(time_ms):
    print("back\n")
    uart.write("kbk")
    time.sleep_ms(time_ms)
    uart.write("d")

# stop
def stop():
    uart.write("d")
    
def initConnection():
    connected = False
    while True:
        uart.write("d")
        for t in range(10):
            result = uart.read(1)
            if result != None:
#                 uart.write(result)    # for debug
                if result == b"d":
                    connected = True
                    break
            time.sleep_ms(10)
        if connected:
            break
    time.sleep_ms(2000)
    uart.write("b22 2 24 2 26 2")
    
            

def actSeq():
    initConnection()
    time.sleep_ms(2000)
    walk(5000)
    time.sleep_ms(2000)
    back(5000)
    time.sleep_ms(2000)
    walk(5000)
    time.sleep_ms(2000)
    back(5000)
    time.sleep_ms(2000)
    uart.write("b26 2 24 2 22 2")
    
    
if __name__ == "__main__":
    actSeq()
    