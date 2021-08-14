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

def speak(audio):
  engine = pyttsx3.init("sapi5")
  voices = engine.getProperty("voices")
  engine.setProperty("voice", voices[0].id)
  engine.setProperty("rate", 200)

  engine.say(audio)
  engine.runAndWait()

def takeCommand():
  print("Listening...")
  r = sr.Recognizer()
  with sr.Microphone() as source:
    audio = r.listen(source)
    saying = ""
    try:
      saying = r.recognize_google(audio)
      print(saying)
    except Exception as e:
      error = str(e)
  return saying

def openBrowser(url):
  speak("Open youtube in browser...")
  webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open(url)

def playMusic():
  speak("Ok.")
  loop = 1
  while True:
    if loop > 1:
      speak("Sorry. I can't find the folder, try saying it again")
    else:
      speak("Please, tell me the folder where to save the music")
    folder_found = None
    query = takeCommand()
    folder = query
    if folder != "":
      dump_sub_level_two = []
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
    if folder_found is not None:
      askPlayMusic(folder_found)
      break
    loop += 1

def askPlayMusic(path_music):
  music_list = []
  l_files = os.listdir(path_music)
  for fl in l_files:
    trim = fl.split(".")
    file_path = f'{path_music}/{fl}'
    if os.path.isfile(file_path) and trim[-1] == "mp3":
      music_list.append(file_path)
  if len(music_list) > 0:
    speak(f"I found {len(music_list)} songs in the folder. Do you want to play all the songs in this folder ?")
    while True:
      say = takeCommand().lower()
      if "yes" in say:
        speak("have a nice day")
        for music in music_list:
          try:
            audio = MP3(music)
            audio_info = audio.info
            os.startfile(music)
            print(f'Playing {music.split("/")[-1]}')
            time.sleep(int(audio_info.length))
          except:
            print("error please check")
        break
