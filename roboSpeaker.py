
import win32com.client as wincom

if __name__ == "__main__":
    print("Welcome to RoboSpeaker 1.0 . Created by Bishal Rokaha.")
    speak = wincom.Dispatch("SAPI.SpVoice")
    while True:
        text = input("Enter what you want me to speak. ")
        if text == "quit":
            speak.Speak( "bye bye friend.")
            break
        speak.Speak(text)