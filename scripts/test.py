import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 200)

engine.say('Hi, this is my wishlist')
wishlist = ['🐙', '🐸', '🦑', '🦎', '🐧', '🦞', '🦥', '🐲', '🌞', '🐉']
for i in range(10):
    mySuperString = f'{str(i+1)} {wishlist[i]}.'
    engine.say(mySuperString)
engine.say('Okay, goodbye now.')

engine.runAndWait()