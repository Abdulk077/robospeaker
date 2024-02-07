import pyttsx3
def speak(text):

    # Here we are creating a function by using of pyttsx3 lib to speak the system
    engine = pyttsx3.init()
    engine.setProperty('rate', 105)
    engine.setProperty('volume', 0.9)
    engine.setProperty('pitch', 10)
    engine.setProperty('age', 10)
    engine.setProperty('emphasis', 'full')
    engine.setProperty('break_time ', 50)
    engine.setProperty('lang', 'es')
    engine.say(text)
    engine.runAndWait()

def speakf(text):
    # here we are creating femail vois by pyttsex3 lib
    engine = pyttsx3.init()
    engine.setProperty('voice', engine.getProperty('voices')[1].id)
    engine.setProperty('rate', 115)
    engine.setProperty('pitch', 0.5)
    engine.setProperty('age', 10)
    engine.setProperty('emphasis', 'full')
    engine.setProperty('break_time ', 200)
    engine.setProperty('language', 'uk')
    engine.say(text)
    engine.runAndWait()

def end():
    speakf(f"Hello wait a Second {b} give us another  chance if you want to continue type y")
    speakf("Are you sure to quit the program  Enter  q  ")
    d = input()
    if (d.lower() == 'q'):
        speakf("Thanks for your Attension  We Are quiting Your Program")
        quit()

while True:
    # here we write code for user to input and Speak by system
    speak("if you want to quit at any time the program enter q ")
    b = input("Enter our name ")
    if (b.lower() == 'q'):
        b = "Unknown"
        end()
        b = input("Enter our name  properly ")
        speak(f" helloo {b}")
    else:
        speak(f" helloo {b}")

    print("Enter to our robo speaker ")
    print("Enter what you want to pronounce ")
    speak("Enter what you want to pronounce ")
    x = input()
    a = x
    if (a.lower() == 'q'):
        end()
    while x.lower() != 'q':
        if(x.lower() != 'y'):
            command = f" {x}"
            speak(command)
        print("Enter what you want to pronounce ")
        speak("Enter what you want to pronounce ")
        x = input()
        if (x.lower() == 'q'):
            end()
            x ='y'