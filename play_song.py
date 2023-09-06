import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

os.environ["SPOTIPY_CLIENT_ID"] = "345dff2ee8f543509908fd0317855e77"
os.environ["SPOTIPY_CLIENT_SECRET"] = "08054ad8eec44862be126dccc1328d8a"
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8080"  # Puedes cambiar esto si lo necesitas

scope = "user-modify-playback-state,user-read-playback-state"
cache_path = "token_cache"  # Define la ruta del archivo de caché para almacenar el token

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, cache_path=cache_path))

def search_track(artist, track_title):
    query = f"artist:{artist} track:{track_title}"
    result = sp.search(q=query, type="track", limit=1)

    if result["tracks"]["total"] > 0:
        track = result["tracks"]["items"][0]
        print(f"Encontrada: {track['name']} por {track['artists'][0]['name']}")
        print(f"ID de la canción: {track['id']}")
        return track["id"]
    else:
        print("No se encontró la canción.")
        return None
    
def get_available_devices():
    devices = sp.devices()
    if devices["devices"]:
        return devices["devices"]
    else:
        print("No se encontraron dispositivos disponibles.")
        return None

def play_on_device(track_id, device_id):
    if track_id and device_id:
        sp.start_playback(device_id=device_id, uris=[f"spotify:track:{track_id}"])
    else:
        print("No se puede reproducir la canción: falta el ID de la canción o del dispositivo.")

def play_song(artist, track_title):
    track_id = search_track(artist, track_title)
    devices = get_available_devices()
    if devices:
        device_id = devices[0]["id"]
        print(f"Reproduciendo en el dispositivo: {devices[0]['name']}")
        play_on_device(track_id, device_id)
