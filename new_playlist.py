#!/usr/bin/env python3

import os
import shutil
import json

playlist_url = input("enter playlist url: ")
playlist_name = input("enter playlist name: ")
script_dir = os.path.abspath(os.path.dirname(__file__))
playlists_dir = os.path.join(script_dir, "playlists")
template_file = os.path.join(playlists_dir, "playlist.json.tpl")
playlist_url_prefix = "https://vk.com/video/playlist/-"

playlist_id = playlist_url.replace(playlist_url_prefix, "")

new_playlist_file = os.path.join(playlists_dir, f"{playlist_id}.json")

shutil.copyfile(template_file, new_playlist_file)

with open(new_playlist_file, 'r') as pf:
    playlist = json.load(pf)

with open(new_playlist_file, 'w') as pf:
    playlist["playlist_name"] = playlist_name
    playlist["playlist_url"] = playlist_url

    video_url = ''
    videos = list(playlist["videos_url"])

    while video_url.lower() != 'f':
        video_url = input("Enter video url (f=finish): ")
        if video_url and video_url != 'f':
            videos.append(video_url)

    playlist["videos_url"] = videos
    
    json.dump(playlist, pf, ensure_ascii=False)