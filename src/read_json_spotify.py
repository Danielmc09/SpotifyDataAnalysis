import json
import pandas as pd

def process_spotify_data():
    """
    Reads a JSON file containing Spotify data, processes the data, and saves it as a CSV file.

    Returns:
    - None
    """
    try:
        # Leer el archivo JSON
        with open('data/raw/taylor_swift_spotify.json') as file:
            data = json.load(file)

        # Validar que el archivo JSON contiene la estructura esperada
        if 'artist_id' not in data or 'artist_name' not in data or 'artist_popularity' not in data or 'albums' not in data:
            raise ValueError("El archivo JSON no contiene la estructura esperada")

        # Procesar los datos (Este paso dependerá del formato específico que necesitas)
        tracks = []
        for album in data['albums']:
            if 'album_id' not in album or 'album_name' not in album or 'album_release_date' not in album or 'album_total_tracks' not in album or 'tracks' not in album:
                raise ValueError("La estructura de un álbum en el archivo JSON no es válida")
            for track in album['tracks']:
                if 'disc_number' not in track or 'duration_ms' not in track or 'explicit' not in track or 'track_number' not in track or 'track_popularity' not in track or 'track_id' not in track or 'track_name' not in track or 'audio_features' not in track:
                    raise ValueError("La estructura de una pista en el archivo JSON no es válida")
                track_info = {
                    'disc_number': track['disc_number'],
                    'duration_ms': track['duration_ms'],
                    'explicit': track['explicit'],
                    'track_number': track['track_number'],
                    'track_popularity': track['track_popularity'],
                    'track_id': track['track_id'],
                    'track_name': track['track_name'],
                    'audio_features.danceability': track['audio_features']['danceability'],
                    'audio_features.energy': track['audio_features']['energy'],
                    'audio_features.key': track['audio_features']['key'],
                    'audio_features.loudness': track['audio_features']['loudness'],
                    'audio_features.mode': track['audio_features']['mode'],
                    'audio_features.speechiness': track['audio_features']['speechiness'],
                    'audio_features.acousticness': track['audio_features']['acousticness'],
                    'audio_features.instrumentalness': track['audio_features']['instrumentalness'],
                    'audio_features.liveness': track['audio_features']['liveness'],
                    'audio_features.valence': track['audio_features']['valence'],
                    'audio_features.tempo': track['audio_features']['tempo'],
                    'audio_features.id': track['audio_features']['id'],
                    'audio_features.time_signature': track['audio_features']['time_signature'],
                    'artist_id': data['artist_id'],
                    'artist_name': data['artist_name'],
                    'artist_popularity': data['artist_popularity'],
                    'album_id': album['album_id'],
                    'album_name': album['album_name'],
                    'album_release_date': album['album_release_date'],
                    'album_total_tracks': album['album_total_tracks'],
                }
                tracks.append(track_info)

        # Convertir a DataFrame de Pandas
        df = pd.DataFrame(tracks)

        # Guardar como CSV
        df.to_csv('data/processed/dataset.csv', index=False)
        print("Procesamiento y guardado completados.")

    except Exception as e:
        print(f"Error durante el procesamiento: {str(e)}")

# Llamar a la función para procesar los datos
process_spotify_data()
