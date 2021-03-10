import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 200)

print('Ready to speak!')

while True:
    user_input = input()
    if user_input == '/exit':
        break
    engine.say(user_input)
    engine.runAndWait()

engine.say('Okay, goodbye now.')
engine.runAndWait()