from machine import UART
import time


uart = UART(0, baudrate=115200,timeout=5)

# walk
def walk(time_ms):
    print("walk\n")
    uart.write("kwkF")      # walk cmd
    time.sleep_ms(time_ms)  # keep time
    uart.write("d")         # stop
    time.sleep_ms(1500)
    
# backward
def back(time_ms):
    print("back\n")
    uart.write("kbk")
    time.sleep_ms(time_ms)
    uart.write("d")
    time.sleep_ms(1500)

# stop
def stop():
    uart.write("d")
    
def initConnection():
    connected = False
    while True:
        uart.write("d")
        for t in range(10):
            uos.dupterm(None, 1)
            time.sleep_ms(5)
            result = uart.read(1)
            uos.dupterm(uart, 1)
#             result = sys.stdin.read()
            if result != None:
#                 uart.write(result)    # for debug
                if result == b"d":
#                 if result.encode() == b"d":
                    connected = True
                    break
            time.sleep_ms(10)

        if connected:
            break
    uart.write("b22 4 24 4 26 4")
    
            

def actSeq():
    initConnection()
    time.sleep_ms(2000)
    walk(3000)
    back(3000)
    uart.write("m0 90\n")
    time.sleep_ms(3000)
    uart.write("i8 -20 9 -60\n")
    time.sleep_ms(2000)
    uart.write("b26 4 24 4 20 4")
    time.sleep_ms(1000)
    uart.write("d")
    uos.dupterm(None, 1)
    
if __name__ == "__main__":
    actSeq()
    