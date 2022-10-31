import network
import espnow
import time

sta = network.WLAN(network.STA_IF)    # Enable station mode for ESP
sta.active(True)
sta.disconnect()                      # Disconnect from last connected WiFi SSID

e = espnow.ESPNow()                   # Enable ESP-NOW
e.active(True)

peer1 = b'\x94\xb9\x7e\x02\x54\xe4'   # MAC address of peer1's wifi interface
e.add_peer(peer1)

# Old 2M esp8266
# peer2 = b'\x60\x01\x94\x5a\x9a\xb8'   # MAC address of peer2's wifi interface
# e.add_peer(peer2)

peer3 = b'\xe8\xdb\x84\xfc\x63\xf0'   # MAC address of peer3's wifi interface
e.add_peer(peer3)
print("Starting...")

while True:  
    e.send(peer1, "walk", True)           # send commands to peer1
#     e.send(peer2, "back", True)           # send commands to peer2
    e.send(peer3, "step", True)           # send commands to peer3
    time.sleep_ms(2000)
    e.send(peer1, "step", True)           # send commands to peer1
#     e.send(peer2, "walk", True)           # send commands to peer2
    e.send(peer3, "back", True)           # send commands to peer3
    time.sleep_ms(2000)
    e.send(peer1, "stop", True)
#     e.send(peer2, "stop", True)
    e.send(peer3, "stop", True)
    x = input()
    if x == "c":
        continue
    elif x == "q":
        break
    