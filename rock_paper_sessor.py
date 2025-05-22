import random 
import pyttsx3
engine =pyttsx3.init('sapi5')
engine.setProperty('volume',2)
engine.setProperty('rate',225)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()
options=['rock','paper','scissor']
while True:
    user_input=input('enter the value (rock/paper/scissor)or {quit} for exit: ')
    if user_input=="quit":
        print("Thanks for playing!")
        text="Thanks for playing!"
        speak(text)
        quit()
        break
    if user_input not in options:
        print("enter the valid input")
        continue
    computer_pick=random.choice(options)
    print(f'computer choice',computer_pick)
    if user_input==computer_pick:
        print("It's Draw")
        text="It's Draw"
        speak(text)
    elif (user_input=="rock"and computer_pick=="scissor")or\
          (user_input=="paper"and computer_pick=="rock")or\
            (user_input=="paper"and computer_pick=="scissor"):
        print("you win")
        text="congratualtion you win"
        speak(text)
    else:
        print("you lost")
        text="you lost! try again"
        speak(text)


    