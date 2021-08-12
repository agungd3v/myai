from modules import speak, takeCommand, openBrowser, playMusic

if __name__ == "__main__":
  speak("I am your bot, how can I help you?")
  while True:
    query = takeCommand().lower()
    print(query)
    if "open youtube" in query:
      speak("Open youtube in browser...")
      openBrowser("youtube.com")
    elif "play music" in query:
      playMusic()
    elif "stop" in query or "maybe everything for now is enough" in query:
      speak("OK. Just call me, if there's anything you need. Byebye")
      break
    else:
      if "none" in query:
        speak("is there anything else i can do to help ?")
      else:
        speak("I don't understand what you're saying, say it again...")
