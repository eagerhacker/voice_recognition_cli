from gtts import gTTS
import os

def tts(text):
    tts = gTTS(text)
    file_name = 'audio.mp3'
    tts.save(file_name)

    while True:
        if(os.path.exists(file_name)):

            os.system(file_name)
            break
        else:
            print('Work in progress',end='')
            


