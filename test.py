#!/usr/bin/env python3

from pprint import pprint
from ytmusicapi import YTMusic

auth_file="/home/smipi1/.ytmusic_auth.json"

# YTMusic.setup(auth_file)

yt = YTMusic(auth_file)

ls = subs=yt.get_library_subscriptions()

for s in subs:
    print(f"{s['artist']}:")
    uploads=yt.get_playlist(s['browseId'])
    print(f"\t{uploads}")

