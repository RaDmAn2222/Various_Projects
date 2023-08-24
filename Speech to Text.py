import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print('Please say something')
    audio = recognizer.listen(source)
    print('Time over, thanks')
try:
    print(recognizer.recognize_google(audio));
except:
    pass;