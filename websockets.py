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
def larkBotListener():
     r = listener.Recognizer()
    with listener.Microphone() as source:
        print('Listening') # Telling user that they are being heard
        r.pause_threshold= 0.5 # Duration for pausing 
        r.adjust_for_ambient_noise(source, duration=1) 
        userSpeech = r.listen(source)
    try: 
         
        command = r.recognize_google(userSpeech).lower()
    
      
    except LookupError: # speech is unintelligible
        print("Could not understand audio")
        command = myCommand();
    return command
def larkBotSpeaker(botSpeech):
    os.system("say " + botSpeech)
def larkCommandProcess(command):
    if 'on' in command:
        send_command(1)
        larkBotSpeaker('The light is switched on')
   
         
           
    if 'off' in command:
     larkSpeaks('switching off lights')
     send_command(99)
     sys.exit()    


while True:
    larkCommandProcess(larkBotListener())




