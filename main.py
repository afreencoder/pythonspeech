import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTs
from time import ctime

r = sr.Recognizer()
def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UknownValueError:
            print('Sorry, I did not get that')
        except sr.RequestError:
            print('Sorry, my speech service is down')
        return voice_data

def alexis_speak(audio_string):
    tts = gTTs(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'What is your name' in voice_data:
        alexis_speak('My name is Alexis')
    if 'what time is it' in voice_data:
        print(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you wan to search?')
        url = 'https://google.com/searchq=' + search
        webbrowser.get().open(url)
        alexis_speak('Here is what I found for' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        alexis_speak('Here is the location of' + location )
    if 'exit' in voice_data:
        exit()

time.sleep(1)
print('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)

