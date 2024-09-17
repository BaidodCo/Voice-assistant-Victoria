from gtts import gTTS
import os
from os import system
from colorama import Fore
import datetime
import difflib
import re
import webbrowser
import pyjokes
from autocorrect import Speller
import tldextract
import time 

current_time = datetime.datetime.now()
# Hmm Some Colors


red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
white = Fore.WHITE 
yellow = Fore.YELLOW
purple = Fore.MAGENTA
cyan = Fore.CYAN

def sp(text):
  speech = gTTS(text=text, slow=False)
  speech.save("vic.mp3")
  os.system('play vic.mp3')


# all copyright reserved for khaled

sp('here is a simple list of what i can do')

os.system('clear')

print(red+"\nTeleuser : get telegram user for you")
print(cyan+"spy : get informations about someone")
print(red+"sleep : to make me inactive for a while")
print(cyan+"time : current time")
print(red+"joke : random joke")
print(cyan+"open : used to oped a app (ex: open youtube )")
print(red+"snapcheck (email@gmail.com) : check if the email online on snapchat")

print(red+"\niam good at chatting ig :D")


print(white+"\n[!] iam still in beta version")

outt = input(purple+"\n\ntype enter to go to the main page :")

if outt == '':
  os.system('python main.py')
  
