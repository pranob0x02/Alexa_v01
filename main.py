import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")

engine.setProperty('rate', 150)
# setting up new voice rate
engine.setProperty("voice", voices[1].id)


# changing index, changes voices. 1 for female

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            # using microphone as source
            talk("Hi i am alexa aka goriber ChatGPT. How can i help you....")

            print("Listening.........")
            voice = listener.listen(source)
            # using listerner to listen to source

            command = listener.recognize_google(voice)
            # converts voice to text using recognize_google()

            command = command.lower()
            if "alexa" in command:
                command = command.replace("hey alexa", "")
                return command
            # command is used in execute_command() function
            # command = take_command()


    except:
        talk("Sorry i couldn't understand what you just said.")


def execute_command():
    command = take_command()

    try:
        if "play" in command:
            # play youtube video using pywhatkit
            song = command.replace("can you play", "")
            talk("playing" + song)
            pywhatkit.playonyt(song)


        elif "time" in command:
            # Tell the time
            time = datetime.datetime.now().strftime("%I:%M %p")
            talk(f"current time is {time}")
            print(time)

        elif "who is" in command:
            # get info about a person from Wikipedia
            person = command.replace("who is", "")
            talk("Showing info about " + person)
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)


        elif "date" in command:
            # Tell alexa to go on a date
            talk(
                "There are 7 billion people on earth and you are still single. Sorry to disappoint you, but I have a boyfriend.")


        elif "joke" in command:
            # Tell alexa to tell a Joke
            joke = pyjokes.get_joke()
            talk(joke)
            print(joke)


        else:
            talk("Can you please repeat.....")

    except:
        talk("Oooops! something went wrong!")


# ------------ execution --------------
execute_command()
