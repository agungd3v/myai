from modules import speak, takeCommand, openBrowser, find_files
import os

if __name__ == "__main__":
  speak("I am your artificial intelligence, how can I help you?")
  while True:
    query = takeCommand().lower()
    print(query)
    if "open youtube" in query:
      speak("Open youtube in browser...")
      openBrowser("youtube.com")
    elif "play music" in query:
      foundfiles = find_files("Nightcore*", "C:/Users/AGUNG")
      if len(foundfiles) > 0:
        os.startfile(foundfiles[0])
    elif "stop" in query or "maybe it's all over" in query:
      speak("Just call me, if there's anything you need. Byebye")
      break
    else:
      if "none" in query:
        speak("is there anything else i can do to help ?")
      else:
        speak("I don't understand what you're saying, say it again...")
