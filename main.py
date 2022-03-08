
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            talk("Hi i am alexa. How can i help you....")

            print("Listening.........")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa", "")
                return command

    except:
        pass


def execute_command():  # Play Youtube video
    command = take_command()
    if "play" in command:
        song = command.replace("play", "")
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif "time" in command:  # Tell the time
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk(f"current time is {time}")
        print(time)

    elif "who is" in command:  # get info about a person from Wikipedia
        person = command.replace("who is", "")
        talk("Showing info about " + person)
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif "date" in command:  # Tell alexa to go on a date
        talk("Sorry! i hava a Boyfriend....")

    elif "joke" in command:  # Tell alexa to tell a Joke
        talk(pyjokes.get_joke())

    else:
        talk("Can you please repeat.....")


execute_command()
