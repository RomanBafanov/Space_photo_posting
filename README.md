# API_2

Данный скрипт даёт возможность загрузить, сохранить,
а также опубликовать фотографии космоса

## Как установить

Python3 должен быть уже установлен. Затем используйте pip 
(или pip3, если есть конфликт с Python2) для установки зависимостей:

```bash
pip install -r requirements.txt
``` 

### will be installed:

requests~=2.31.0
python-dotenv~=1.0.0
pyTelegramBotAPI==4.12.0

## Переменные окружения

Необходимо создать файл **.env**, в нём должен содержаться API ключ полученный 
Вами на сайте **https://api.nasa.gov/**  Переменная должна иметь имя **API_KEY_NASA**

```bash
API_KEY_NASA='API ключ'
```

Так же Вам необходимо создать бота и получить токен бота в телеграмме
**https://t.me/BotFather**, который будет отправлять фотографии. 
Переменная должна иметь имя **BOT_TOKEN**

```bash
BOT_TOKEN='токен бота'
```

## Как пользоваться

Для скачивания фотографий запуска ракет запустите скрипт **fetch_spacex_images.py**. 
Далее введите id-запуска, фотографии которого вы хотите получить. 
Для работы в терминале используйте команду **python main.py ваша ссылка**.

```bash
$ python fetch_spacex_images.py 5eb87d47ffd84e000754b38a
```

В случае если Вы не знаете id-запуска, то введите none и скачаются фотографии 
с последнего запуска.

```bash
$ python fetch_spacex_images.py none
```

Если у вас возникли трудности наберите **python fetch_spacex_images.py -h**

```bash
python fetch_spacex_images.py -h
Программа даёт возможность скачать фотографии сделанные c запусков NASA: python fetch_spasex_images.py id-запускаЕсли вы укажите id-запуска none, то программа
скачает фотографии с последнего запуска

positional arguments:
  space_id    id-запуска

options:
  -h, --help  show this help message and exit
```

Для скачивания фотографий дня NASA запустите скрипт **fetch_NASA_day-images.py**. 
Далее введите количество фотографий которых хотите получить. 
Для работы в терминале используйте команду **python fetch_NASA_day-images.py количество фотографий**.

```bash
$ python fetch_NASA_day-images.py количество фотографий
```

Если у вас возникли трудности наберите **python fetch_NASA_day-images.py -h**

```bash
Программа даёт возможность скачать фотографии дня сделанные NASA : python fetch_NASA_day-images.py Количество фотографий

positional arguments:
  count       Количество фотографий

options:
  -h, --help  show this help message and exit
```

Для скачивания фотографий NASA Земли запустите скрипт **fetch_NASA_earth-images.py**.
Для работы в терминале используйте команду **python fetch_NASA_earth-images.py**.

```bash
$ python fetch_NASA_earth-images.py
```

Если у вас возникли трудности наберите **python fetch_NASA_earth-images.py -h**

```bash
Программа даёт возможность скачать фотографии Земли сделанные NASA: python fetch_NASA_earth-images.py

options:
  -h, --help  show this help message and exit
```

Для запуска публикаций сохранённых фотографий запустите скрипт **notification.py**.
Далее введите количество секунд через которые будут публиковаться фотографии.
Для работы в терминале используйте команду **python notification.py количество секунд**.

```bash
$ python notification.py 30
```

В случае если вы введёте количество секунд X, то программа будет публиковать фотографии каждые 4 часа.

```bash
$ python notification.py X
```

Если у вас возникли трудности наберите **python notification.py -h**

```bash
Программа даёт возможность опубликовать фотографии,находящиеся в папке images каждые X-секунд: python notification.py количество секундЕсли вы укажите количество  
секунд X, то программа опубликует фотографии каждые 4 часа

positional arguments:
  second      количество секунд

options:
  -h, --help  show this help message and exit
```

## Цель проекта

Проект создан для скачивания фотографий космоса с запусков ракет, 
фотографий дня, фотографий нашей планеты, а так же запуска публикаций фотографий в телеграмм канал.
