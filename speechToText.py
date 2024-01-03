import speech_recognition as sr

def stt(input_source):
    r = sr.Recognizer()

    try:
        if(input_source == 'mic'):
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                audio = r.listen(source)
                text = r.recognize_amazon(audio).lower()
                print(text)
        
        else:            
            try:
                file = input('Enter path to file: ')
                with sr.AudioFile(file) as audioFile:
                    audio = r.record(audioFile)
                    text = r.recognize_google(audio)
                    print(text)
            except ValueError as ve:
                print('not supported format')
            except Exception as e:
                print('no input audio file', e.args)

    except Exception as e:
        print('error:', e.args)