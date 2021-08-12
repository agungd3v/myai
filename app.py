from modules import speak, takeCommand, openBrowser, playMusic

WAKE = "buddy"

while True:
  print("Listening...")
  query = takeCommand()

  if query.count(WAKE) > 0:
    speak("hi, do you need help ?")
    print("Listening...")
    query = takeCommand()

    if "open youtube" in query:
      speak("Open youtube in browser...")
      openBrowser("youtube.com")

    if "play music" in query:
      speak("Searching folder for you...")
      playMusic()

  if "stop" in query or "maybe everything for now is enough" in query:
    speak("OK. Just call me, if there's anything you need. Byebye")
    break
