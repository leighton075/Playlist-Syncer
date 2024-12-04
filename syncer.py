import spotipy
from spotipy import SpotifyOAuth

CLIENT_ID = 'client_id from spotify dev app here'
CLIENT_SECRET = 'client_secret from spotify dev app here'
REDIRECT_URI = 'redirect_uri from spotify dev app here'
CUSTOM_PLAYLIST_ID = 'custom palylist id here'

scope = 'user-library-read playlist-modify-private playlist-modify-public'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=scope))
print('Authenticated successfully')
liked_songs = []
results = sp.current_user_saved_tracks()
print('Fetching liked songs...')

# Get all the songs in your liked songs
while results:
    for item in results['items']:
        track = item['track']
        liked_songs.append(track['id'])
    results = sp.next(results) if results['next'] else None
print(f'Total liked songs retrieved: {len(liked_songs)}')

custom_playlist_songs = []
results = sp.playlist_items(CUSTOM_PLAYLIST_ID)
print(f'Fetching songs from palylist ID: {CUSTOM_PLAYLIST_ID}')

# Get all the songs in your custom playlist
while results:
    for item in results['items']:
        track = item['track']
        if track and track['id']:
            custom_playlist_songs.append(track['id'])
    results = sp.next(results) if results['next'] else None
print(f'Total songs retreived from custom playlist: {len(custom_playlist_songs)}')

# Determine which tracks need to be added and removed
tracks_to_add = [track_id for track_id in liked_songs if track_id not in custom_playlist_songs]
tracks_to_remove = [track_id for track_id in custom_playlist_songs if track_id not in liked_songs and track_id is not None]
print(f'Track to add: {len(tracks_to_add)}')
print(f'Tracks to remove: {len(tracks_to_remove)}')

# Spotify only supports adding up to 100 songs at a time so anything greater than that needs to be added in batches
def batch_add_tracks(playlist_id, tracks, batch_size=100):
    for i in range(0, len(tracks), batch_size):
        sp.playlist_add_items(playlist_id, tracks[i:i + batch_size])
        print(f'Added {len(tracks[i:i + batch_size])} songs to your custom playlist')

# Add songs to playlist
if tracks_to_add:
    print('Adding new tracks to playlist...')
    batch_add_tracks(CUSTOM_PLAYLIST_ID, tracks_to_add)
 
# Removed songs from playlist   
if tracks_to_remove:
    print('Removing extra tracks from playlist...')
    sp.playlist_remove_all_occurrences_of_items(CUSTOM_PLAYLIST_ID, tracks_to_remove)
    print(f'Removed {len(tracks_to_remove)} songs from your custom playlist')
    
if not tracks_to_add and not tracks_to_remove:
    print("Your custom playlist is already up to date with your liked songs")
