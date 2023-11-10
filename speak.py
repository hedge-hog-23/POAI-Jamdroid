import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import subprocess

# Initialize the recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand your command.")
        return ""
    except sr.RequestError:
        print("I'm sorry, I'm having trouble connecting to the internet.")
        return ""

def open_application(application_name):
    # replace with your file name or paths
    application_paths = {
        "notepad": "notepad.exe",
        "chrome": r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        "figma": r"C:\Users\Senth\AppData\Local\Figma\Figma.exe"
    }

    
    if application_name in application_paths: #checking if file exists
        try:
            app_path = application_paths[application_name]
            subprocess.Popen([app_path], shell=True)
            speak(f"Opening {application_name}")
        except Exception as e:
            speak(f"Sorry, I couldn't open {application_name}")
    else:
        speak(f"Sorry, I don't know how to open {application_name}")


    if application_name in application_paths:
        try:
            app_path = application_paths[application_name]
            subprocess.Popen([app_path], shell=True)
            speak(f"Opening {application_name}")
        except Exception as e:
            speak(f"Sorry, I couldn't open {application_name}")
    else:
        speak(f"Sorry, I don't know how to open {application_name}")

def run_python_script(file_name):
    file_path = f"D:\\POAI_proj\\OpenCVProjects\\{file_name}.py" # change this path too !!
    os.system(f"python {file_path}")
def search(query):
    sanitized_query = "+".join(query.split())
    url = f"https://www.google.com/search?q={sanitized_query}"
    webbrowser.open(url)

def main():
    speak("Hello, I am your desktop assistant. How can I assist you today?")

    while True:
        command = listen()

        if "hello" in command:
            speak("Hello! How can I help you?")
            
        elif "open" in command:
            app_name = command.split("open", 1)[1].strip()
            open_application(app_name)
            
        elif "bye" in command:
            speak("Goodbye!")
            speak("Sure! Reach me if you need help!")
            break
        elif "search" in command:
            query = command.split("search", 1)[-1].strip()
            search(query)
            
        elif "python file" in command:
            file_name = command.split("python file", 1)[1].strip()
            speak(f"opening {file_name}")
            speak("press q to exit")
            run_python_script(file_name)
            
            
        else:
            speak("I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    main()
