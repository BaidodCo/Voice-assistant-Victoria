# all copyright reserved for khaled
from gtts import gTTS
import os
import datetime
from colorama import Fore
from fuzzywuzzy import fuzz
import pyjokes
from autocorrect import Speller
import tldextract
import requests
from data import knowledge_base
from lists import listexit, listsleep, currenttime, reset, teleuser, joke, spy, helpp, calculatee

current_time = datetime.datetime.now()

# Some Colors
red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
white = Fore.WHITE
yellow = Fore.YELLOW
purple = Fore.MAGENTA
cyan = Fore.CYAN

spell = Speller(lang='en')

def speak(text):
    speech = gTTS(text=text, slow=False)
    speech.save("output.mp3")
    os.system('play output.mp3')

def open_url(url):
    domain = tldextract.extract(url)
    base_url = f"{domain.domain}.{domain.suffix}"
    os.system(f"termux-open-url https://{base_url}")

def process_user_input(user_input):
    user_input = user_input.lower().strip()
# all copyright reserved for khaled
    # Autocorrect
    user_input = spell(user_input)

    # Check for known places
    for place, info in knowledge_base["places"].items():
        if place in user_input:
            return info

    for conversation in knowledge_base["conversation"]:
        if conversation in user_input:
            return knowledge_base["conversation"][conversation]

    for badword in knowledge_base["badwords"]:
        if badword in user_input:
            return knowledge_base["badwords"][badword]

    highest_ratio = 75
    best_match = None

    for weapon in knowledge_base["weapons"]:
        ratio = fuzz.ratio(weapon, user_input)
        if ratio > highest_ratio:
            highest_ratio = ratio
            best_match = weapon

    if best_match:
        return knowledge_base["weapons"][best_match]

    # Handle long questions with fuzzy matching
    for question in knowledge_base["long_questions"]:
        ratio = fuzz.partial_ratio(question, user_input)
        if ratio >= 80:  # Adjust threshold as needed
            return knowledge_base["long_questions"][question]

    return "I'm sorry, I couldn't understand your input."

def main():
    os.system('clear')
    print("")
    print(cyan + "[!] Victoria Assassinate")
    print(purple + "[¡] Built By Khaled + baidodgo team owned by khaled")

    print("")
    print("")
    

# all copyright reserved for khaled

    while True:
        os.system("clear")
        print(cyan + "[!] Victoria Assassinate")
        print(purple + "[¡] Built By Khaled + baidodgo team owned by khaled")
        print("")
        user_input = input(white + "[?] Ask Me A Question" + yellow + ' :' + green + ' ').lower().strip()

        if user_input in listexit:
            speak('Goodnight Darling')
            exit()
        elif user_input in listsleep:
            os.system('python files/sleep.py')
            speak('Good Morning')
            os.system('clear')
        elif user_input in currenttime:
            speak(f'The time is {current_time.strftime("%H:%M")}')
            os.system('clear')
        elif user_input in reset:
            speak('Okay Done')
            os.system('python main.py')
        elif user_input in teleuser:
            os.system('python files/teleuser.py')
        elif user_input in joke:
            joke_text = pyjokes.get_joke()
            speak(joke_text)
        elif user_input in spy:
            os.system('python spy/search.py')
            # Implement spy logic here if needed
        elif user_input in helpp:
            os.system('python files/help.py')
        elif user_input in calculatee:
            speak('I can help with calculations. Please provide the expression.')
            # Implement calculation logic here if needed
        elif 'snapcheck' in user_input:
            email = user_input.replace('snapcheck', "").strip()
            res = requests.post('https://bitmoji.api.snapchat.com/api/user/find', data={'email': email}).text
            if '{"account_type":"bitmoji"}' in res:
                speak(f'Bitmoji account found for {email}')
            elif '{"account_type":"snapchat"}' in res:
                speak(f'Snapchat account found for {email}')
            else:
                speak('Something went wrong, please check your input')
        elif 'open' in user_input:
            query = user_input.replace('open', "").strip()
            if query in ['google', 'youtube', 'instagram', 'snapchat', 'stackoverflow']:
                speak(f'Okay, opening {query} in your browser.')
                open_url(f"https://www.{query}.com")
            else:
                speak("Sorry, I don't know the website you're referring to.")
        else:
            response = process_user_input(user_input)
            speak(response)

if __name__ == "__main__":
    main()
# all copyright reserved for khaled
