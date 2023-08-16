import telebot
from telebot.storage import StateMemoryStorage
from dotenv import load_dotenv
import argparse
import random
import time
import os


def get_public_of_photos(args, bot, chat_id):
    abs_path = os.path.abspath('images')
    images = os.listdir(abs_path)
    random.shuffle(images)
    for image in images:
        abs_path = os.path.abspath(f'images/{image}')
        bot.send_photo(chat_id=chat_id, photo=open(abs_path, 'rb'))
        time.sleep(args)

    bot.infinity_polling(skip_pending=True)


def main():
    parser = argparse.ArgumentParser(
        description='Программа даёт возможность опубликовать фотографии,'
                    'находящиеся в папке images каждые X-секунд: '
                    'python notification.py количество секунд'
                    'Если вы укажите количество секунд X, то программа опубликует фотографии каждые 4 часа'
    )
    parser.add_argument('second', nargs='?', default=14400, help='количество секунд')
    args = parser.parse_args()

    state_storage = StateMemoryStorage()
    load_dotenv()
    token = os.getenv('BOT_TOKEN')
    chat_id = os.getenv('BOT_CHAT_ID')

    bot = telebot.TeleBot(token, state_storage=state_storage)

    get_public_of_photos(args, bot, chat_id)


if __name__ == '__main__':
    main()
