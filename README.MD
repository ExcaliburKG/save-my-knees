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

Все ссылки на видео складываем в файлик youtube.txt в формате
https://www.youtube.com/watch?v=ISbaz49DPKo
https://www.youtube.com/watch?v=ASVax45GPzo
...

то есть копируем из браузера полный урл и вставляем.
Скрипт возьмет все ссылки и скачает их в папку
Как запускать скрипт скачивания:
```
python download_videos.py
```
При запуске скрипт предложит выбрать формат для видео и аудио - выбираем самый большой размер из таблицы на экране и вводим в формате:
```
137+140
```