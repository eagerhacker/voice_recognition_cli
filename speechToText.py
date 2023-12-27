import speech_recognition as sr

def stt(input_source, audioFile = None):
    r = sr.Recognizer()

    try:
        if(input_source == 'mic'):
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                audio = r.listen(source)
                text = r.recognize_amazon(audio).lower()
                print(text)
        
        else:
            if(audioFile):
                file = sr.AudioFile('voice.wav')
                audio = r.record(file)
                text = r.recognize_google(audio)
                print(text)
            else:
                print('no input audio file')
                
    except Exception as e:
        print('error:',e.args)