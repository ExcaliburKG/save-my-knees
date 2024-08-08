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
    download_cmd = f'youtube-dl.exe --verbose -o "{downloaded_videos_dir}\%(title)s-%(id)s.%(ext)s" {video_url}'
    print(download_cmd)
    p = subprocess.run(download_cmd,
                   check=True,
                   text=True,
                   cwd=current_dir,
                   capture_output=True)
    print(p.stdout)
    print(p.stderr)