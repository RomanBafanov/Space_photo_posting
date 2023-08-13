import telebot
from telebot.storage import StateMemoryStorage
from dotenv import load_dotenv
import argparse
import random
import time
import os


state_storage = StateMemoryStorage()

load_dotenv()
token = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(token, state_storage=state_storage)


def publication_of_photos(args):
    abs_path = os.path.abspath('images')
    images = os.listdir(abs_path)
    random.shuffle(images)
    for image in images:
        abs_path = os.path.abspath(f'images/{image}')
        bot.send_photo(chat_id='-1001692357239', photo=open(abs_path, 'rb'))
        time.sleep(args)

    bot.infinity_polling(skip_pending=True)


def main():
    parser = argparse.ArgumentParser(
        description='Программа даёт возможность опубликовать фотографии,'
                    'находящиеся в папке images каждые X-секунд: '
                    'python notification.py количество секунд'
                    'Если вы укажите количество секунд X, то программа опубликует фотографии каждые 4 часа'
    )
    parser.add_argument('second', help='количество секунд')
    args = parser.parse_args()
    if args == 'X':
        args = 14400
    publication_of_photos(args)


if __name__ == '__main__':
    main()
