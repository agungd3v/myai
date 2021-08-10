from modules import speak, takeCommand
import webbrowser

if __name__ == "__main__":
  speak("I am your artificial intelligence, how can I help you?")
  while True:
    query = takeCommand().lower()
    if "open youtube" in query:
      speak("Open youtube in browser...")
      webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("youtube.com")
    elif "stop" in query:
      speak("Just call me, if there's anything you need. Byebye")
      break
    else:
      speak("I don't understand what you're saying, say it again...")
