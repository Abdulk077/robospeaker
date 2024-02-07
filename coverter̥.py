import pyttsx3
def speak(text):
    # Here we are creating a function by using of pyttsx3 lib to speak the system
    engine = pyttsx3.init()
    engine.setProperty('rate', 110)
    engine.setProperty('volume', 0.9)
    engine.setProperty('pitch', 10)
    engine.setProperty('age', 10)
    engine.setProperty('emphasis', 'full')
    engine.setProperty('break_time ', 50)
    engine.setProperty('lang', 'hi')
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
def male():

    if (b.lower() == 'q'):
        d = b
        d = "Unknown"
        end(d)
        d = input("Enter our name  properly ")
        speak(f" helloo {d}")
    else:
        speak(f" helloo {b}")

    print("Enter to our robo speaker ")
    print("Enter what you want to pronounce ")
    speak("Enter what you want to pronounce ")
    x = input()
    a = x
    if (a.lower() == 'q'):
        end(a)
    while x.lower() != 'q':
        if (x.lower() != 'y'):
            command = f" {x}"
            speak(command)
        print("Enter what you want to pronounce ")
        speak("Enter what you want to pronounce ")
        x = input()
        if (x.lower() == 'q'):
            end(x)
            x = 'y'
def female():

    if (b.lower() == 'q'):
        d = b
        d = "Unknown"
        end(d)
        d = input("Enter our name  properly ")
        speakf(f" helloo {d}")
    else:
        speakf(f" helloo {b}")

    print("Enter to our robo speaker ")
    print("Enter what you want to pronounce ")
    speakf("Enter what you want to pronounce ")
    x = input()
    a = x
    if (a.lower() == 'q'):
        end(a)
    while x.lower() != 'q':
        if (x.lower() != 'y'):
            command = f" {x}"
            speakf(command)
        print("Enter what you want to pronounce ")
        speakf("Enter what you want to pronounce ")
        x = input()
        if (x.lower() == 'q'):
            end(x)
            x = 'y'

def end(e):
    speakf(f"Hello wait a Second {e} give us another  chance if you want to continue type y")
    speakf("Are you sure to quit the program  Enter  q  ")
    d = input()
    if (d.lower() == 'q'):
        speakf("Thanks for your Attension  We Are quiting Your Program")
        quit()
while True:

    speak("if you want to quit at any time the program enter q ")
    print("Chose your voice ")
    print("If you want male voice Enter 1 ")
    print("If you want female voice Enter 2 ")
    speak("If you want to continue with my voice Enter 1")
    speakf(" If you want to interested in my voice then type 2")
    c = input()
    if(c.lower() == 'q'):
        c = "Unknown"
        end(c)

    if(c == '1'):
        speak("Enter your name ")
        b = input("Enter your Name ")
        male()

    else:
        speakf("Enter your name ")
        b = input("Enter your name ")
        female()

    # here we write code for user to input and Speak by system