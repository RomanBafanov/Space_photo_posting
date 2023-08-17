from dotenv import load_dotenv
from save_foto import *
import requests
import argparse


URL = 'https://api.nasa.gov/EPIC/archive/natural'
NUMBER_OF_PHOTOS = 5

def get_earth_images(date, image, idx, api_key):
    url = f'{URL}/{date[0]}/{date[1]}/{date[2]}/png/{image}.png'
    params = {
        'api_key': api_key,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()

    filename = f'images/Earth{idx}.png'

    return response.url, filename


def get_image_date(api_key, count):
    url = URL
    params = {
        'api_key': api_key,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()


    date = data[count]['date'].split()[0].split('-')
    image = data[count]['image']

    return date, image, api_key


def main():
    parser = argparse.ArgumentParser(
        description='Программа даёт возможность скачать фотографии Земли сделанные NASA: '
                    'python fetch_NASA_earth-images.py'
    )
    parser.parse_args()

    load_dotenv()
    api_key = os.getenv('API_KEY_NASA')
    for count in range(NUMBER_OF_PHOTOS):
        date, image, api_key = get_image_date(api_key, count)

        url, filename = get_earth_images(date, image, count, api_key)

        save_photo(url, filename)


if __name__ == '__main__':
    main()
