Ставим Ubuntu Linux из магазина
https://apps.microsoft.com/detail/9pn20msr04dw?hl=en-us&gl=RU

В Ubuntu терминале выполняем

Клонируем репо yt-dlp
```
sudo apt-get install python3-pip
git clone --recursive https://github.com/yt-dlp/yt-dlp.git
cd yt-dlp
pip install .
```

Создание плейлиста с названием и ссылками на видео делается скриптом:
```
python new_playlist.py
```
Копируем из браузера полный урл и вставляем.


Как запускать скрипт скачивания:
```
python download_videos.py
```
При запуске скрипт предложит выбрать формат для видео и аудио - выбираем самый большой размер из таблицы на экране и вводим в формате:
```
137+140
```

Скрипт возьмет все ссылки и скачает их в папку videos/%playlist_name%