import re
import lyricsgenius

genius_token = 'I0tQPG70zMkfR7uRcBpqQN9j15brk5kH2dBnKLtg71FwHuzBPHNrYG0JujeMMyEe'
genius = lyricsgenius.Genius(genius_token)

def clean_lyrics(song):

    lyrics = song.lyrics
    lyrics = lyrics.split('\n')
    lyrics = [line for line in lyrics if line != '']
    lyrics = [line for line in lyrics if not line.startswith('[')]
    lyrics = lyrics[1:]

    last_element = lyrics[-1]
    match = re.search(r'\d', last_element)
    
    if match:
        position = match.start()
        lyrics[-1] = last_element[:position]
    
    return lyrics


def get_lyrics(artist, song_name):

    song = genius.search_song(song_name, artist)
    lyrics = clean_lyrics(song)
    return lyrics
