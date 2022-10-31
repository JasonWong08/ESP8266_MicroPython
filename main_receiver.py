import network
import espnow
from machine import UART


dicCommand = {
    b'walk': "kwkF",
    b'back': "kbk",
    b'stop': "d",
    b'step':"kvtF"
    }

# def commandConvert(msg = b'stop'):
#     if msg in dicCommand:
#         return dicCommand.get(msg)

def espnow_rx():
    # config UART
    uart = UART(0, baudrate = 115200)
    
    # A WLAN interface must be active to send()/recv()
    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    sta.disconnect()        # Disconnect from last connected WiFi SSID
    
    e = espnow.ESPNow()     # Enable ESP-NOW
    e.active(True)
    
    peer = b'\xf4\xcf\xa2\x6b\xf5\x56'    # MAC address of peer's wifi interface
    e.add_peer(peer)          # Sender's MAC registration
#     print("Receive started.")
    while True:
        host, msg = e.recv()
#         if msg == b'walk':        # decode message and translate
#             uart.write("kwkF")    # to the NyBoard's command
#         elif msg == b'back':
#             uart.write("kbk")
#         elif msg == b'stop':
#             uart.write("d")
        serialCommand = dicCommand.get(msg, "None")  #search in the command dictionary by key
        if serialCommand != "None":                  # find the pre-defined command
            uart.write(serialCommand)
#             print("Receive command:" + msg)
#         else:
#             print(msg + " is not supported.")
                
                
if __name__ == "__main__":
    espnow_rx()
    