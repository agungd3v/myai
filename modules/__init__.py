import pyttsx3
import speech_recognition as sr
import webbrowser
from modules.file_path import findmyfiles

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
    r.pause_threshold = 1
    audio = r.listen(source)

    try:
      saying = r.recognize_google(audio, language = 'en-US')
    except Exception as e:
      print("Say that again please...") 
      return None
    return saying

def openBrowser(url):
  return webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open(url)

def find_files(filename, search_path):
  return findmyfiles(filename, search_path)
