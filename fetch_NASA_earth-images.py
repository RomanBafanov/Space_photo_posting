from dotenv import load_dotenv
from save_foto import *
import requests
import argparse


URL = 'https://api.nasa.gov/EPIC/archive/natural'


def get_earth_images(date, image,idx, api_key):
    url = f'{URL}/{date[0]}/{date[1]}/{date[2]}/png/{image}.png'
    params = {
        'api_key': api_key,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()

    filename = f'images/Earth{idx}.png'
    save_photo(response.url, filename)


def get_image_date(api_key):
    url = URL
    params = {
        'api_key': api_key,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    json_data = response.json()
    idx = 1
    for count in range(5):
        date = json_data[count]['date'].split()[0].split('-')
        image = json_data[count]['image']

        get_earth_images(date, image, idx, api_key)


def main():
    parser = argparse.ArgumentParser(
        description='Программа даёт возможность скачать фотографии Земли сделанные NASA: '
                    'python fetch_NASA_earth-images.py'
    )
    args = parser.parse_args()

    load_dotenv()
    api_key = os.getenv('API_KEY_NASA')
    get_image_date(api_key)


if __name__ == '__main__':
    main()
