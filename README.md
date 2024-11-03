# Playlist-Syncer
Sync your liked songs and a playlist with one click

To use the syncer, make sure you are logged into spotify on your device and have all the dependicies installed. 
Then just change the custom_playlist_id variable to whatever the id of the playlist you want synced is.

To get the id of your playlist share you playlist and copy the link, for example: https://open.spotify.com/album/3cQO7jp5S9qLBoIVtbkSM1?si=-AAphYydRAqPZ739s6Jt1Q
Your id will be the string after album/ and before ?si=. In this case it is 3cQO7jp5S9qLBoIVtbkSM1. (Obviously you won't be able to change this playlist in the example)

On your first time running the script it will generate a .cache file with your spotify access token, don't share this with anyone.
After a certain amount of time your access token will need to be refreshed so it wil create the .cache file again, nothing you need to worry about in case you're wondering why it sometimes briefly opens a browser tab.
