#!/usr/bin/env python3

import os
import sys
import subprocess
import shutil

with open(os.path.abspath('./youtube.txt'), 'r') as src:
    videos = src.readlines()

current_dir = os.path.abspath(os.path.dirname(__file__))
downloaded_videos_dir = os.path.join(current_dir, "videos")

if os.path.exists(downloaded_videos_dir):
    shutil.rmtree(downloaded_videos_dir)

os.makedirs(downloaded_videos_dir, exist_ok=True)

for video_url in videos:
    if video_url.startswith("#"):
        continue
    print(f"Downloading {video_url}")
    get_video_formats_cmd = f'/home/kirill/.local/bin/yt-dlp "{video_url}" --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0" -F --cookies "/mnt/c/Users/gorbu/Documents/save-my-knees/cookies.firefox-private.txt"'

    p = subprocess.run(get_video_formats_cmd,
                   check=False,
                   shell=True,
                   text=True,
                   cwd=current_dir,
                   capture_output=True)
    print(p.stdout)
    print(p.stderr)
    if p.returncode != 0:
        raise Exception('Unable to get video format')
    video_format = input("Input format: ")

    download_cmd = f'/home/kirill/.local/bin/yt-dlp -o "{downloaded_videos_dir}/%(title)s-%(id)s.%(ext)s" "{video_url}" --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0" -f {video_format} --cookies "/mnt/c/Users/gorbu/Documents/save-my-knees/cookies.firefox-private.txt"'

    p = subprocess.run(download_cmd,
                   check=False,
                   shell=True,
                   text=True,
                   cwd=current_dir,
                   capture_output=True)
    print(p.stdout)
    print(p.stderr)
    if p.returncode != 0:
        raise Exception('Unable to get video')
    
    os.system('cls||clear')