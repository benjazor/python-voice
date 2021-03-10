import requests
import pyttsx3
import json
import time

def tellOneJoke():
    # Setup the voice
    engine = pyttsx3.init()
    engine.setProperty('rate', 175)

    # Get the joke from an amazing API
    # https://github.com/15Dkatz/official_joke_api
    response = requests.get('https://official-joke-api.appspot.com/random_joke')

    # Check if the joke was recieved
    if response.status_code != 200:
        engine.say('Whoopsie whoopsie, it looks like I won\'t be able to tell you a joke today!')
        engine.runAndWait()
        return

    # Load the joke
    joke = json.loads(response.text)

    # Setup the joke
    engine.say(joke['setup'])

    # Wait for the punchline
    engine.runAndWait()
    time.sleep(1)

    # Drop the punchline
    engine.say(joke['punchline'])
    engine.runAndWait()

tellOneJoke()