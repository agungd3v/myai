import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty("voice", voices[1].id)

def speak(audio):
  engine.say(audio)
  engine.runAndWait()

def takeCommand():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening...")
    r.pause_threshold = 2
    audio = r.listen(source)

    try:
      print("Recognizing...")    
      query = r.recognize_google(audio, language = 'id-ID')
    except Exception as e:
      print("Say that again please...") 
      return "None"
    return query
