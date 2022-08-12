import subprocess
try:
    import speech_recognition as sr
    import pyaudio as pa
    import pywhatkit as pwk
    from gtts import gTTS
    from playsound import playsound
    from pyjokes import *
except:
    subprocess.check_output('pip install -r requirements.txt')
   
def speech(text):
    print(text)
    language = 'en'
    output = gTTS(text=text, lang=language, slow=False)
    output.save('./sounds/output.mp3')
    playsound('./sounds/output.mp3')
  
def getAudio():
    recorder = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        playsound('./sounds/activate.wav')
        audio = recorder.listen(source)
        
    text = recorder.recognize_google(audio)
    print("You said: {}".format(text))
    return text

text = getAudio()

if "youtube" in text.lower():
    speech('Okay, I will bring that up on YouTube for you.')
    pwk.playonyt(text)
elif "joke" in text.lower():
    speech(pyjokes.get_joke())
