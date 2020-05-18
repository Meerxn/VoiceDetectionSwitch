# -*- coding: utf-8 -*-
"""
Created on Sun May 17 21:09:09 2020

@author: meeran
"""

import speech_recognition as sr
import os
import sys
import serial # install pySerial 
import time
board = serial.Serial("your serial port krishang")

def myCommand():
    "listens for commands"
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('....')
        command = myCommand();
    return command

def assistant(command):
 if 'on' in command:
     time.sleep(1)
     board.write('H')
     
 elif 'off' in command:
     time.sleep(1)
     board.write('L')
 else:
    time.sleep(1)
    board.close()
    sys.exit()
    
    
    
   




time.sleep(2)

while True:
    bulb(myCommand())
