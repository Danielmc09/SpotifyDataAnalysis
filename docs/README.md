# Análisis de Calidad de Datos de Spotify

## Descripción

Este proyecto consiste en un análisis de calidad de datos extraídos de la API de Spotify, enfocándose en los datos relacionados con álbumes y pistas musicales, específicamente en los trabajos de Taylor Swift. El objetivo es identificar anomalías y asegurar la calidad de los datos para futuros análisis.

## Estructura del Proyecto

```plaintext
SpotifyDataAnalysis/
│
├── data/
│   ├── raw/
│   │   └── taylor_swift_spotify.json    # Datos originales extraídos de la API
│   │
│   ├── processed/
│   │   └── dataset.csv                  # Datos procesados y limpios
│   │
│   └── anomalies/
│       └── anomalies_report.csv         # Reporte de anomalías encontradas
│
├── src/
│   ├── analisis_file.py                 # Script principal de análisis
│   └── anomalies_dataset.py             # Script para generar el reporte de anomalías
│
├── docs/
│   └── README.md                        # Documentación del proyecto
│
├── requirements.txt                     # Librerías necesarias para el proyecto
│
└── .gitignore                           # Archivos y carpetas ignorados por git
```

## Funcionalidades

- **Limpieza de Datos**: Normalización y limpieza de datos para preparar el análisis.
- **Detección de Anomalías**: Identificación de duplicados, valores nulos y anomalías en los datos.
- **Reporte de Anomalías**: Generación de un informe detallado con todas las anomalías encontradas.

## Tecnologías Utilizadas

- **Python**: Lenguaje principal para el procesamiento y análisis de datos.
- **Pandas**: Biblioteca de Python utilizada para la manipulación y análisis de datos.

## Cómo usar

1. **Preparación del entorno**:
   - Asegúrate de tener Python instalado en tu sistema.
   - Instala las dependencias necesarias utilizando el archivo `requirements.txt`:

     ```
     pip install -r requirements.txt
     ```

2. **Ejecución del script**:
   - Coloca el archivo de datos `taylor_swift_spotify.json` en el directorio del proyecto.
   - Ejecuta el script `read_json_spotify.py` para comenzar el análisis.
   - Revisa el archivo `dataset.csv` generado para ver los datos analizados y limpios.
   - Ejecuta el script `anomalies_dataset.py` para encontrar las anomalias.
   - Consulta el archivo `anomalies_report.csv` para ver las anomalías detectadas.


Autor: <a href="https://www.linkedin.com/in/angeldanielmendieta/">Angel Daniel Menideta Castillo</a> © 2024
