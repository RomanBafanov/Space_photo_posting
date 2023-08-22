from dotenv import load_dotenv
from save_foto import save_photo
import requests
import os

URL = 'https://api.nasa.gov/EPIC/archive/natural'
NUMBER_OF_PHOTOS = 5


def get_image_date(api_key, count):
    url = URL
    params = {
        'api_key': api_key,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    photo_details = response.json()


    date = photo_details[count]['date'].split()[0].split('-')
    image = photo_details[count]['image']

    return date, image


def main():
    load_dotenv()
    api_key = os.getenv('API_KEY_NASA')
    params = {
        'api_key': api_key,
    }
    for count in range(NUMBER_OF_PHOTOS):
        date, image = get_image_date(api_key, count)

        url = f'{URL}/{date[0]}/{date[1]}/{date[2]}/png/{image}.png'
        filename = f'images/Earth{count}.png'

        save_photo(url, filename, params)


if __name__ == '__main__':
    main()
