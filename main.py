from textToSpeech import tts
from speechToText import stt
import os, sys

while True:
    print('Voice Recognition\n1. Text To Speech\n2. Speech To Text\n3. Exit')
    choice = 0

    try:
        choice = int(input('Enter option: '))
    except ValueError as ve:
        print('Enter valid number')

    os.system('cls')

    if(choice == 1):
        print('Select option:\n1. From Text File\n2. From User Input\n0. Back')
            
        while True:
            c = int(input('Enter option: '))

            if(c == 0):
                os.system('cls')                
                break
            if(c == 1):
                file = input('Enter path to file: ')
                try:
                    with open(file) as f:
                        contents = f.read()
                        tts(contents)
                        break
                except FileNotFoundError as fnfe:
                    print('File Not Found', fnfe.args)

            if(c == 2):
                input_text = input('Enter text for recognition: ')
                tts(input_text)

    if(choice == 2):
        print('Select option:\n1. From Audio File (WAV only)\n2. From Mic\n0. Back')
            
        while True:
            c = int(input('Enter option: '))
            if(c == 0):
                os.system('cls')                
                break
            if(c == 1):        
                stt('file2')

            if(c == 2):
                print('Open mic to speak: ')
                stt('mic')
                break            
    if(choice == 3):
      
        sys.exit()