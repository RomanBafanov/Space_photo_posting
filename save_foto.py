import requests
import os


def save_photo(url, filename):
    response = requests.get(url)
    response.raise_for_status()

    new_folder = 'images'
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)

    with open(filename, 'wb') as file:
        file.write(response.content)