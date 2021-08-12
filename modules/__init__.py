import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import time
from pathlib import Path
from mutagen.mp3 import MP3

HOME_PATH = str(Path.home()).split("\\")
SUB_LEVEL_PATH = ["Documents", "Desktop", "Downloads", "Pictures", "Videos", "Music"]
ADD_SLASH = None
PATH_DILIMITER = "/"

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
    audio = r.listen(source)

    try:
      saying = r.recognize_google(audio, language = 'en-US')
    except Exception as e:
      print("Say that again please...")
      return "None"
    return saying

def openBrowser(url):
  return webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open(url)

def playMusic():
  folder = "Nightcore"
  dump_sub_level_two = []
  folder_found = None
  start_finder = PATH_DILIMITER.join(HOME_PATH)
  while True:
    if os.listdir(start_finder).__contains__(folder):
      folder_found = start_finder + PATH_DILIMITER + folder
    else:
      for sub_level_one in SUB_LEVEL_PATH:
        if os.listdir(start_finder + PATH_DILIMITER + sub_level_one).__contains__(folder):
          folder_found = start_finder + PATH_DILIMITER + sub_level_one + PATH_DILIMITER + folder
    break
  if folder_found is None:
    for sub_level_one in SUB_LEVEL_PATH:
      for sub_level_two in os.listdir(start_finder + PATH_DILIMITER + sub_level_one):
        if os.path.isdir(start_finder + PATH_DILIMITER + sub_level_one + PATH_DILIMITER + sub_level_two):
          dump_sub_level_two.append(start_finder + PATH_DILIMITER + sub_level_one + PATH_DILIMITER + sub_level_two)
    if len(dump_sub_level_two) > 0:
      for dslt in dump_sub_level_two:
        try:
          if os.listdir(dslt).__contains__(folder):
            folder_found = dslt
        except PermissionError:
          print("Folder excluded reading : " + dslt)
  else:
    askPlayMusic(folder_found)

def askPlayMusic(path_music):
  speak("OK, I found the folder. Do you want to play all the songs in this folder ?")
  say = takeCommand().lower()
  if "yes" in say:
    l_files = os.listdir(path_music)
    for fl in l_files:
      trim = fl.split(".")
      file_path = f'{path_music}/{fl}'
      if os.path.isfile(file_path) and trim[-1] == "mp3":
        try:
          audio = MP3(file_path)
          audio_info = audio.info
          os.startfile(file_path)
          print(f'Playing {fl}')
          time.sleep(int(audio_info.length))
        except:
          print("error please check")
      else:
        print("error file music not found")
