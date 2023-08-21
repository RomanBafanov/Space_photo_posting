import requests
import os


def save_photo(url, filename):
    response = requests.get(url)
    response.raise_for_status()

    new_folder = 'images'
    os.makedirs(new_folder, exist_ok=True)

    with open(filename, 'wb') as file:
        file.write(response.content)


def save_photo_whith_params(url, params, filename):
    response = requests.get(url, params=params)
    response.raise_for_status()

    new_folder = 'images'
    os.makedirs(new_folder, exist_ok=True)

    with open(filename, 'wb') as file:
        file.write(response.content)