from modules import speak, takeCommand, openBrowser, playMusic

WAKE = "buddy"
CAN = "what you can"

while True:
  query = takeCommand().lower()
  if query.count(WAKE) > 0:
    speak("hi, do you need help ?")
    query = takeCommand().lower()
    if query.count(CAN) > 0:
      speak("I can read documents")
      speak("I can open a web in the browser")
      speak("I can play a music")
      speak("I can send an email")
    if "open youtube" in query:
      openBrowser("youtube.com")
    if "music" in query:
      playMusic()
    if "stop" in query or "maybe everything for now is enough" in query:
      speak("OK. Just call me, if there's anything you need. Byebye")
      break
