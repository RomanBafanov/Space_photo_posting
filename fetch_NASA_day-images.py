from dotenv import load_dotenv
from save_foto import save_photo
import requests
import argparse
import os


URL = 'https://api.nasa.gov'


def get_space_images(api_key, count):
    params = {
        'api_key': api_key,
        'count': count,
    }
    url = f'{URL}/planetary/apod'
    response = requests.get(url, params=params)
    response.raise_for_status()

    for count, photo_details in enumerate(response.json()):
        photo = photo_details['url']
        extension = get_extension(photo)
        if extension:
            filename = f'images/NASA_day-foto{count}{extension}'
            save_photo(photo, filename)


def get_extension(link):
    file_extension = os.path.splitext(link)
    extension = file_extension[1]

    return extension


def main():
    parser = argparse.ArgumentParser(
        description='Программа даёт возможность скачать фотографии дня сделанные NASA : '
                    'python fetch_NASA_day-images.py Количество фотографий'
    )
    parser.add_argument('count', help='Количество фотографий')
    args = parser.parse_args()
    count = args.count
    load_dotenv()
    api_key = os.getenv('API_KEY_NASA')

    get_space_images(api_key, count)


if __name__ == '__main__':
    main()
