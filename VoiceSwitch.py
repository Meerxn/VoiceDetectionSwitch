import os # User os system import
import sys 
import speech_recognition as listener # Listener import
import webbrowser
def myCommand():
   
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
def larkSpeaks(userSpeech):
    for line in userSpeech.splitlines():
        os.system("say " + userSpeech)
def lark(command):
      
    
    if 'hello' in command:
        
            larkSpeaks('hello there ')
    if 'good' in command:
             larkSpeaks('that is great ')
          
    if 'amazing' in command:
           larkSpeaks(' happy birthday NANDAN ' )
           webbrowser.open("https://www.youtube.com/watch?v=flMN4ME3isU")
         
           
    if 'goodbye' in command:
     larkSpeaks('goodbye and have a good day')
     sys.exit()

larkSpeaks('Hello Fardeen welcome to the lark experience ')  
while True:
    lark(myCommand())