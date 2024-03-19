import json
import pandas as pd

def process_spotify_data():
    try:
        with open('../data/raw/taylor_swift_spotify.json') as file:
            data = json.load(file)

        if 'artist_id' not in data or 'artist_name' not in data or 'artist_popularity' not in data or 'albums' not in data:
            raise ValueError("El archivo JSON no contiene la estructura esperada")

        tracks = []
        for album in data['albums']:
            if 'album_id' not in album or 'album_name' not in album or 'album_release_date' not in album or 'album_total_tracks' not in album or 'tracks' not in album:
                raise ValueError("La estructura de un álbum en el archivo JSON no es válida")
            for track in album['tracks']:
                if 'disc_number' not in track or 'duration_ms' not in track or 'explicit' not in track or 'track_number' not in track or 'track_popularity' not in track or 'track_id' not in track or 'track_name' not in track or 'audio_features' not in track:
                    raise ValueError("La estructura de una pista en el archivo JSON no es válida")
                
                # Usar la expansión de diccionarios para simplificar la creación de track_info
                track_info = {**track, **track['audio_features'],
                                'artist_id': data['artist_id'],
                                'artist_name': data['artist_name'],
                                'artist_popularity': data['artist_popularity'],
                                'album_id': album['album_id'],
                                'album_name': album['album_name'],
                                'album_release_date': album['album_release_date'],
                                'album_total_tracks': album['album_total_tracks']
                            }
                # Eliminar la clave 'audio_features' ya que sus valores se han expandido
                track_info.pop('audio_features', None)
                tracks.append(track_info)

        df = pd.DataFrame(tracks)
        df.to_csv('../data/processed/dataset.csv', index=False)
        print("Procesamiento y guardado completados.")

    except Exception as e:
        print(f"Error durante el procesamiento: {str(e)}")

process_spotify_data()
