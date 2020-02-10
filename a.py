
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone () as source:
    print('speak any thing:')
    audio = r.listen(source)
    words = r.recognize_google(audio, key=None)
    print(words)

