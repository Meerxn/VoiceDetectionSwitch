from ws4py.client.threadedclient import WebSocketClient #Install ws4py
import time, requests
import speech_recognition as sr
import os
import sys

esp8266host = "ws://192.168.0.151:81/"

class DummyClient(WebSocketClient):
    def opened(self):
        print("Websocket open")
    def closed(self, code, reason=None):
        print ("Connexion closed down", code, reason)
    def received_message(self, m):
        print (m)

# Number 1 for it to turn on, anything else to turn off
def send_command(number):
    ws = DummyClient(esp8266host)
    ws.connect()
    print("Ready !")
    ws.send(f"led0:{int(number)}")
    ws.close()
    exit()


send_command(1)
    



