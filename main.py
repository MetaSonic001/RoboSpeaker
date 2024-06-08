import pyttsx3

if __name__ == '__main__':
    engine = pyttsx3.init()
    print("Welcome to RoboSpeaker")
    while True:
        x = input("What do you want me to speak: ")
        if x.lower() == "q":
            engine.say("bye bye friend")
            print("bye bye friend")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()
