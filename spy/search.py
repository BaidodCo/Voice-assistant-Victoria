# all copyright reserved for khaled
from search_engines import Google, Bing
import os
from gtts import gTTS
from os import system
from colorama import Fore
import datetime
import difflib
from fuzzywuzzy import fuzz
import re
import webbrowser
import pyjokes
from autocorrect import Speller
import tldextract

current_time = datetime.datetime.now()
# Hmm Some Colors
# all copyright reserved for khaled spy code is not made by me its a free source in github by lordgivt

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



class LordGivt():
    def __init__(self):
        self.name = None
        self.FName = None
        self.GFName = None
        self.last_name = None
        self.output = ""
        self.admin()

    def save(self):
        with open(f"{self.name}.txt", "a", encoding='utf-8') as F:
            F.write(self.output)
        F.close()
        print(f"Done Save Info in = {os.getcwd()}/{self.name}.txt")
        sp('done save informations')
        os.system('clear')
        os.system('python main.py')

    def admin(self):
        self.set_info()
        self.output += "[ done run ]\n\n"
        os.system('clear')
        print("Searching in Google ..")
        print("Searching in Bing note i will search google and bing more than 5 times..")
        sp('searching in bing plus google')
        space = " "

        if self.name and self.FName:
            sql = self.name + space + self.FName
            self.search_google(sql)
            self.search_bing(sql)
        if self.name and self.last_name:
            sql = self.name + space + self.last_name
            self.search_google(sql)
            self.search_bing(sql)
        if self.name and self.GFName and self.last_name:
            sql = self.name + space + self.GFName + space + self.last_name
            self.search_google(sql)
            self.search_bing(sql)
        if self.name and self.last_name:
            sql = self.name + space + self.last_name
            self.search_google(sql)
        if self.name and self.FName and self.last_name:
            sql = self.name + space + self.FName + space + self.last_name
            self.search_google(sql)
            self.search_bing(sql)

        if self.name and self.FName and self.GFName and self.last_name:
            sql = self.name + space + self.FName + space + self.GFName + space + self.last_name
            self.search_google(sql)
            self.search_bing(sql)

        print("[ Searching in Social Media ]")
        self.output += "\n\n\n\n\n"
        self.output += "[ Searching in Social Media ]\n"
        self.output += "[ Will Use Name For Search .. ]\n\n"

        self.search_in_social_media(self.name)
        self.save()

    def add_info(self, link, title, text, _from):
        self.output += f"[ Link ] {link}\n[ title ] {title}\n[ text ] {text}\n[ From ] {_from}\n\n"

    def set_info(self):
        os.system('clear')
        sp('please fell in the required informations khaled also i should told you that stalking is not good cuz i love you and you made me')
        os.system('clear')
        print('\n\n')
        name = input(red+" Name [ space = unknown ] : ")
        FName = input(cyan+" Father  Name [ space = unknown ] : ")
        GFName = input(purple+" GrandFather Name [ space = unknown ] : ")
        last_name = input(white+" Family name [ space = unknown ] : ")
        os.system('clear')
        if name == "" or name == " ":
            self.name = False
        else:
            self.name = name

        if FName == "" or FName == " ":
            self.FName = False
        else:
            self.FName = FName

        if GFName == "" or GFName == " ":
            self.GFName = False
        else:
            self.GFName = GFName

        if last_name == "" or last_name == " ":
            self.last_name = False
        else:
            self.last_name = last_name

        if self.FName and self.name and self.GFName and self.last_name is None:
            input("Please Add Some Info !")
            sp('please add info')
            os.system('python main.py')

    def search_google(self, sql):
        try:
            engine = Google()
            results = engine.search(sql, pages=2)
            for data in results.__dict__['_results']:
                link = data['link']
                title = data['title']
                text = data['text']
                self.add_info(link, title, text, " google.com")
            print("Done Search in Google")
            sp('done search in Google')
        except:
            pass

    def search_bing(self, sql):
        try:
            engine = Bing()
            results = engine.search(sql, pages=2)
            for data in results.__dict__['_results']:
                link = data['link']
                title = data['title']
                text = data['text']
                self.add_info(link, title, text, " bing.com")
            print("Done Search in Bing")
            os.system('clear')
            sp('done search in bing note i will scan google and bing more than 5 times')
        except:
            pass

    def search_in_social_media(self, sql):
        websites = ['https://t.me/', 'https://instagram.com', 'https://twitter.com', 'https://www.youtube.com/', 'https://mega.nz/', 'https://www.google.com/drive/', 'https://pastebin.com/']
        for x in websites:
            try:
                engine = Google()
                results = engine.search(sql + f"  {x}", pages=2)
                for data in results.__dict__['_results']:
                    link = data['link']
                    title = data['title']
                    text = data['text']
                    self.add_info(link, title, text, " google.com ")
                os.system('clear')
                print(f" Done Search in {x}")
                sp('done search in'+x)
            except:
                pass
        print("Done Search in social media")
        sp('done search in social media')
LordGivt()
# all copyright reserved for khaled
