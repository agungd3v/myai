from modules import speak, takeCommand, openBrowser

if __name__ == "__main__":
  speak("I am your artificial intelligence, how can I help you?")
  while True:
    query = takeCommand().lower()
    if "open youtube" in query:
      speak("Open youtube in browser...")
      openBrowser("youtube.com")
    elif "stop" in query:
      speak("Just call me, if there's anything you need. Byebye")
      break
    else:
      speak("I don't understand what you're saying, say it again...")
