import requests
import random
import pyfiglet
import os
from gtts import gTTS


# all copyright reserved for khaled
def sp(text):
  speech = gTTS(text=text, slow=False)
  speech.save("vic.mp3")
  os.system('play vic.mp3')



#telegram id and token 
# all copyright reserved for khaled

ID = ""
token = ""



requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text=")

na = '1234567890qwertyuioplkjhgfdsazxcvbnm'

def user():
 user = (''.join(random.choice(na)for i in range(5)))
 url = f'https://t.me/{user}'
 re = requests.get(url).text
 if '"robots"' in re:
     sp("i found a user and its"+user+"i have send it to Khaled Telegram")
 else:
    sp("i found a user and its"+user+"i have send it to Khaled Telegram")
    requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=✨ Here You Go Mr Khaled : @{user}')
    os.system("python main.py")
  


user()
# all copyright reserved for khaled
