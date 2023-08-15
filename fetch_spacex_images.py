from save_foto import *
import requests
import argparse


def fetch_spacex_last_launch(space_id):
    url = f'https://api.spacexdata.com/v5/launches/{space_id}'
    response = requests.get(url)
    response.raise_for_status()

    links = response.json()['links']['flickr']['original']
    idx = 1
    for foto in links:
        filename = f'images/spaceX{idx}.jpg'
        idx += 1
        save_photo(foto, filename)


def main():
    parser = argparse.ArgumentParser(
        description='Программа даёт возможность скачать фотографии сделанные c запусков NASA: '
                    'python fetch_spacex_images.py id-запуска'
                    'Если вы укажите id-запуска none, то программа скачает фотографии с последнего запуска'
    )
    parser.add_argument('space_id', help='id-запуска')
    args = parser.parse_args()
    space_id = args.space_id
    if space_id == 'none':
        space_id = '5eb87d47ffd86e000604b38a'
    fetch_spacex_last_launch(space_id)


if __name__ == '__main__':
    main()
