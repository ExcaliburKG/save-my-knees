#!/usr/bin/env python3

import os
import subprocess
import shutil
import json

cleanup_videos = False
script_dir = os.path.abspath(os.path.dirname(__file__))
downloaded_videos_dir = os.path.join(script_dir, "videos")
playlists_dir = os.path.join(script_dir, "playlists")
cookie_file = os.path.join(script_dir, "cookies.firefox-private.txt")
video_file_name_template = "%(title)s.%(ext)s"
downloader_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0"

os.makedirs(playlists_dir, exist_ok=True)

if os.path.exists(downloaded_videos_dir) and cleanup_videos:
    shutil.rmtree(downloaded_videos_dir)

os.makedirs(downloaded_videos_dir, exist_ok=True)

for file in os.listdir(playlists_dir):
    filename = os.fsdecode(file)
    if filename.endswith(".json"):
        playlist_file = os.path.join(playlists_dir, filename)
        with open(playlist_file, 'r') as pf:
            playlist = json.load(pf)
        
        videos = playlist["videos_url"]
        playlist_name = playlist["playlist_name"]

        playlist_folder = os.path.join(downloaded_videos_dir, playlist_name)
        os.makedirs(playlist_folder, exist_ok=True)

        for video_url in videos:
            if video_url.startswith("#"):
                continue
            print(f"Downloading {video_url}")
            get_video_formats_cmd = f'yt-dlp "{video_url}" --user-agent "{downloader_user_agent}" -F --cookies "{cookie_file}"'

            p = subprocess.run(get_video_formats_cmd,
                        check=False,
                        shell=True,
                        text=True,
                        cwd=script_dir,
                        capture_output=True)
            print(p.stdout)
            print(p.stderr)
            if p.returncode != 0:
                raise Exception('Unable to get video format')
            video_format = input("Input format: ")

            video_file = os.path.join(playlist_folder, video_file_name_template)

            download_cmd = f'yt-dlp -o "{video_file}" "{video_url}" --user-agent "{downloader_user_agent}" -f {video_format} --cookies "{cookie_file}"'

            p = subprocess.run(download_cmd,
                        check=False,
                        shell=True,
                        text=True,
                        cwd=script_dir,
                        capture_output=True)
            print(p.stdout)
            print(p.stderr)
            if p.returncode != 0:
                raise Exception('Unable to get video')
            
            shutil.move(playlist_file, f"{playlist_file}.done")
            os.system('cls||clear')
            print(f"Playlist {playlist_file} downloaded successfully!")