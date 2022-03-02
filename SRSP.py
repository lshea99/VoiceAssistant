#Speech Recognition Pyhton Script
#Author:Luke Tvarozna

import speech_recognition

def speech():

    recognizer = speech_recognition.Recognizer()

    while True:

        try:
            #Declare microphone as listening device
            with speech_recognition.Microphone() as mic:
                
                #Adjust for outside noises
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                
                #Declares the language/grammer 
                text = recognizer.recognize_google(audio)
                text = text.lower()

                # print(f"Recognized {text}")
        
                text = str(recognizer.recognize_google(audio))

                return(text)

        # If it expereinces an error it will reset
        except:
            # print("Unknown")
            return(None)