from gtts import gTTS
import os
from os import system
from colorama import Fore

# all copyright reserved for khaled
# Hmm Some Colors

red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
white = Fore.WHITE 
yellow = Fore.YELLOW
purple = Fore.MAGENTA
cyan = Fore.CYAN

def sp(text):
  speech = gTTS(text=text)
  speech.save("vic.mp3")
  os.system('play vic.mp3')


os.system('clear')

def sleep():
    while True:
        sp('Type unsleep to Re Activate Me')
        print("")
        print("")
        user_input = input(red+'[!]'+white+" Type UnSleep To WakeUp: ").lower().strip()
        
        if user_input == "unsleep" or "wakeup" or "wake up" or "victoria" or "wakey wakey" or "wake" or "turn on" or "on" or "start" or "re activate" or "reactivate" or "":
            break

sleep()