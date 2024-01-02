import pandas as pd

def analyze_data_quality():
    """
    Analyzes the quality of a dataset by identifying anomalies such as duplicates, null values, and uniqueness violations.
    Generates a report of the anomalies and saves it as 'anomalies_report.csv'.

    Returns:
    None
    """
    try:
        # Cargar el dataset
        df = pd.read_csv('data/processed/dataset.csv')

        # Validar que el DataFrame no esté vacío
        if df.empty:
            raise ValueError("El DataFrame está vacío. No se pueden realizar análisis de calidad de datos.")

        # Inicializar una lista para almacenar anomalías
        anomalies_list = []

        # Visualizar las primeras filas para entender la estructura de datos
        print("Primeras filas del dataset:")
        print(df.head())

        # Validar que todas las columnas necesarias estén presentes
        required_columns = ['disc_number', 'duration_ms', 'explicit', 'track_number', 'track_popularity', 'track_id', 'track_name', 'audio_features.danceability', 'audio_features.energy', 'audio_features.key', 'audio_features.loudness', 'audio_features.mode', 'audio_features.speechiness', 'audio_features.acousticness', 'audio_features.instrumentalness', 'audio_features.liveness', 'audio_features.valence', 'audio_features.tempo', 'audio_features.id', 'audio_features.time_signature', 'artist_id', 'artist_name', 'artist_popularity', 'album_id', 'album_name', 'album_release_date', 'album_total_tracks']
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Faltan las siguientes columnas necesarias en el DataFrame: {', '.join(missing_columns)}")

        # Buscar duplicados
        duplicates = df[df.duplicated()]
        if len(duplicates) > 0:
            anomalies_list.append({'Tipo': 'Duplicados', 'Descripción': 'Filas duplicadas', 'Detalles': f'{len(duplicates)} filas duplicadas'})

        # Revisar la completitud: contar valores nulos por columna
        print("\nValores nulos por columna:")
        null_counts = df.isnull().sum()
        for col, cnt in null_counts.items():
            if cnt > 0:
                anomalies_list.append({'Tipo': 'Valor Nulo', 'Descripción': f'Valores nulos en columna {col}', 'Detalles': f'{cnt} valores nulos'})

        # Verificar unicidad en columnas que deben ser únicas (e.g., IDs)
        unique_track_ids = df['track_id'].nunique()
        if unique_track_ids != len(df):
            anomalies_list.append({'Tipo': 'Unicidad', 'Descripción': 'IDs de pista no son únicos', 'Detalles': f'{len(df) - unique_track_ids} IDs repetidos'})

        # Aquí puedes agregar más análisis específicos, como valores atípicos, inconsistencias, etc.

        # Convertir la lista de anomalías a un DataFrame y guardar el reporte de anomalías
        anomalies = pd.DataFrame(anomalies_list, columns=['Tipo', 'Descripción', 'Detalles'])
        anomalies.to_csv('data/anomalies/anomalies_report.csv', index=False)

        print("\nAnálisis de calidad de datos completado. Reporte de anomalías guardado como 'anomalies_report.csv'.")

    except Exception as e:
        print(f"Error durante el análisis de calidad de datos: {str(e)}")

# Llamar a la función para analizar la calidad de datos
analyze_data_quality()
